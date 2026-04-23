from fastapi import FastAPI

app = FastAPI(title="Assistant AI API", version="0.1.0")

@app.get("/")
def read_root():    
    return {"message": "Welcome to the Assistant AI API!"}

@app.get("/health")
def health():    
    return {"status": "OK"}