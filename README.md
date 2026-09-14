# 🇬🇳 Komara Brain Trial

Cerveau multi-agents de Komara Agency — **un routeur intelligent, 3 sections métiers**.

## Architecture

```
komara-brain-trial/
├── router/
│   └── main.py            # Routeur + API FastAPI
└── agents/
    ├── base_agent.py      # Classe de base (routage, mini-cerveau, réponse)
    ├── whatsapp_bot/       # Section 1 : Bots WhatsApp / Telegram
    ├── creation_digitale/  # Section 2 : Logo, Visuel, Branding
    └── dev_web/            # Section 3 : Site Web, App
```

## Comment ça marche

1. Un message arrive sur `/webhook/{channel}` (whatsapp, telegram, api...)
2. Le **routeur** classe le message par mots-clés et choisit l'agent au meilleur score
3. L'**agent** répond depuis son mini-cerveau (prix, process, FAQ)
4. Si l'agent ne sait pas → `handoff: true` (escalade humaine)

## Démarrage rapide

```bash
# Local
pip install -r requirements.txt
uvicorn router.main:app --reload

# Docker
docker build -t komara-brain .
docker run -p 8000:8000 komara-brain
```

## Endpoints

| Méthode | Route | Description |
|---|---|---|
| GET  | `/health` | État du cerveau + agents |
| POST | `/webhook/{channel}` | Message entrant → réponse de l'agent |
| POST | `/route` | Diagnostic : quel agent gère ce message |

## Exemple

```bash
curl -X POST http://localhost:8000/webhook/whatsapp \
  -H "Content-Type: application/json" \
  -d '{"sender": "224700000000", "message": "combien coûte un bot whatsapp ?"}'
```

```json
{
  "channel": "whatsapp",
  "router": {"agent": "whatsapp_bot", "score": 3},
  "agent": "whatsapp_bot",
  "reply": "Packs bots : Starter 99€, Business 150€...",
  "handoff": false
}
```

## Ajouter un agent

1. Crée `agents/mon_agent/agent.py` héritant de `BaseAgent`
2. Définis `KEYWORDS` (routage) et `KNOWLEDGE` (réponses)
3. Enregistre-le dans `AGENTS` dans `router/main.py`

Ton toujours humain, jamais robotisé 😄
