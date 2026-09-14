"""Komara Brain Trial — Routeur intelligent + API FastAPI.

Un seul point d'entrée pour tous les canaux (WhatsApp, Telegram, API...).
Le routeur classifie le message et délègue au bon agent :
  - Section 1 : Bots WhatsApp / Telegram
  - Section 2 : Création digitale (logo, visuel, branding)
  - Section 3 : Dév web (site, app)
"""
from __future__ import annotations
import logging
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agents.whatsapp_bot.agent import AGENT as BOTS_AGENT
from agents.creation_digitale.agent import AGENT as DESIGN_AGENT
from agents.dev_web.agent import AGENT as WEB_AGENT

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
log = logging.getLogger("komara-brain")

app = FastAPI(
    title="Komara Brain Trial 🇬🇳",
    description="Routeur intelligent multi-agents : bots, création digitale, dév web.",
    version="1.0.0",
)

AGENTS = [BOTS_AGENT, DESIGN_AGENT, WEB_AGENT]
AGENT_BY_NAME = {a.name: a for a in AGENTS}


class IncomingMessage(BaseModel):
    sender: Optional[str] = None
    message: str
    context: Optional[dict] = None
    force_agent: Optional[str] = None  # bypass du routage si fourni


def route(message: str) -> tuple:
    """Retourne (agent, score). L'agent avec le meilleur score de mots-clés gagne."""
    scores = {a.name: a.match_score(message) for a in AGENTS}
    best_name = max(scores, key=scores.get)
    best_score = scores[best_name]
    if best_score == 0:
        return DESIGN_AGENT, 0  # agent par défaut (le plus fréquent)
    return AGENT_BY_NAME[best_name], best_score


@app.get("/health")
def health():
    return {"status": "ok", "brain": "komara-brain-trial", "agents": [a.name for a in AGENTS]}


GLOBAL_WELCOME = (
    "Bonjour 👋 Bienvenue chez Komara Agency 🇬🇳\n"
    "Je peux t'aider sur 3 domaines :\n"
    "🤖 Bots WhatsApp/Telegram (automatisation)\n"
    "🎨 Création digitale (logo, affiche, branding)\n"
    "💻 Développement web (site, boutique, app)\n"
    "Dis-moi ce que tu cherches 😊"
)
GLOBAL_THANKS = (
    "Avec grand plaisir 😊🇬🇳\n"
    "N'hésite pas si tu as d'autres questions. On est là pour toi !\n"
    "Et si tu veux avancer : le +212 701-986219 pour en discuter directement 😉"
)


@app.post("/webhook/{channel}")
def webhook(channel: str, msg: IncomingMessage):
    """Point d'entrée unique : /webhook/whatsapp, /webhook/telegram, /webhook/api..."""
    if channel not in ("whatsapp", "telegram", "api", "web", "test"):
        raise HTTPException(status_code=400, detail=f"Canal inconnu : {channel}")

    # Salutations et politesses : gérées globalement (cohérence entre agents)
    probe = AGENTS[0]
    if probe.is_greeting(msg.message) and not msg.force_agent:
        return {"channel": channel, "sender": msg.sender,
                "router": {"agent": "welcome", "score": 0},
                "agent": "welcome", "section": "accueil",
                "reply": GLOBAL_WELCOME, "handoff": False}
    if probe.is_thanks(msg.message) and not msg.force_agent:
        return {"channel": channel, "sender": msg.sender,
                "router": {"agent": "merci", "score": 0},
                "agent": "merci", "section": "politesse",
                "reply": GLOBAL_THANKS, "handoff": False}

    if msg.force_agent:
        agent = AGENT_BY_NAME.get(msg.force_agent)
        if not agent:
            raise HTTPException(status_code=400, detail=f"Agent inconnu : {msg.force_agent}")
        score = -1
    else:
        agent, score = route(msg.message)

    result = agent.respond(msg.message, msg.context)
    log.info(f"[{channel}] {msg.sender or '?'} → agent={agent.name} score={score} handoff={result['handoff']}")

    return {
        "channel": channel,
        "sender": msg.sender,
        "router": {"agent": agent.name, "score": score},
        **result,
    }


@app.post("/route")
def route_only(msg: IncomingMessage):
    """Diagnostic : voir comment le routeur classifie sans répondre."""
    agent, score = route(msg.message)
    return {"message": msg.message, "agent": agent.name, "section": agent.section, "score": score}
