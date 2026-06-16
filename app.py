from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

class ClientMessage(BaseModel):
    message: str
    session_id: str 

class ChatResponse(BaseModel):
    reply: str
    session_id: str

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/chat/")
async def message_response(request: ClientMessage):
    session_id = request.session_id
    return {"reply": f"session id = {session_id}"}

app.mount("/static", StaticFiles(directory="static"), name="static")
