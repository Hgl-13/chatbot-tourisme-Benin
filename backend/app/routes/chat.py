"""
Route /chat - Endpoint principal du chatbot
"""
from fastapi import APIRouter
from app.models import ChatRequest, ChatResponse
from app.services import llm_service

# Créer le router avec préfixe /api et tag pour la doc
router = APIRouter(
    prefix="/api",
    tags=["chat"]
)


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest) -> ChatResponse:
    """
    Endpoint principal du chatbot.

    Reçoit un message utilisateur et retourne une réponse générée par le LLM.

    Args:
        request: ChatRequest contenant le message et l'historique optionnel

    Returns:
        ChatResponse avec la réponse du LLM et les sources (None pour l'instant)
    """
    # Appeler le service LLM pour générer la réponse
    response_text = await llm_service.generate_response(request.message)

    # Construire et retourner la réponse
    return ChatResponse(
        response=response_text,
        source=None  # Pas de RAG pour l'instant, on ajoutera les sources plus tard
    )
