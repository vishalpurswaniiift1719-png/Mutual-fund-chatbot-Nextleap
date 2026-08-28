import sys
from ingestion.scraper import get_fund_links, scrape_fund_pages
from ingestion.parser import parse_html_files
from ingestion.chunker import chunk_funds_data
from ingestion.embedder import embed_and_store_chunks
from ingestion.validate import validate_data
from backend.config import SCRAPE_SOURCE_URL

def run_pipeline():
    """Run the complete end-to-end data ingestion pipeline."""
    print("=========================================")
    print("🚀 Starting Data Ingestion Pipeline")
    print("=========================================\n")
    
    try:
        # Step 1: Scrape
        print("\n--- STEP 1: SCRAPING ---")
        fund_links = get_fund_links(SCRAPE_SOURCE_URL)
        if not fund_links:
            print("ERROR: No fund links found. Pipeline aborted.")
            return False
        scrape_fund_pages(fund_links)
        
        # Step 2: Parse
        print("\n--- STEP 2: PARSING ---")
        parse_html_files()
        
        # Step 3: Validate
        print("\n--- STEP 3: VALIDATING ---")
        if not validate_data():
            print("ERROR: Validation failed. Pipeline aborted.")
            return False
            
        # Step 4: Chunk
        print("\n--- STEP 4: CHUNKING ---")
        chunk_funds_data()
        
        # Step 5: Embed
        print("\n--- STEP 5: EMBEDDING ---")
        embed_and_store_chunks()
        
        print("\n=========================================")
        print("✅ Pipeline execution completed successfully!")
        print("=========================================\n")
        return True
        
    except Exception as e:
        print(f"\n❌ Pipeline failed: {e}")
        return False

if __name__ == "__main__":
    success = run_pipeline()
    sys.exit(0 if success else 1)
