import os
import time
import hashlib
import requests
from bs4 import BeautifulSoup
from backend.config import RAW_DATA_DIR, SCRAPE_SOURCE_URL

# Indmoney requires headers to avoid bot blocking
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}

def get_fund_links(amc_url: str) -> list:
    """Fetch all Navi mutual fund scheme links from the AMC page."""
    print(f"Fetching AMC page: {amc_url}")
    response = requests.get(amc_url, headers=HEADERS)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = set()
    
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        # Filter for Navi fund pages (excluding category/learn pages)
        if '/mutual-funds/navi-' in href and '-growth' in href:
            if not href.startswith('http'):
                href = f"https://www.indmoney.com{href}"
            links.add(href)
            
    return list(links)

def scrape_fund_pages(links: list):
    """Scrape each fund page and save raw HTML."""
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    
    print(f"Found {len(links)} fund links. Starting scrape...")
    
    for url in links:
        slug = url.rstrip('/').split('/')[-1]
        filepath = RAW_DATA_DIR / f"{slug}.html"
        
        print(f"Scraping {slug}...")
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            
            # Simple content hashing to avoid re-writing identical files
            new_content = response.text
            new_hash = hashlib.sha256(new_content.encode('utf-8')).hexdigest()
            
            if filepath.exists():
                with open(filepath, 'r', encoding='utf-8') as f:
                    old_content = f.read()
                old_hash = hashlib.sha256(old_content.encode('utf-8')).hexdigest()
                
                if old_hash == new_hash:
                    print(f"  -> Skipping {slug}, no changes.")
                    continue
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"  -> Saved {slug}.html")
            
            # Be polite to the server
            time.sleep(2)
            
        except Exception as e:
            print(f"Error scraping {url}: {e}")

if __name__ == "__main__":
    try:
        fund_links = get_fund_links(SCRAPE_SOURCE_URL)
        if not fund_links:
            print("No fund links found. Check if the AMC page structure changed.")
        else:
            scrape_fund_pages(fund_links)
    except Exception as e:
        print(f"Failed to fetch AMC page: {e}")
