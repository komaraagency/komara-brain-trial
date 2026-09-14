"""Section 2 : Création digitale — logo, visuel, branding.

Connaissance organisée en 6 axes :
  ACCUEIL · VENTE · PRISE DE RDV · CONSEIL · OBJECTION · CLOSING
"""
from agents.base_agent import BaseAgent


class CreationDigitaleAgent(BaseAgent):
    name = "creation_digitale"
    section = "Logo, Visuel, Branding"
    KEYWORDS = [
        "logo", "affiche", "flyer", "visuel", "image", "retouche", "photo",
        "branding", "charte graphique", "identite visuelle", "design",
        "carte de visite", "couverture facebook", "miniature", "montage video",
        "graphique", "couleur", "banniere",
    ]
    FALLBACK = ("Je suis le spécialiste création digitale 🎨 (logo, affiches, branding, retouche)\n"
                "Dis-moi ton projet et je te propose la meilleure option 😉")

    KNOWLEDGE = {
        # ---------------- ACCUEIL ----------------
        "bonjour": "Bonjour 👋 Bienvenue dans l'atelier créatif de Komara Agency 🎨\nLogo, affiche, retouche, branding : dis-moi ce que tu veux créer 😊",
        "salut": "Salut 👋 L'équipe créa de Komara Agency à ton écoute.\nTu as un projet visuel en tête ? Je suis tout ouïe 👂",
        "bonsoir": "Bonsoir 👋 La création ne dort jamais 😄\nParle-moi de ton projet visuel, je note tout.",
        "ca va": "Ça va nickel, merci 😊 Et toi ?\nUn projet visuel en tête ? Logo, affiche, retouche ?",
        "qui etes vous": "Komara Agency 🇬🇳 — studio de création digitale entre la Guinée et le Maroc.\nLogos, affiches, branding, retouches photoréalistes. On donne une identité aux business. Tu crées quoi ?",
        # ---------------- VENTE ----------------
        "prix logo": "Logo pro : 80€ 💎 2 révisions incluses, fichiers HD (PNG, PDF, vectoriel).\nExpress 24h : +30%. C'est pour quel type de business ?",
        "prix affiche": "Affiche/flyer pro : à partir de 30€ 🎨\nFormats réseaux inclus (9:16 stories, 1:1 feed, 16:9).\nTu veux un devis précis ?",
        "je veux un logo": "Avec plaisir ✨ Dis-moi :\n1️⃣ Le nom de ton business\n2️⃣ Le style (moderne, classique, africain...)\n3️⃣ Tes couleurs préférées\nEt je te fais ça pro 🇬🇳",
        "retouche photo": "Retouche pro niveau studio 📸 Photoréalisme 8K, lumière naturelle, texture de peau préservée.\nÀ partir de 5€ par visuel selon la complexité. Envoie ta photo !",
        "charte graphique": "La charte graphique c'est l'ADN visuel de ta marque 💎\nLogo + couleurs + typographies + règles d'usage + déclinaisons.\nTu as déjà un logo ou on part de zéro ?",
        "branding": "Le branding c'est ce que les gens ressentent quand ils voient ta marque 🤫\nIdentité complète : logo, couleurs, ton, visuels réseaux.\nC'est pour une nouvelle marque ou un rebranding ?",
        "carte de visite": "Carte de visite pro : à partir de 20€ 💼 Recto/verso, fichiers prêts à imprimer (300 dpi).\nTu as déjà le logo ou on fait le pack logo + carte ?",
        "montage video": "Montage vidéo et miniatures 🎬 TikTok/Reels/Youtube.\nMiniature YouTube : 10€. Montage complet : sur devis selon la durée.\nTu as les rushs ou il faut tout créer ?",
        # ---------------- PRISE DE RDV ----------------
        "rdv": "Volontiers 📅 Aujourd'hui 16h-19h ou demain 10h-13h ?\nOu directement par téléphone au +212 701-986219 😊\nOn parlera de ton projet autour d'un (thé virtuel 😄).",
        "appel": "Ok pour un appel 📞 Matin ou après-midi ?\nJe te rappelle au +212 701-986219. 10 minutes suffisent pour cerner ton besoin 😊",
        "tu es dispo": "Toujours dispo pour parler créa 😄 Aujourd'hui ou demain ? Donne-moi un créneau et c'est noté 📅",
        # ---------------- CONSEIL ----------------
        "conseil": "Mon conseil : commence par le logo, puis la charte 🎯\nUn business sans identité paraît amateur, même avec un bon produit.\nLogo 80€ d'abord, le reste suit. C'est quoi ton activité ?",
        "quelle couleur pour ma marque": "Les couleurs parlent avant les mots 🎨\nBleu = confiance · Rouge = énergie · Vert = nature · Or = prestige · Noir = luxe.\nC'est quoi l'émotion que ton client doit ressentir ? Je te dirai la couleur 😉",
        "c'est quoi un bon logo": "3 critères : simple, mémorable, intemporel ✨\nSimple = lisible en petit. Mémorable = reconnu en 1 seconde. Intemporel = encore beau dans 10 ans.\nNike, Apple, MTN : aucune ne réinvente la roue 😄",
        "besoin d'un site aussi": "On fait tout : logo → site → bot 💪 Si tu veux une image complète, on regarde le pack site avec l'équipe web.\nCommençons par le visuel, ton identité d'abord 😊",
        # ---------------- OBJECTION ----------------
        "c'est cher": "Je comprends 😊 Mais pense : deux boutiques, même produit — celle au visuel propre vend 2-3 fois plus.\n80€ pour un logo qui travaille pour toi 10 ans = 8€/an. Rentabilisé à la première vente crédible.\nOn peut commencer petit si tu veux.",
        "pas le temps": "Justement, c'est MOI qui travaille 😄 Tu m'envoies juste le nom et l'activité, je te propose 3 pistes.\n20 minutes de ton côté, et le tour est joué. On regarde ça quand ?",
        "je vais reflechir": "Prends ton temps 👌 Juste par curiosité : c'est le prix, ou le style qui te fait hésiter ?\nSi c'est le style, je peux te montrer des exemples tout de suite 😊",
        "arnaque": "Méfiance saine, je comprends 🙏 Chez nous : 2 révisions incluses, payement en 2 fois possible (50/50), et tu valides avant livraison finale.\nTu vois le travail à chaque étape. Zéro surprise.",
        "mon cousin fait du design": "Génial s'il maîtrise 😊 Mais est-ce qu'il fournit fichiers pro (vectoriel, 300 dpi), révisions et délais garantis ?\nNous c'est notre métier, avec un processus éprouvé. Mais si ton cousin est fort, profites-en 😉",
        "canva le fait gratuitement": "Canva c'est super pour débuter 👏 Mais un logo pro doit être vectoriel (net à toutes les tailles) et unique.\nLes templates Canva, des milliers de business les utilisent déjà. Tu mérites du sur-mesure 😊",
        "je fais moi meme": "Courageux 💪 Mais l'identité visuelle, c'est un métier : composition, couleurs, typographies.\nTu te concentres sur ton business, moi sur ton image. Chacun son métier 😄",
        "pas sur que ca me plaise": "Pour ça il y a 2 révisions incluses 🤝 Et je te propose 3 pistes de départ : tu choisis ta direction.\nSi vraiment rien ne te plaît après les révisions, on en rediscute. Simple.",
        "et si je n'aime pas": "Tu valides chaque étape : pistes → création → révisions → livraison 👌 Rien part sans ton accord.\nEt 2 révisions incluses pour affiner. C'est TA marque 😊",
        "je demande a mon associe": "Très bien 👌 Je te prépare un mini-board avec 3 styles possibles à lui montrer.\nVous me dites la direction et je lance. Je vous recontacte vendredi ?",
        # ---------------- CLOSING ----------------
        "on commence": "Parfait 🔥 Envoie-moi :\n1️⃣ Nom du business\n2️⃣ Activité en une phrase\n3️⃣ Couleurs aimées (ou « décolle-toi » 😄)\nEt je te livre 3 pistes sous 48h 🚀",
        "je suis interesse": "Super 😊 Logo 80€, affiche 30€, charte complète sur devis.\nOn commence par quoi ? Si tu hésites, le logo d'abord c'est la base 💪",
        "valide je prends": "Excellente décision 🔥 50% à la commande, 50% à la livraison.\nMobile Money, virement ou PayPal. Envoie-moi les infos et c'est parti 🚀",
    }


AGENT = CreationDigitaleAgent()
