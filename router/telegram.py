"""Canal Telegram : réception des updates + envoi des réponses."""
from __future__ import annotations

import logging
import os
import requests

log = logging.getLogger("komara-brain.telegram")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_WEBHOOK_SECRET = os.getenv("TELEGRAM_WEBHOOK_SECRET", "")
TG_API = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"


def is_configured() -> bool:
    return bool(TELEGRAM_BOT_TOKEN)


def extract_message(update: dict) -> tuple | None:
    """Retourne (chat_id, text, sender_name) ou None si pas exploitable."""
    msg = update.get("message") or update.get("edited_message") or {}
    text = msg.get("text") or (msg.get("caption") or "")
    chat_id = (msg.get("chat") or {}).get("id")
    if not chat_id or not text or not text.strip():
        return None
    name = ((msg.get("from") or {}).get("first_name") or "")[:60]
    return chat_id, text.strip(), name


def send_message(chat_id: int, text: str) -> bool:
    if not is_configured():
        log.warning("TELEGRAM_BOT_TOKEN manquant — réponse non envoyée")
        return False
    # Telegram limite à 4096 caractères par message
    for chunk in [text[i:i + 4000] for i in range(0, len(text), 4000)] or [""]:
        try:
            r = requests.post(
                f"{TG_API}/sendMessage",
                json={"chat_id": chat_id, "text": chunk},
                timeout=10,
            )
            if r.status_code != 200:
                log.error(f"Telegram sendMessage KO: {r.status_code} {r.text[:200]}")
                return False
        except requests.RequestException as exc:
            log.error(f"Telegram réseau: {exc}")
            return False
    return True


def set_webhook(base_url: str) -> dict:
    """Enregistre le webhook Telegram vers {base_url}/webhook/telegram."""
    if not is_configured():
        return {"ok": False, "error": "TELEGRAM_BOT_TOKEN manquant sur Railway"}
    url = f"{base_url.rstrip('/')}/webhook/telegram"
    payload: dict = {"url": url, "allowed_updates": ["message", "edited_message"]}
    if TELEGRAM_WEBHOOK_SECRET:
        payload["secret_token"] = TELEGRAM_WEBHOOK_SECRET
    r = requests.post(f"{TG_API}/setWebhook", json=payload, timeout=10)
    try:
        return {"ok": r.status_code == 200, "webhook_url": url, "detail": r.json()}
    except ValueError:
        return {"ok": False, "detail": r.text[:200]}
