from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from app.chatbot import ask_question

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/chat")
def serve_frontend():
    return FileResponse("frontend/index.html")

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