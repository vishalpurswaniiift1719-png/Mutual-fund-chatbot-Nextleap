import json
import os
from backend.config import FUNDS_DATA_PATH, PROCESSED_DATA_DIR

def chunk_funds_data():
    """Convert structured fund data into semantic text chunks."""
    print("Starting chunking process...")
    
    if not os.path.exists(FUNDS_DATA_PATH):
        print(f"ERROR: {FUNDS_DATA_PATH} not found.")
        return
        
    with open(FUNDS_DATA_PATH, 'r', encoding='utf-8') as f:
        funds = json.load(f)
        
    chunks = []
    
    for fund in funds:
        # Create a single cohesive text block for the fund
        text_content = (
            f"Fund Name: {fund['fund_name']}\n"
            f"Category: {fund['fund_category']}\n"
            f"Expense Ratio: {fund.get('expense_ratio', 'Not available')}\n"
            f"Exit Load: {fund.get('exit_load', 'Not available')}\n"
            f"NAV: {fund.get('nav', 'Not available')}\n"
            f"Annual Return Since Inception: {fund.get('annual_return_since_inception', 'Not available')}\n"
            f"Minimum SIP Amount: {fund.get('min_sip_amount', 'Not available')}\n"
            f"Minimum Lumpsum Amount: {fund.get('min_lumpsum', 'Not available')}\n"
            f"Risk Level: {fund.get('risk', 'Not available')}\n"
            f"Benchmark Index: {fund.get('benchmark_index', 'Not available')}\n"
            f"Lock-in Period: {fund.get('lock_in_period', 'None')}"
        )
        
        # Create metadata payload
        slug = fund['source_url'].rstrip('/').split('/')[-1]
        metadata = {
            "chunk_id": f"{slug}_full",
            "fund_name": fund['fund_name'],
            "fund_category": fund['fund_category'],
            "scheme_code": fund['scheme_code'],
            "source_url": fund['source_url'],
            "scrape_date": fund['scrape_date']
        }
        
        chunks.append({
            "text": text_content,
            "metadata": metadata
        })
        
    chunks_path = PROCESSED_DATA_DIR / "chunks.json"
    with open(chunks_path, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, indent=2)
        
    print(f"SUCCESS: Generated {len(chunks)} chunks and saved to {chunks_path}")

if __name__ == "__main__":
    chunk_funds_data()
