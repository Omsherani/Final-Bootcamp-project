from fastapi import FastAPI
from backend.agent import agent

app = FastAPI()

@app.get("/")
def root():
    return {"message": "RAG Agent is running!"}

@app.get("/ask")
def ask(query: str):
    response = agent.run(query)
    return {"response": response}

