"""
Centralized configuration for the Mutual Fund FAQ Assistant.
Loads environment variables from .env file and provides typed settings.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ─── Base Paths ───────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
VECTORSTORE_DIR = BASE_DIR / "vectorstore"
PROMPTS_DIR = BASE_DIR / "backend" / "prompts"

# ─── LLM Configuration ───────────────────────────────────────────────────────

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "google")  # openai | google | ollama
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# ─── Embedding Model ─────────────────────────────────────────────────────────

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL", "models/gemini-embedding-2"
)
EMBEDDING_DIMENSIONS = int(os.getenv("EMBEDDING_DIMENSIONS", "384"))

# ─── Vector Store ─────────────────────────────────────────────────────────────

CHROMA_PERSIST_DIR = os.getenv(
    "CHROMA_PERSIST_DIR", str(VECTORSTORE_DIR / "chroma_db")
)

# ─── Scraping ─────────────────────────────────────────────────────────────────

SCRAPE_SOURCE_URL = os.getenv(
    "SCRAPE_SOURCE_URL",
    "https://www.indmoney.com/mutual-funds/amc/navi-mutual-fund",
)

# ─── App Settings ─────────────────────────────────────────────────────────────

APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", "8000"))

# ─── RAG Settings ─────────────────────────────────────────────────────────────

RETRIEVAL_TOP_K = 5           # Number of chunks to retrieve from vector store
RERANK_TOP_N = 3              # Number of chunks after re-ranking
MAX_RESPONSE_SENTENCES = 3    # Maximum sentences in a response
CHUNK_SIZE = 400              # Target chunk size in tokens
CHUNK_OVERLAP = 50            # Overlap between chunks in tokens

# ─── Fund Metadata ───────────────────────────────────────────────────────────

FUND_METADATA_PATH = PROCESSED_DATA_DIR / "fund_metadata.json"
CITATIONS_INDEX_PATH = PROCESSED_DATA_DIR / "citations_index.json"
FUNDS_DATA_PATH = PROCESSED_DATA_DIR / "funds.json"
