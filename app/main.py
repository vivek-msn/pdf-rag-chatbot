from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.chatbot import ask_question

app = FastAPI()

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