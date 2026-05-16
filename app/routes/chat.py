from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.services.conversation_manager import handle_conversation

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):

    return handle_conversation(request.messages)