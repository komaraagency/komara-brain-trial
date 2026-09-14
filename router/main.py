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
from fastapi.responses import HTMLResponse
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


def detect_global_intent(message: str) -> str | None:
    """Intention cross-domaine quand aucun agent ne matche : rdv, objection, sinon None."""
    probe = AGENTS[0]
    t = probe.normalize(message)
    if any(p in t for p in RDV_PATTERNS):
        return "rdv"
    if any(p in t for p in OBJECTION_PATTERNS):
        return "objection"
    return None


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

# Intentions cross-domaine (sans mot-clé métier) : réponses neutres
GLOBAL_RDV = (
    "Avec plaisir 📅 On peut se parler :\n"
    "☀️ 10h-13h ou 🌆 16h-19h (heure Guinée)\n"
    "Donne-moi un créneau et je confirme. Ou appelle le +212 701-986219 😉"
)
GLOBAL_OBJECTION = (
    "Je comprends 😊 Pour te répondre au juste, c'est pour quel projet :\n"
    "🤖 un bot WhatsApp/Telegram, 🎨 un visuel (logo, affiche), ou 💻 un site ?\n"
    "Dans tous les cas : paiement possible en 2 fois (50/50), et satisfaction garantie 🤝"
)
RDV_PATTERNS = ["rdv", "rendez vous", "rendez-vous", "appel", "dispo", "recontacte", "rappel"]
OBJECTION_PATTERNS = ["cher", "reflechi", "hesite", "arnaque", "rembourse",
                      "budget", "pas sur", "pas convince", "doute"]


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
        # intention cross-domaine (rdv, objection) quand aucun domaine ne matche
        if score == 0:
            g = detect_global_intent(msg.message)
            if g == "rdv":
                return {"channel": channel, "sender": msg.sender,
                        "router": {"agent": "rdv_global", "score": 0},
                        "agent": "rdv_global", "section": "prise de rdv",
                        "reply": GLOBAL_RDV, "handoff": False}
            if g == "objection":
                return {"channel": channel, "sender": msg.sender,
                        "router": {"agent": "objection_global", "score": 0},
                        "agent": "objection_global", "section": "objection",
                        "reply": GLOBAL_OBJECTION, "handoff": False}

    result = agent.respond(msg.message, msg.context)
    log.info(f"[{channel}] {msg.sender or '?'} → agent={agent.name} score={score} handoff={result['handoff']}")

    return {
        "channel": channel,
        "sender": msg.sender,
        "router": {"agent": agent.name, "score": score},
        **result,
    }


CHAT_HTML = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Komara Brain — Test</title>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  body { font-family: system-ui, sans-serif; background:#0b141a; color:#e9edef;
         height:100vh; display:flex; flex-direction:column; }
  header { background:#1f2c33; padding:14px 16px; display:flex; align-items:center; gap:10px; }
  .logo { width:38px; height:38px; background:linear-gradient(135deg,#ce1126,#fcd116,#009460);
          border-radius:50%; display:flex; align-items:center; justify-content:center;
          font-weight:bold; font-size:18px; color:#fff; }
  header h1 { font-size:16px; } header p { font-size:12px; color:#8696a0; }
  #chat { flex:1; overflow-y:auto; padding:16px; display:flex; flex-direction:column; gap:10px; }
  .msg { max-width:80%; padding:10px 14px; border-radius:12px; font-size:15px;
         line-height:1.45; white-space:pre-wrap; }
  .bot { background:#1f2c33; align-self:flex-start; border-top-left-radius:2px; }
  .me  { background:#005c4b; align-self:flex-end; border-top-right-radius:2px; }
  .tag { font-size:11px; color:#66b2a2; margin-bottom:4px; font-weight:600; }
  form { display:flex; gap:8px; padding:12px; background:#1f2c33; }
  input { flex:1; background:#2a3942; border:none; border-radius:22px; padding:12px 16px;
          color:#e9edef; font-size:15px; outline:none; }
  button { background:#00a884; color:#fff; border:none; border-radius:22px;
           padding:12px 20px; font-size:15px; font-weight:600; cursor:pointer; }
</style>
</head>
<body>
<header>
  <div class="logo">K</div>
  <div><h1>Komara Brain 🇬🇳</h1><p id="status">Test en direct — 3 agents + routeur</p></div>
</header>
<div id="chat"></div>
<form onsubmit="return send(event)">
  <input id="input" placeholder="Écris ton message..." autocomplete="off">
  <button>➤</button>
</form>
<script>
const chat = document.getElementById("chat");
function add(text, who, tag) {
  const d = document.createElement("div");
  d.className = "msg " + who;
  if (tag) { const t = document.createElement("div"); t.className="tag";
             t.textContent = tag; d.appendChild(t); }
  d.appendChild(document.createTextNode(text));
  chat.appendChild(d); chat.scrollTop = chat.scrollHeight;
}
async function send(e) {
  e.preventDefault();
  const input = document.getElementById("input");
  const text = input.value.trim(); if (!text) return false;
  input.value = ""; add(text, "me");
  try {
    const r = await fetch("/webhook/test", {
      method: "POST", headers: {"Content-Type":"application/json"},
      body: JSON.stringify({message: text, sender: "web_test"})
    });
    const d = await r.json();
    add(d.reply, "bot", "🤖 " + d.agent + (d.handoff ? " (handoff)" : ""));
  } catch (err) { add("Erreur de connexion 😅", "bot"); }
  return false;
}
add("Salut 👋 Je suis le cerveau Komara Agency en mode test.\nEssaie : \"combien coûte un bot ?\", \"je veux un logo\", \"c'est cher\" ou \"rdv\" 😊", "bot");
</script>
</body>
</html>"""


@app.get("/chat", response_class=HTMLResponse)
def chat():
    """Page de test : discuter avec le cerveau depuis un navigateur."""
    return CHAT_HTML


@app.post("/route")
def route_only(msg: IncomingMessage):
    """Diagnostic : voir comment le routeur classifie sans répondre."""
    agent, score = route(msg.message)
    return {"message": msg.message, "agent": agent.name, "section": agent.section, "score": score}
