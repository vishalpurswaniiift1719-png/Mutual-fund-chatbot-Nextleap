import json
import os
from pathlib import Path
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from backend.config import PROCESSED_DATA_DIR, VECTORSTORE_DIR, EMBEDDING_MODEL, GOOGLE_API_KEY, EMBEDDING_DIMENSIONS

def embed_and_store_chunks():
    """Embed chunks and store them in ChromaDB."""
    print("Starting vector embedding and storage...")
    
    chunks_path = PROCESSED_DATA_DIR / "chunks.json"
    if not os.path.exists(chunks_path):
        print(f"ERROR: {chunks_path} not found.")
        return
        
    with open(chunks_path, 'r', encoding='utf-8') as f:
        chunks = json.load(f)
        
    if not chunks:
        print("ERROR: No chunks to embed.")
        return
        
    print(f"Loading {len(chunks)} chunks into ChromaDB...")
    
    # Initialize Embedding Model
    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY,
        output_dimensionality=EMBEDDING_DIMENSIONS
    )
    
    # Prepare documents
    documents = []
    ids = []
    for chunk in chunks:
        doc = Document(
            page_content=chunk['text'],
            metadata=chunk['metadata']
        )
        documents.append(doc)
        ids.append(chunk['metadata']['chunk_id'])
        
    # Initialize ChromaDB
    # We use chunks metadata chunk_id as the ID for upsert
    vectorstore = Chroma(
        collection_name="navi_mutual_funds",
        embedding_function=embeddings,
        persist_directory=str(VECTORSTORE_DIR)
    )
    
    # Add to Chroma (this acts as an upsert if IDs are provided)
    vectorstore.add_documents(documents=documents, ids=ids)
    
    print(f"SUCCESS: Embedded and stored {len(documents)} documents in ChromaDB at {VECTORSTORE_DIR}")

if __name__ == "__main__":
    embed_and_store_chunks()
