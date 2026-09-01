# Navi Mutual Fund FAQ Assistant

A facts-only, Retrieval-Augmented Generation (RAG) based chatbot designed to answer user queries regarding Navi Mutual Fund schemes. The assistant is strictly designed to provide factual, source-backed information without offering financial or investment advice.

## Tech Stack
* **Frontend:** React + Vite, TailwindCSS (for styling)
* **Backend:** FastAPI, Python
* **LLM / AI:** Google Generative AI (`gemini-3.5-flash-lite` for lightning-fast responses, `models/gemini-embedding-2` for embeddings), Langchain
* **Vector Store:** Chroma DB
* **Data Extraction/Ingestion:** Custom scraping & chunking pipeline

## Key Features
* **Facts-Only Responses:** The bot actively refuses to provide investment advice (e.g., "Should I buy?", "Is this a good fund?") and gracefully redirects users to educational resources.
* **Privacy Guard:** Automatically detects and blocks Personally Identifiable Information (PII) before it hits the LLM.
* **Intent Classification:** Smartly routes queries as factual, category-based (requiring disambiguation), or out-of-scope.
* **Lightning Fast:** Uses optimized `gemini-3.5-flash-lite` models for sub-second LLM inference times.
* **Citations:** Every factual answer includes a direct source URL indicating where the information was retrieved from.

## Getting Started

### Prerequisites
* Python 3.9+
* Node.js & npm
* A Google AI Studio API Key (`GOOGLE_API_KEY`)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vishalpurswaniiift1719-png/Mutual-fund-chatbot-Nextleap.git
   cd Mutual-fund-chatbot-Nextleap
   ```

2. **Setup the Backend:**
   ```bash
   # Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Setup environment variables
   cp .env.example .env
   # Edit .env and add your GOOGLE_API_KEY
   ```

3. **Data Ingestion (One-time setup):**
   Run the ingestion pipeline to scrape data, create embeddings, and populate Chroma DB.
   ```bash
   python -m ingestion.pipeline
   ```

4. **Setup the Frontend:**
   ```bash
   cd frontend
   npm install
   ```

### Running the Application Locally

1. **Start the Backend:**
   ```bash
   # From the root directory
   python -m backend.main
   ```
   The API will be available at `http://localhost:8000`.

2. **Start the Frontend (in a new terminal):**
   ```bash
   cd frontend
   npm run dev
   ```
   The frontend will be available at `http://localhost:5173`.

## Architecture Overview
For detailed information on how the system is architected, the prompt constraints, and the RAG pipeline flow, please refer to [Architecture.md](Architecture.md) and [implementation-plan.md](implementation-plan.md).

## License
MIT
