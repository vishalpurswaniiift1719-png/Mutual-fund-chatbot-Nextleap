import os
import json
import glob
from bs4 import BeautifulSoup
from backend.config import RAW_DATA_DIR, PROCESSED_DATA_DIR, FUNDS_DATA_PATH, FUND_METADATA_PATH, CITATIONS_INDEX_PATH
import datetime

def parse_html_files():
    """Parse all scraped HTML files and extract structured mutual fund data."""
    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
    
    html_files = glob.glob(str(RAW_DATA_DIR / "*.html"))
    print(f"Found {len(html_files)} HTML files to parse.")
    
    funds_data = []
    metadata = {}
    citations = {}
    
    today_str = datetime.date.today().isoformat()
    
    for filepath in html_files:
        filename = os.path.basename(filepath)
        slug = filename.replace('.html', '')
        source_url = f"https://www.indmoney.com/mutual-funds/{slug}"
        
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        soup = BeautifulSoup(html_content, 'html.parser')
        next_data_tag = soup.find('script', id='__NEXT_DATA__')
        
        if not next_data_tag:
            print(f"Warning: No __NEXT_DATA__ found in {filename}")
            continue
            
        try:
            data = json.loads(next_data_tag.string)
            mf = data.get('props', {}).get('pageProps', {}).get('mutualFundsDetailData', {})
            
            if not mf or 'data' not in mf:
                print(f"Warning: No mutualFundsDetailData.data in {filename}")
                continue
                
            fund_data = mf['data']
            fund_name = fund_data.get('name', 'Unknown Fund')
            
            # The API doesn't seem to have a flat "category" field, but it has tag_links
            category = "Unknown Category"
            tags = fund_data.get('tag_links', [])
            if tags and len(tags) > 2:
                category = tags[-1].get('name', 'Unknown Category')
                
            scheme_code = str(fund_data.get('fund_id', ''))
            
            fund_overview_info = fund_data.get('fund_overview', {}).get('info', [])
            info_dict = {str(item.get('name', '')).lower(): item.get('value', 'Not available') for item in fund_overview_info}
            
            # Additional fields are inside fund_data or its widgets (like peers, fundamentals)
            # For this MVP, we will try to extract what we can, and fallback to generic text.
            # RAG will rely on text chunks anyway.
            
            # Min SIP / Lumpsum comes as "₹100/₹100"
            min_inv = info_dict.get('min lumpsum/sip', 'Not available')
            min_lumpsum = min_inv.split('/')[0] if '/' in min_inv else min_inv
            min_sip = min_inv.split('/')[1] if '/' in min_inv else min_inv
            
            fund_record = {
                "fund_name": fund_name,
                "fund_category": category,
                "scheme_code": scheme_code,
                "nav": fund_data.get('nav', 'Not available'),
                "annual_return_since_inception": fund_data.get('inception_return', 'Not available'),
                "expense_ratio": info_dict.get('expense ratio', 'Not available'),
                "exit_load": info_dict.get('exit load', 'Not available'),
                "min_sip_amount": min_sip,
                "min_lumpsum": min_lumpsum,
                "risk": fund_data.get('risk_meter', {}).get('widget_properties', {}).get('zone_title', 'Not available'),
                "benchmark_index": info_dict.get('benchmark', 'Not available'),
                "lock_in_period": info_dict.get('lock in', 'None'),
                "source_url": source_url,
                "scrape_date": today_str
            }
            
            # If the exact fields above are None or different keys in Next.js, we provide fallbacks
            # We will use string representations since RAG just needs text context.
            
            funds_data.append(fund_record)
            
            # Update Metadata Store (Category to Funds mapping)
            cat_key = category.lower().replace(' ', '_')
            if cat_key not in metadata:
                metadata[cat_key] = []
            metadata[cat_key].append({
                "name": fund_name,
                "scheme_code": scheme_code
            })
            
            # Citations index is typically per-chunk, but we map fund -> citation initially
            citations[fund_name] = {
                "source_url": source_url,
                "scrape_date": today_str
            }
            
        except json.JSONDecodeError:
            print(f"Error parsing JSON in {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            
    # Save the processed data
    with open(FUNDS_DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(funds_data, f, indent=2)
    print(f"Saved {len(funds_data)} records to {FUNDS_DATA_PATH}")
    
    with open(FUND_METADATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)
    print(f"Saved metadata to {FUND_METADATA_PATH}")
    
    with open(CITATIONS_INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(citations, f, indent=2)
    print(f"Saved citations index to {CITATIONS_INDEX_PATH}")

if __name__ == "__main__":
    parse_html_files()
