
import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


load_dotenv()

app = FastAPI(title="Assistant AI API", version="0.3.0")

OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

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
    prompt = f"You are a helpful AI assistant.\n\nUser question: {payload.question}"

    body = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=body, timeout=60)
        response.raise_for_status()
        data = response.json()

        return {
            "question": payload.question,
            "answer": data.get("response", "")
        }

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Ollama connection error: {str(e)}")