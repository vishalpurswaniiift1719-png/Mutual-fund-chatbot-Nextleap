from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from backend.config import VECTORSTORE_DIR, EMBEDDING_MODEL, GOOGLE_API_KEY, EMBEDDING_DIMENSIONS

class Retriever:
    def __init__(self):
        # We must use the same embedding function that was used during ingestion
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model=EMBEDDING_MODEL,
            google_api_key=GOOGLE_API_KEY,
            output_dimensionality=EMBEDDING_DIMENSIONS
        )
        
        self.vectorstore = Chroma(
            collection_name="navi_mutual_funds",
            embedding_function=self.embeddings,
            persist_directory=str(VECTORSTORE_DIR)
        )

    def retrieve_by_fund(self, fund_name: str, query: str) -> str:
        """
        Since we use a metadata-driven retrieval strategy (1 chunk per fund),
        we enforce a hard filter on the fund name.
        """
        # Because we only have 1 chunk per fund, a basic similarity search with 
        # k=1 and a strict metadata filter is guaranteed to return the exact chunk.
        results = self.vectorstore.similarity_search(
            query=query,
            k=1,
            filter={"fund_name": fund_name}
        )
        
        if results:
            doc = results[0]
            source_url = doc.metadata.get("source_url", "N/A")
            return f"{doc.page_content}\nSource URL: {source_url}"
        return ""

retriever = Retriever()
