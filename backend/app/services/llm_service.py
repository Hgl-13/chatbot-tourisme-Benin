from groq import AsyncGroq
from app.config import settings

SYSTEM_PROMPT = """Tu es un guide touristique expert spécialisé sur les attraits touristiques du Bénin.

  Ta mission :
  - Aider les touristes à découvrir l'histoire, la culture et les sites du Bénin
  - Fournir des informations pratiques (activités, régions, prix indicatifs)
  - Être amical, précis, drôle et informatif
  - Répondre toujours en français

  Si tu ne connais pas une information précise, dis-le honnêtement et demande a l'utilisateur de reformuler sa question."""
  
class LLMService:
    def __init__(self):
        self.client = AsyncGroq(api_key=settings.groq_api_key)

    async def generate_response(self, prompt: str) -> str:
        """
        Génère une réponse à partir d'un prompt en utilisant Groq LLM.
        """
        try:
            response = await self.client.chat.completions.create(
                model=settings.llm_model,  # "mixtral-8x7b-32768"
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                temperature=settings.temperature,
                max_tokens=settings.max_tokens
            )
            return response.choices[0].message.content

        except Exception as e:
            print(f"Erreur lors de la génération de la réponse: {e}")
            return "Désolé, je n'ai pas pu générer une réponse pour le moment."


# Instance globale du service (singleton)
llm_service = LLMService()