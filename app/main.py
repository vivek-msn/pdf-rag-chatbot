from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from app.chatbot import ask_question

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/chat")
def serve_frontend():
    return FileResponse("frontend/index.html")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str = Field(..., min_length=1)

@app.get("/")
def home():
    return {"message": "RAG API is running"}

@app.post("/ask")
def ask(request: AskRequest):

    try:
        answer, metadatas = ask_question(
            request.question
        )

        return {
            "answer": answer,
            "sources": metadatas
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )