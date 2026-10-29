from fastapi import FastAPI
import os
import openai
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str


app = FastAPI()
client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)

messages=[]

@app.get("/")
def test_get():
    return {
        "status": "success"
    }

@app.post("/chat")
def llm_chat(req: ChatRequest):
    print("messages -> ", messages)
    master_prompt = f"""
    previous chat context: {messages}
    current user prompt: {req.message}
    """
    response = client.responses.create(
        model="openai/gpt-oss-120b",
        input=master_prompt
    )
    messages.append(
        {
            "user": req.message,
            "llm_response": response.output_text
        }
    )
    return {
        "llm_output": response.output_text
    }

    