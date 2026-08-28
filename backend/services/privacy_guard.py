import re

class PrivacyGuard:
    def __init__(self):
        # Basic regex patterns for identifying PII
        self.pii_patterns = {
            "email": re.compile(r"[\w\.-]+@[\w\.-]+\.\w+"),
            "phone_number": re.compile(r"\b\d{10}\b|\b\d{3}[-\.\s]\d{3}[-\.\s]\d{4}\b|\+\d{1,3}[-\.\s]\d{10}\b"),
            "pan_card": re.compile(r"[A-Z]{5}[0-9]{4}[A-Z]{1}"),
            "aadhaar": re.compile(r"\b\d{4}\s\d{4}\s\d{4}\b|\b\d{12}\b")
        }

    def check_for_pii(self, text: str) -> dict:
        """
        Scans text for PII. 
        Returns {"has_pii": True, "type": <type>} if found, else {"has_pii": False}
        """
        for pii_type, pattern in self.pii_patterns.items():
            if pattern.search(text):
                return {"has_pii": True, "type": pii_type}
                
        return {"has_pii": False}

privacy_guard = PrivacyGuard()
