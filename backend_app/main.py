from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Assistant AI API", version="0.2.0")

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def read_root():    
    return {"message": "Welcome to the Assistant AI API!"}

@app.get("/health")
def health():    
    return {"status": "OK"}

@app.post("/ask")
def ask_question(payload: QuestionRequest):
    return {
        "question": payload.question,
        "answer": f"This is a temporary answer for the question: {payload.question}"
    }