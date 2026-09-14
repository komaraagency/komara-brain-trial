"""Section 2 : Création digitale — logo, visuel, branding."""
from agents.base_agent import BaseAgent


class CreationDigitaleAgent(BaseAgent):
    name = "creation_digitale"
    section = "Logo, Visuel, Branding"
    KEYWORDS = [
        "logo", "affiche", "flyer", "visuel", "image", "retouche", "photo",
        "branding", "charte graphique", "identite visuelle", "design",
        "carte de visite", "couverture facebook", "miniature", "montage video",
    ]
    FALLBACK = ("Je suis le spécialiste création digitale 🎨 (logo, affiches, branding, retouche)\n"
                "Dis-moi ton projet et je te propose la meilleure option 😉")
    KNOWLEDGE = {
        "prix logo": "Logo pro : 80€ (pack visuel à partir de 5€ pour les petites images).\n2 révisions incluses, express 24h +30%.\nC'est pour quel type de business ?",
        "prix affiche": "Affiche/flyer pro : à partir de 30€ 🎨\nFormats réseaux inclus (9:16, 1:1, carré). Tu veux un devis précis ?",
        "je veux un logo": "Avec plaisir ✨ Dis-moi :\n1️⃣ Le nom de ton business\n2️⃣ Le style (moderne, classique, africain...)\n3️⃣ Tes couleurs préférées\nEt je te fais ça pro 🇬🇳",
        "charte graphique": "La charte graphique c'est l'ADN visuel de ta marque 💎\nLogo + couleurs + typographies + règles d'usage.\nOn te construit une identité complète. Tu as déjà un logo ?",
        "retouche photo": "Retouche pro : photoréalisme 8K, lumière naturelle, texture de peau préservée 📸\nÀ partir de 5€ par visuel selon la complexité. Envoie ta photo !",
        "branding": "Le branding c'est ce que les gens ressentent quand ils voient ta marque 🤫\nOn te construit une identité complète : logo, couleurs, ton, visuels.\nC'est pour une nouvelle marque ou un rebranding ?",
        "combien de temps": "Logo : 48-72h. Affiche : 24-48h. Charte complète : 5-7 jours ⏱️\nExpress 24h possible avec +30%. C'est urgent pour toi ?",
        "es tu un robot": "Non non 😄 L'équipe Komara Agency, des créateurs digitaux passionnés.\nOn peut commencer par ton projet ?",
    }


AGENT = CreationDigitaleAgent()
