

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ENDPOINT = os.getenv("ENDPOINT")
API_KEY = os.getenv("API_KEY")
API_VERSION = os.getenv("API_VERSION")
MODEL_NAME = os.getenv("MODEL_NAME")

client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query.question},
    ]
    
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
    )
    
    return {"answer": completion.choices[0].message['content']}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
