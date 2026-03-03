"""
Configuration de l'application - Gestion des variables d'environnement
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """
    Classe de configuration utilisant Pydantic.
    Les valeurs sont automatiquement chargées depuis le fichier .env
    """

    # API Configuration
    app_name: str = "Chatbot Tourisme Bénin"
    app_version: str = "1.0.0"
    debug: bool = True
    port: int = 8000

    # CORS
    frontend_url: str = "http://localhost:5173"

    # LLM Provider
    groq_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    llm_provider: str = "groq"  # "groq" or "openai"
    llm_model: str = "mixtral-8x7b-32768"

    # Embeddings
    embedding_provider: str = "sentence-transformers"
    embedding_model: str = "paraphrase-multilingual-MiniLM-L12-v2"

    # ChromaDB
    chroma_persist_directory: str = "./app/data/processed/chroma_db"
    collection_name: str = "benin_tourism_knowledge"

    # RAG Configuration
    chunk_size: int = 1000
    chunk_overlap: int = 200
    top_k_results: int = 5
    temperature: float = 0.7
    max_tokens: int = 1000

    # Scraping
    scraping_delay: float = 1.0
    user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Instance globale de configuration
settings = Settings()
