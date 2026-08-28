import json
import re
from pathlib import Path
from backend.config import PROCESSED_DATA_DIR

class CategoryDisambiguator:
    def __init__(self):
        self.metadata_path = PROCESSED_DATA_DIR / "fund_metadata.json"
        self.category_mapping = {}
        self.fund_names = []
        self._load_data()
        
    def _load_data(self):
        """Load fund metadata to initialize mappings."""
        if not self.metadata_path.exists():
            return
            
        with open(self.metadata_path, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
            
        # metadata is a dict: {"aggressive_allocation": [{"name": "Fund", "scheme_code": "123"}], ...}
        for category, funds in metadata.items():
            cat_norm = category.lower().strip().replace("_", " ")
            
            if cat_norm not in self.category_mapping:
                self.category_mapping[cat_norm] = []
                
            for fund in funds:
                fund_name = fund["name"]
                if fund_name not in self.fund_names:
                    self.fund_names.append(fund_name)
                if fund_name not in self.category_mapping[cat_norm]:
                    self.category_mapping[cat_norm].append(fund_name)
            
            # Also add some common aliases (e.g. if category is "Large Cap", add "largecap")
            aliases = [cat_norm.replace(" ", ""), cat_norm.replace("-", " ")]
            if "funds" in cat_norm:
                aliases.append(cat_norm.replace("funds", "fund").strip())
            
            for alias in set(aliases):
                if alias and alias != cat_norm:
                    if alias not in self.category_mapping:
                        self.category_mapping[alias] = []
                    for fund in funds:
                        if fund["name"] not in self.category_mapping[alias]:
                            self.category_mapping[alias].append(fund["name"])
                        
    def extract_fund_name(self, query: str) -> str | None:
        """
        Check if the query contains a specific fund name.
        Uses token overlap matching for MVP.
        """
        query_norm = query.lower()
        query_words = set(re.findall(r'\w+', query_norm))
        
        best_match = None
        best_score = 0
        
        sorted_funds = sorted(self.fund_names, key=len, reverse=True)
        
        for fund in sorted_funds:
            clean_fund = fund.lower()
            for word in ["direct plan growth", "direct growth", "index fund", "fund", "index"]:
                clean_fund = clean_fund.replace(word, "")
            clean_fund_str = re.sub(r'\s+', ' ', clean_fund).strip()
            
            # 1. Exact Substring Match
            if clean_fund_str and clean_fund_str in query_norm and len(clean_fund_str) > 5:
                return fund
                
            # 2. Token Overlap Match
            fund_words = set(re.findall(r'\w+', clean_fund_str))
            if not fund_words:
                continue
                
            overlap = fund_words.intersection(query_words)
            score = len(overlap) / len(fund_words)
            
            # Require at least 3 matching words and > 60% overlap
            if score > 0.6 and len(overlap) >= 3:
                if score > best_score:
                    best_score = score
                    best_match = fund
                    
        return best_match

    def detect_category(self, query: str) -> list[str]:
        """
        Check if the query matches a fund category, and return matching funds.
        """
        query_norm = query.lower()
        
        for cat_key, funds in self.category_mapping.items():
            # If the category name appears as a whole word in the query
            if re.search(r'\b' + re.escape(cat_key) + r'\b', query_norm):
                return funds
                
        generic_keywords = [
            'large cap', 'mid cap', 'small cap', 'multicap', 'flexi cap', 
            'nifty', 'sensex', 'tax saver', 'elss', 'hybrid', 'nasdaq', 'us equity'
        ]
        
        for kw in generic_keywords:
            if re.search(r'\b' + re.escape(kw) + r'\b', query_norm):
                matching_funds = [f for f in self.fund_names if all(w in f.lower().replace("&", "") for w in kw.split())]
                if matching_funds:
                    return matching_funds
                    
        return []
        
disambiguator = CategoryDisambiguator()
