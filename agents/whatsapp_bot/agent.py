"""Section 1 : Bots WhatsApp / Telegram — automatisation client."""
from agents.base_agent import BaseAgent


class WhatsAppBotAgent(BaseAgent):
    name = "whatsapp_bot"
    section = "Bots WhatsApp / Telegram"
    KEYWORDS = [
        "bot", "robot", "automatisation", "automatiser", "whatsapp", "telegram",
        "message automatique", "reponse automatique", "chatbot", "faq automatique",
        "assistant virtuel", "agent ia", "prise de commande",
    ]
    FALLBACK = ("Je suis le spécialiste des bots WhatsApp/Telegram 🤖📱\n"
                "Dis-moi ce que tu veux automatiser et je te chifire ça en 2 minutes 😉")
    KNOWLEDGE = {
        "prix bot": "Ça dépend de ce que le bot doit faire 😊\nPacks bots : Starter 99€, Business 150€ (le plus vendu), Pro 300€.\nAbonnement agents IA : Découverte 490€/mois, Croissance 1200€/mois.\nTu veux le détail des packs ?",
        "combien coute un bot": "Packs bots : Starter 99€, Business 150€, Pro 300€ (one-shot).\nAgents IA : Découverte 490€/mois, Croissance 1200€/mois.\nQuel budget as-tu en tête ?",
        "je veux un bot whatsapp": ("Super projet 🔥 Un bot WhatsApp peut accueillir tes clients, "
            "présenter tes produits, prendre les commandes et relancer les paniers abandonnés 24h/24.\n"
            "Pack Business à 150€ = le plus vendu. On commence quand ?"),
        "bot telegram": "On fait aussi les bots Telegram 🇬🇳 Mêmes packs : 99€ / 150€ / 300€.\nTelegram c'est parfait pour vendre en canal privé. Tu l'utilises déjà ?",
        "comment ca marche": "3 étapes simples :\n1️⃣ Tu m'envoies tes produits/FAQ et ton ton\n2️⃣ Je construis et entraîne le bot (48-72h)\n3️⃣ Il répond à tes clients tout seul, 24h/24 🚀\nOn lance le tien ?",
        "comment payer": "Mobile Money (Orange, MTN), virement bancaire ou PayPal.\n50% à la commande, 50% à la livraison. C'est bon pour toi ?",
        "delai": "Le bot est prêt en 48 à 72h ⏱️ Et le tour est joué : il bosse pendant que tu dors 😄\nOn démarre aujourd'hui ?",
        "es tu un robot": "Loin de là 😄 Ici c'est l'équipe Komara Agency, de vraies personnes derrière chaque projet.\nTu veux automatiser quoi exactement ?",
    }


AGENT = WhatsAppBotAgent()
