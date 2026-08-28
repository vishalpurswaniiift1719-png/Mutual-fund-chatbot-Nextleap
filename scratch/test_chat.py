import sys
# Fix encoding for Windows
sys.stdout.reconfigure(encoding='utf-8')

from backend.routes.chat import chat, ChatRequest
import asyncio

async def test():
    print("TEST 1: Factual Query (Navi Nifty 50 Index Fund)")
    req = ChatRequest(message="What is the expense ratio of the Navi Nifty 50 Index Fund?")
    resp = await chat(req)
    print(f"Type: {resp.type}")
    print(f"Message:\n{resp.message}")
    if resp.citation:
        print(f"Citation: {resp.citation}")
    print("-" * 50)

    print("TEST 2: Category Query (Large Cap)")
    req = ChatRequest(message="Tell me about large cap funds")
    resp = await chat(req)
    print(f"Type: {resp.type}")
    print(f"Message:\n{resp.message}")
    if resp.options:
        for opt in resp.options:
            print(f" - {opt.name}")
    print("-" * 50)
    
    print("TEST 3: Out of Scope (Advice)")
    req = ChatRequest(message="Should I invest in Navi Nifty 50?")
    resp = await chat(req)
    print(f"Type: {resp.type}")
    print(f"Message:\n{resp.message}")
    print("-" * 50)

if __name__ == "__main__":
    asyncio.run(test())
