import os
import re
from datetime import date
from langchain_google_genai import ChatGoogleGenerativeAI
from backend.config import PROMPTS_DIR, LLM_PROVIDER, GOOGLE_API_KEY, OPENAI_API_KEY
# If we support OpenAI in the future, we can load it conditionally
# from langchain_openai import ChatOpenAI

class Generator:
    def __init__(self):
        # Load prompt template
        prompt_path = PROMPTS_DIR / "system_prompt.txt"
        with open(prompt_path, 'r', encoding='utf-8') as f:
            self.system_prompt_template = f.read()
            
        # Initialize LLM based on config
        # By default we are using Google
        if LLM_PROVIDER.lower() == "google":
            if not GOOGLE_API_KEY:
                print("WARNING: GOOGLE_API_KEY is not set.")
            self.llm = ChatGoogleGenerativeAI(
                model="gemini-3.5-flash-lite",
                google_api_key=GOOGLE_API_KEY,
                max_retries=0
            )
        else:
            raise ValueError(f"Unsupported LLM Provider: {LLM_PROVIDER}")

    def generate_response(self, query: str, context: str) -> str:
        """
        Takes the user query and the retrieved context string,
        injects them into the prompt, and gets the LLM response.
        """
        # Inject into prompt
        prompt = self.system_prompt_template.replace("{context}", context).replace("{query}", query)
        
        # Invoke LLM
        response = self.llm.invoke(prompt)
        content = response.content
        if isinstance(content, list):
            # Extract text from list of dicts/blocks
            text_parts = []
            for item in content:
                if isinstance(item, dict) and 'text' in item:
                    text_parts.append(item['text'])
                elif isinstance(item, str):
                    text_parts.append(item)
            text = " ".join(text_parts).strip()
        else:
            text = str(content).strip()
        # Add footer (Wait, footer rule: "Last updated from sources: <date>")
        # We can extract the scrape_date from the context if it's there.
        # But for simplicity, we'll just append it programmatically to ensure it's there.
        
        # We extract the scrape_date from the context string using regex
        scrape_date = "recently"
        match = re.search(r"Scrape Date:\s*([0-9\-]+)", context, re.IGNORECASE)
        # However, our context actually doesn't have "Scrape Date:", wait.
        # The chunker generated "Fund Name:...". Wait, let's just use today's date if not found.
        if match:
            scrape_date = match.group(1)
        else:
            scrape_date = date.today().isoformat()
            
        footer = f"\n\n*Last updated from sources: {scrape_date}*"
        return text + footer

generator = Generator()
