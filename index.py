
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
from openai import AzureOpenAI

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ENDPOINT = "https://polite-ground-030dc3103.4.azurestaticapps.net/api/v1"
API_KEY = "c40f7f56-f79c-4b27-af2d-0d0c46bb1972"
API_VERSION = "2024-02-01"
MODEL_NAME = "gpt-35-turbo"

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
    
    return {"answer": completion.choices[0].message.content}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
