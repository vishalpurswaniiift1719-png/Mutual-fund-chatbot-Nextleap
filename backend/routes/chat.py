"""
Chat route — handles user queries to the FAQ assistant.
"""

from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional, List
import uuid

router = APIRouter(tags=["Chat"])


# ─── Request / Response Models ────────────────────────────────────────────────

class ChatRequest(BaseModel):
    """Incoming chat message from the user."""
    message: str = Field(..., description="The user's query text")
    session_id: Optional[str] = Field(
        default=None,
        description="Session ID for conversation continuity",
    )
    selected_fund: Optional[str] = Field(
        default=None,
        description="Fund name selected during disambiguation",
    )


class FundOption(BaseModel):
    """A fund option shown during disambiguation."""
    name: str
    scheme_code: str


class ChatResponse(BaseModel):
    """Response from the FAQ assistant."""
    type: str = Field(
        ...,
        description="Response type: answer | disambiguation | refusal | privacy_warning",
    )
    message: str = Field(..., description="The response text")
    citation: Optional[str] = Field(
        default=None,
        description="Source citation URL (for 'answer' type)",
    )
    options: Optional[List[FundOption]] = Field(
        default=None,
        description="Fund options (for 'disambiguation' type)",
    )
    educational_link: Optional[str] = Field(
        default=None,
        description="Educational resource link (for 'refusal' type)",
    )
    footer: Optional[str] = Field(
        default=None,
        description="Last updated footer text",
    )
    session_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="Session ID for conversation continuity",
    )


# ─── Chat Endpoint ───────────────────────────────────────────────────────────

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Process a user query through the RAG pipeline.

    Flow:
    1. Privacy Guard → block PII queries
    2. Intent Classifier → route to appropriate handler
    3. Category Disambiguator → resolve ambiguous fund references
    4. Retrieval Engine → fetch relevant chunks from vector store
    5. Response Generator → generate LLM response
    6. Response Formatter → enforce constraints (3 sentences, citation, footer)
    """
    session_id = request.session_id or str(uuid.uuid4())
    query = request.message
    
    # 0. Privacy Guard
    from backend.services.privacy_guard import privacy_guard
    pii_check = privacy_guard.check_for_pii(query)
    if pii_check["has_pii"]:
        return ChatResponse(
            type="privacy_warning",
            message="I detected sensitive personal information (PII) in your message. For your security, please do not share personal details like emails, phone numbers, or IDs.",
            session_id=session_id
        )

    # 1. Intent Classification & Disambiguation
    from backend.services.classifier import classifier
    from backend.services.retriever import retriever
    from backend.services.generator import generator
    from backend.services.refusal_handler import refusal_handler

    classification = classifier.classify(query)
    
    # If the user previously selected a fund in disambiguation flow, we override
    if request.selected_fund:
        classification["intent"] = "factual"
        classification["fund_name"] = request.selected_fund
        
    intent = classification.get("intent")
    
    if intent == "out_of_scope":
        refusal_payload = refusal_handler.get_refusal_response()
        reason = classification.get("reason")
        
        if reason == "investment_advice":
            message = refusal_payload["message"]
        else:
            message = "I couldn't identify a specific Navi Mutual Fund in your query, or your question is unrelated to our supported schemes."
            
        return ChatResponse(
            type="refusal",
            message=message,
            educational_link=refusal_payload["educational_link"],
            session_id=session_id
        )
        
    elif intent == "category":
        funds = classification.get("matching_funds", [])
        
        if len(funds) == 1:
            # Bypass disambiguation if only one fund matches
            intent = "factual"
            classification["intent"] = "factual"
            classification["fund_name"] = funds[0]
        else:
            # Limit to top 5 funds
            top_funds = funds[:5]
            options = [FundOption(name=f, scheme_code="TBD") for f in top_funds]
            
            return ChatResponse(
                type="disambiguation",
                message=f"I found {len(top_funds)} funds matching that category. Which one would you like info on?",
                options=options,
                session_id=session_id
            )
            
    if intent == "factual":
        fund_name = classification.get("fund_name")
        if not fund_name:
             return ChatResponse(
                type="refusal",
                message="I couldn't identify a specific Navi Mutual Fund in your query.",
                session_id=session_id
             )
             
        # 2. Retrieval
        context = retriever.retrieve_by_fund(fund_name, query)
        if not context:
             return ChatResponse(
                type="answer",
                message=f"I don't have information on {fund_name} in my current dataset.",
                session_id=session_id
             )
             
        # 3. Generation
        try:
            answer = generator.generate_response(query, context)
        except Exception as e:
            print(f"Exception during LLM generation: {e}")
            error_msg = str(e).lower()
            if "429" in error_msg or "quota" in error_msg or "resource_exhausted" in error_msg:
                answer = "I'm sorry, but I am currently unavailable because the API rate limit (free tier quota) has been exceeded. Please try again later."
            else:
                answer = "I encountered an unexpected error while generating the response. Please try again."

        
        # 4. Formatter (Extract citation link from answer or context)
        import re
        citation = None
        
        # The prompt instructs the LLM to output "Source: <URL>" at the end.
        match_answer = re.search(r"Source:\s*(?:\[|<)?(https?://[^\s\*\]>]+)(?:\]|>)?", answer, re.IGNORECASE)
        if match_answer:
             citation = match_answer.group(1)
             # Remove it from the plain text answer
             answer = re.sub(r"Source:\s*(?:\[|<)?https?://[^\s\*\]>]+(?:\]|>)?", "", answer, flags=re.IGNORECASE).strip()
        else:
             # Just in case it output the literal placeholder
             answer = re.sub(r"Source:\s*<URL>", "", answer, flags=re.IGNORECASE).strip()
             # Fallback to extracting from context if LLM forgot
             match_context = re.search(r"Source URL:\s*(https?://[^\s]+)", context, re.IGNORECASE)
             if not match_context:
                  match_context = re.search(r"(https?://[^\s\n]+)", context)
             if match_context:
                  citation = match_context.group(1)
             
        return ChatResponse(
            type="answer",
            message=answer,
            citation=citation,
            session_id=session_id
        )


# ─── Funds List Endpoint ─────────────────────────────────────────────────────

@router.get("/funds")
async def list_funds():
    """
    Returns the full list of available Navi Mutual Fund schemes with categories.
    """
    # TODO: Phase 2 — Load from fund_metadata.json after scraping
    return {
        "amc": "Navi Mutual Fund",
        "funds": [],
        "message": "Fund data will be populated after the ingestion pipeline runs.",
    }
