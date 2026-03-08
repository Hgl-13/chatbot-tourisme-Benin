import requests
import json

# Test de la route /api/chat
url = "http://localhost:8000/api/chat"
payload = {
    "message": "Bonjour ! Que peux-tu me dire sur le Benin ?"
}

print("🚀 Test de l'API /api/chat...")
print(f"Envoi de : {payload}")
print()

response = requests.post(url, json=payload)

print(f"Status code : {response.status_code}")
print(f"Réponse :")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))
