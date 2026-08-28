import re
from backend.services.disambiguator import disambiguator

class IntentClassifier:
    def __init__(self):
        # We can expand this with an LLM call if keyword matching isn't enough, 
        # but for this highly scoped MVP, heuristics work exceptionally well.
        pass

    def classify(self, query: str) -> dict:
        """
        Classifies the user query into one of three intents:
        - 'factual': Asking a specific question about a specific fund
        - 'category': Asking about a category of funds, requiring disambiguation
        - 'out_of_scope': General chat, investment advice, or unrelated topics
        
        Returns:
            dict: {
                "intent": str,
                "fund_name": str | None,
                "matching_funds": list[str],
                "reason": str
            }
        """
        query_norm = query.lower()
        
        # 1. Check for explicit out-of-scope triggers (investment advice)
        advice_keywords = ['should i invest', 'recommend', 'best fund', 'good time to buy', 'buy or sell', 'portfolio advice', 'is it safe']
        if any(kw in query_norm for kw in advice_keywords):
            return {
                "intent": "out_of_scope",
                "fund_name": None,
                "matching_funds": [],
                "reason": "investment_advice"
            }
            
        # 2. Try to extract a specific fund name
        fund_name = disambiguator.extract_fund_name(query)
        if fund_name:
            return {
                "intent": "factual",
                "fund_name": fund_name,
                "matching_funds": [fund_name],
                "reason": "exact_fund_match"
            }
            
        # 3. Check for a category match
        category_funds = disambiguator.detect_category(query)
        if category_funds:
            # Return list of funds so the UI can ask the user to pick one
            return {
                "intent": "category",
                "fund_name": None,
                "matching_funds": category_funds,
                "reason": "category_match"
            }
            
        # 4. Fallback for completely unrelated queries
        return {
            "intent": "out_of_scope",
            "fund_name": None,
            "matching_funds": [],
            "reason": "unrelated_or_unrecognized"
        }

classifier = IntentClassifier()
