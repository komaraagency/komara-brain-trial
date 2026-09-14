"""Section 3 : Développement web — sites, apps."""
from agents.base_agent import BaseAgent


class DevWebAgent(BaseAgent):
    name = "dev_web"
    section = "Site Web, App"
    KEYWORDS = [
        "site web", "site internet", "site vitrine", "boutique en ligne",
        "e-commerce", "application", "app mobile", "developpement",
        "landing page", "portfolio", "hebergement", "nom de domaine",
    ]
    FALLBACK = ("Je suis le spécialiste web 💻 (sites vitrines, boutiques, apps)\n"
                "Décris-moi ton projet et je te chifire ça vite 😉")
    KNOWLEDGE = {
        "prix site": "Ça dépend du projet 😊\nSite vitrine : 150-350€. Boutique e-commerce : 350-550€.\nSur-mesure : devis gratuit en 24h. Tu as déjà un nom de domaine ?",
        "combien coute un site": "Site vitrine : 150-350€ 💻 Boutique en ligne : 350-550€.\nTout inclus : design responsive, SEO de base, formation. Tu veux un devis ?",
        "je veux un site": "Excellent décision 🚀 Un site pro change la crédibilité d'un business.\nDis-moi :\n1️⃣ Vitrine ou boutique ?\n2️⃣ Ton activité\n3️⃣ Tes couleurs/style\nEt on lance ça 💪",
        "boutique en ligne": "Boutique e-commerce complète : 350-550€ 💳\nPaiement en ligne, gestion de stock, paniers relancés automatiquement.\nTu vends quoi ?",
        "app mobile": "Apps mobiles sur devis 📱 Dis-moi l'idée et le nombre d'écrans nécessaires.\nOn fait aussi les PWA (app web installable, moins cher). C'est pour quel usage ?",
        "delai": "Site vitrine : 1-2 semaines. Boutique : 2-4 semaines ⏱️\nUn planning précis te sera envoyé avant de commencer. C'est pour quand ?",
        "maintenance": "Maintenance : on s'en occupe 🔧 Corrections, mises à jour, sauvegardes.\nÀ partir de 30€/mois. Tu veux qu'on gère ça pour toi ?",
        "es tu un robot": "Pas du tout 😄 L'équipe Komara Agency, des devs qui aiment ce qu'ils font.\nParlons de ton projet !",
    }


AGENT = DevWebAgent()
