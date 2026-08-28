import json
import os
from backend.config import FUNDS_DATA_PATH, FUND_METADATA_PATH, CITATIONS_INDEX_PATH

def validate_data():
    """Verify extracted data completeness."""
    print("Validating Ingestion Pipeline Data...")
    
    # Check if files exist
    for path in [FUNDS_DATA_PATH, FUND_METADATA_PATH, CITATIONS_INDEX_PATH]:
        if not os.path.exists(path):
            print(f"ERROR: Missing file: {path}")
            return False
            
    with open(FUNDS_DATA_PATH, 'r', encoding='utf-8') as f:
        funds = json.load(f)
        
    if not funds:
        print("ERROR: funds.json is empty!")
        return False
        
    print(f"SUCCESS: Loaded {len(funds)} funds from funds.json")
    
    missing_critical = 0
    for fund in funds:
        if not fund.get('fund_name') or fund.get('fund_name') == 'Unknown Fund':
            print(f"WARNING: Fund missing name: {fund}")
            missing_critical += 1
            
        if not fund.get('source_url'):
            print(f"WARNING: Fund missing source URL: {fund['fund_name']}")
            missing_critical += 1
            
    if missing_critical > 0:
        print(f"ERROR: Validation failed: {missing_critical} critical fields missing.")
        return False
        
    with open(FUND_METADATA_PATH, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
        
    print(f"SUCCESS: Loaded {len(metadata.keys())} categories from metadata.json")
    
    with open(CITATIONS_INDEX_PATH, 'r', encoding='utf-8') as f:
        citations = json.load(f)
        
    print(f"SUCCESS: Loaded {len(citations.keys())} citations from citations_index.json")
    
    print("\nSUCCESS: All validation checks passed!")
    return True

if __name__ == "__main__":
    success = validate_data()
    exit(0 if success else 1)
