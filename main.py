from fastapi import FastAPI
from pydantic import BaseModel

from services.ai_service import ai_chat

app = FastAPI()


# =========================
# REQUEST MODEL
# =========================

class ChatRequest(BaseModel):

    user_id: str

    message: str


# =========================
# HOME ROUTE
# =========================

@app.get("/")
def home():

    return {
        "message": "AI E-Commerce Assistant Running"
    }


# =========================
# CHAT ROUTE
# =========================

@app.post("/chat")
def chat(request: ChatRequest):
    
    reply = ai_chat(
        request.user_id,
        request.message
    )

    # reply = ai_chat(request.message)

    return {
        # "info":"raw data",
        "user_id": request.user_id,
        # "reply": reply
        "reply": ai_chat(
            request.user_id,
            request.message
            )
        
    }

# @app.get("/")
# def home():
#     return {"message": "AI Review Summarizer API Running"}

# @app.post("/Testing")
# def chat(data: dict):

#     # user_id = data.get("user_id")

#     message = data.get("message")

#     result = testing(message)

#     return {
#         "reply": result
#     }

