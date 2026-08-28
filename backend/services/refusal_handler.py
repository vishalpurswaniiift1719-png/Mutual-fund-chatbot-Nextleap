class RefusalHandler:
    def __init__(self):
        # Standard responses for out of scope queries
        self.standard_refusal = (
            "I am a factual assistant specifically for Navi Mutual Fund equity schemes. "
            "I cannot provide personalized investment advice, portfolio recommendations, "
            "or answer queries unrelated to Navi funds."
        )
        self.educational_link = "https://www.sebi.gov.in/sebiweb/other/OtherAction.do?doInvestor=yes"

    def get_refusal_response(self) -> dict:
        """
        Returns a standardized refusal payload.
        """
        return {
            "message": self.standard_refusal,
            "educational_link": self.educational_link
        }

refusal_handler = RefusalHandler()
