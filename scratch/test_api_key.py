import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(override=True)
api_key = os.getenv("GOOGLE_API_KEY")
print(f"Testing API key: {api_key[:5]}...{api_key[-5:]}")

try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=api_key,
    )
    response = llm.invoke("Hello, say hi!")
    print("Success! Response:", response.content)
except Exception as e:
    print("Error:", str(e))
