"""Section 1 : Bots WhatsApp / Telegram — automatisation client.

Connaissance organisée en 6 axes :
  ACCUEIL · VENTE · PRISE DE RDV · CONSEIL · OBJECTION · CLOSING
"""
from agents.base_agent import BaseAgent


class WhatsAppBotAgent(BaseAgent):
    name = "whatsapp_bot"
    section = "Bots WhatsApp / Telegram"
    KEYWORDS = [
        "bot", "robot", "automatisation", "automatiser", "whatsapp", "telegram",
        "message automatique", "reponse automatique", "chatbot", "faq automatique",
        "assistant virtuel", "agent ia", "prise de commande", "relance",
    ]
    FALLBACK = ("Je suis le spécialiste des bots WhatsApp/Telegram 🤖📱\n"
                "Dis-moi ce que tu veux automatiser et je te chifre ça en 2 minutes 😉")

    KNOWLEDGE = {
        # ---------------- ACCUEIL ----------------
        "bonjour": "Bonjour 👋 Bienvenue chez Komara Agency 🇬🇳\nTu veux automatiser tes messages WhatsApp ? Tu es au bon endroit.\nDis-moi ton besoin et on regarde ça ensemble 😊",
        "salut": "Salut à toi 👋 L'équipe Komara Agency à ton service.\nTu as un projet de bot WhatsApp ou Telegram en tête ?",
        "bonsoir": "Bonsoir 👋 Content de te lire à cette heure-ci 😄\nParle-moi de ton projet d'automatisation, je note tout.",
        "ca va": "Ça va super bien, merci 😊 Et toi ?\nPendant qu'on y est : ton business, il galère à répondre à tous les messages ?",
        "qui etes vous": "Komara Agency 🇬🇳 — on crée des bots WhatsApp/Telegram qui vendent pendant que tu dors.\nPacks à partir de 99€ une seule fois. Tu automatises quoi actuellement ?",
        # ---------------- VENTE ----------------
        "prix bot": "Ça dépend de ce que le bot doit faire 😊\nPacks bots : Starter 99€, Business 150€ (le plus vendu), Pro 300€.\nAbonnement agents IA : Découverte 490€/mois, Croissance 1200€/mois.\nTu veux le détail des packs ?",
        "combien coute un bot": "Packs bots : Starter 99€, Business 150€, Pro 300€ (one-shot, pas d'abonnement) 💼\nAgents IA en abonnement : Découverte 490€/mois, Croissance 1200€/mois.\nQuel budget as-tu en tête ?",
        "je veux un bot whatsapp": "Super projet 🔥 Un bot WhatsApp accueille tes clients, présente tes produits, prend les commandes et relance les paniers 24h/24.\nPack Business à 150€ = le plus vendu. On commence quand ?",
        "bot telegram": "On fait aussi les bots Telegram 🇬🇳 Mêmes packs : 99€ / 150€ / 300€.\nTelegram c'est parfait pour vendre en canal privé. Tu l'utilises déjà ?",
        "c'est quoi un agent ia": "L'agent IA c'est le niveau au-dessus du bot 🚀\nIl répond ET il vend : qualification des clients, relance des paniers, prise de RDV, suivi.\nDécouverte 490€/mois, Croissance 1200€/mois, POC 2500€. Je t'explique ?",
        "difference entre les packs": "Simple :\n Starter 99€ = 1 canal, questions/réponses\n Business 150€ = commandes + FAQ + relance (le plus vendu 🔥)\n Pro 300€ = multi-canaux + CRM + stats\nTu vois lequel te va ?",
        "que contient le pack": "Chaque pack inclut : création du bot, entraînement sur TES réponses, tests, et la mise en ligne 🛠️\nLe Pro ajoute le CRM et les statistiques de vente.\nTu veux qu'on détaille le Business ?",
        # ---------------- PRISE DE RDV ----------------
        "rdv": "Avec plaisir 📅 On peut se parler aujourd'hui ou demain :\n ☀️ 10h-13h ou 🌆 16h-19h (heure Guinée).\nDonne-moi un créneau et je te confirme. Ou appelle directement le +212 701-986219 😉",
        "appel": "Ok pour un appel 📞 Dis-moi juste : matin ou après-midi ?\nJe te rappelle au +212 701-986219. Ça dure 5-10 minutes, promis 😄",
        "tu es dispo": "Toujours dispo pour parler business 😄 Aujourd'hui 16h-19h ou demain 10h-13h : tu préfères quoi ?",
        # ---------------- CONSEIL ----------------
        "quel bot pour mon business": "Bonne question 👏 Dis-moi :\n1️⃣ Tu vends quoi ?\n2️⃣ Combien de messages/jour reçois-tu ?\n3️⃣ Tu veux juste répondre ou aussi vendre ?\nAvec ça je te dis le pack parfait direct 😊",
        "est ce que ca marche pour mon business": "Si tes clients t'écrivent, oui 💯 Restos, boutiques, coachs, immobilier, écoles : partout où il y a des messages, un bot fait gagner du temps ET des ventes.\nC'est quoi ton activité ?",
        "peu de messages": "C'est justement là qu'il faut commencer 💪\n10 messages/jour bien traités = 10 ventes. Le bot transforme chaque message en occasion de vendre.\nEt quand tu grandiras, il suivra 😊",
        "conseil": "Mon conseil honnête : commence avec le Business 150€ 💼\nIl couvre 90% des besoins (commandes + FAQ + relance).\nSi ça déborde, on upgrade vers le Pro. Jamais l'inverse 😉",
        # ---------------- OBJECTION ----------------
        "c'est cher": "Je comprends 😊 Mais calcule : un commercial à plein temps, c'est 200€+/mois, tous les mois.\nLe bot : 150€ une seule fois, il travaille 24h/24 pendant 1 an. Rentabilisé en 2-3 ventes.\nTu veux qu'on calcule pour TON cas ?",
        "pas le temps": "Normal chef 😂 C'est justement pour ça que le bot existe.\nDe mon côté ça prend 48-72h, et de ton côté : juste m'envoyer tes produits et tes réponses type. 30 minutes max.\nOn cale ça ce week-end ?",
        "je vais reflechir": "Pas de souci, réfléchir c'est sain 👌 Mais une question rapide :\nC'est le prix qui te retient, ou tu doutes que ça marche pour toi ?\nSelon ta réponse je peux te rassurer tout de suite 😊",
        "arnaque": "Je comprends la méfiance, il y a des filous partout 🙏 Chez nous : 50% avant / 50% après livraison, facture, support 1 mois, et témoignages clients.\nZéro risque. Tu veux voir les témoignages ?",
        "fiverr": "Oui, il y en a à 30€ sur Fiverr 😅 Ce sont des bots génériques qui copient-collent des réponses.\nLe nôtre est entraîné sur TON business, TON ton, TES produits. Qualité vs prix, tu vois ?",
        "mon neveu peut le faire": "Super si ton neveu maîtrise 😊 Mais qui fait le support à 2h du mat quand ça bug ? Chez nous : 1 mois de support inclus.\nTu payes la tranquillité, pas juste le code.",
        "client robot": "Non 😎 On lui donne TA voix : il dit « Bonjour, l'assistant de [ton business] ».\n90% des clients préfèrent une réponse en 2 secondes qu'une attente de 2 heures. C'est tout ce qu'ils retiendront.",
        "je fais moi meme": "Tu peux, franchement 👏 Mais ça te prendra des semaines d'apprentissage.\nMoi je te livre en 72h, entraîné et testé. Ton temps vaut plus que 150€, non ? 😉",
        "pas sur que ca marche": "Teste 7 jours 🤝 Si le bot ne te sert pas, je te le modifie gratuitement ou je te rembourse.\nTu ne risques rien du tout.",
        "je demande a mon associe": "Excellente démarche 👌 Je t'envoie un récap PDF + la démo vidéo pour lui montrer.\nJe vous rappelle vendredi pour votre réponse ?",
        "remboursement": "Simple et clair : 7 jours satisfait ou modifié/remboursé 🤝\nAucune question, aucune complication.",
        # ---------------- CLOSING ----------------
        "on commence": "Génial 🔥 Envoie-moi :\n1️⃣ Ton nom de business\n2️⃣ Tes produits/services principaux\n3️⃣ Les 10 questions les plus fréquentes de tes clients\nEt je lance le build dès aujourd'hui 🚀",
        "je suis interesse": "Parfait 😊 On fait quoi : Starter 99€ pour tester, ou Business 150€ direct (le plus vendu) ?\nDans les deux cas je te guide tout du long 💪",
        "je prends le pack business": "Excellent choix, c'est le préféré de nos clients 🔥 Business 150€ :\n50% à la commande (Mobile Money, virement ou PayPal), 50% à la livraison.\nEnvoie-moi tes produits et on démarre 🚀",
    }


AGENT = WhatsAppBotAgent()
