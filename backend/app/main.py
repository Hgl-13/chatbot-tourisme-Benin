"""
  Point d'entrée de l'application FastAPI
  """
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routes.chat import router as chat_router

# Création de l'instance FastAPI
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API de chatbot pour guider les touristes au Bénin",
    debug=settings.debug
)

# Configuration CORS - Autorise le frontend à communiquer avec l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],  # URL du frontend (React)
    allow_credentials=True,
    allow_methods=["*"],  # Autorise GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Autorise tous les headers HTTP
)

# Enregistrement des routers
app.include_router(chat_router)


# Route de santé - Pour vérifier que l'API fonctionne
@app.get("/health")
async def health_check():
    """
    Endpoint de santé pour vérifier que l'API est en ligne
    """
    return {
        "status": "healthy",
        "app_name": settings.app_name,
        "version": settings.app_version
    }


# Route racine - Page d'accueil de l'API
@app.get("/")
async def root():
    """
    Point d'entrée principal de l'API
    """
    return {
        "message": "Bienvenue sur l'API du Chatbot Tourisme Bénin",
        "docs": "/docs",  # Documentation Swagger
        "health": "/health"
    }


# Point d'entrée pour lancer le serveur directement
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",  # Chemin vers l'app FastAPI
        host="0.0.0.0",  # Écoute sur toutes les interfaces réseau
        port=settings.port,
        reload=settings.debug  # Auto-reload en mode développement
    )
