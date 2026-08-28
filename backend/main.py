"""
Mutual Fund FAQ Assistant — FastAPI Application Entry Point.

A facts-only RAG-based assistant for Navi Mutual Fund schemes.
Provides factual, source-backed responses with no investment advice.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config import APP_HOST, APP_PORT
from backend.routes.chat import router as chat_router

# ─── App Initialization ──────────────────────────────────────────────────────

app = FastAPI(
    title="Mutual Fund FAQ Assistant",
    description=(
        "A facts-only FAQ assistant for Navi Mutual Fund schemes. "
        "Answers factual queries with source-backed responses. "
        "No investment advice."
    ),
    version="1.0.0",
)

# ─── CORS Middleware ──────────────────────────────────────────────────────────
# Allow frontend to communicate with the backend

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Route Registration ──────────────────────────────────────────────────────

app.include_router(chat_router, prefix="/api")


# ─── Health Check ─────────────────────────────────────────────────────────────

@app.get("/api/health", tags=["Health"])
async def health_check():
    """Health check endpoint for monitoring and uptime checks."""
    return {
        "status": "ok",
        "service": "Mutual Fund FAQ Assistant",
        "version": "1.0.0",
    }


# ─── Static Files (Frontend) ───────────────────────────────────────────────────

from fastapi.staticfiles import StaticFiles
import os

# Create frontend/dist dir if it doesn't exist
os.makedirs("frontend/dist", exist_ok=True)
app.mount("/", StaticFiles(directory="frontend/dist", html=True), name="frontend")


# ─── Run with Uvicorn ────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "backend.main:app",
        host=APP_HOST,
        port=APP_PORT,
        reload=True,
    )
