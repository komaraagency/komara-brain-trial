"""Section 3 : Développement web — sites, apps.

Connaissance organisée en 6 axes :
  ACCUEIL · VENTE · PRISE DE RDV · CONSEIL · OBJECTION · CLOSING
"""
from agents.base_agent import BaseAgent


class DevWebAgent(BaseAgent):
    name = "dev_web"
    section = "Site Web, App"
    KEYWORDS = [
        "site web", "site internet", "site vitrine", "boutique en ligne",
        "e-commerce", "ecommerce", "application", "app mobile", "developpement",
        "landing page", "portfolio", "hebergement", "nom de domaine",
        "site", "web", "app", "seo", "google",
    ]
    FALLBACK = ("Je suis le spécialiste web 💻 (sites vitrines, boutiques, apps)\n"
                "Décris-moi ton projet et je te chifre ça vite 😉")

    KNOWLEDGE = {
        # ---------------- ACCUEIL ----------------
        "bonjour": "Bonjour 👋 Bienvenue côté web de Komara Agency 💻\nSite vitrine, boutique en ligne, app : raconte-moi ton projet 😊",
        "salut": "Salut 👋 L'équipe web de Komara Agency à ton service.\nUn site à créer ? Une app en tête ? Je t'écoute 🎧",
        "bonsoir": "Bonsoir 👋 Le web ne dort jamais 😄\nParle-moi de ton projet web, je prends note.",
        "ca va": "Ça va bien, merci 😊 Et toi ?\nUn projet de site ou d'app en tête ?",
        "qui etes vous": "Komara Agency 🇬🇳 — on construit des sites et apps qui vendent, pas juste qui brillent.\nVitrine, e-commerce, sur-mesure. Tu as déjà une présence en ligne ?",
        # ---------------- VENTE ----------------
        "prix site": "Ça dépend du projet 😊\nSite vitrine : 150-350€ 💼 Boutique e-commerce : 350-550€.\nSur-mesure : devis gratuit en 24h. Tu as déjà un nom de domaine ?",
        "combien coute un site": "Site vitrine : 150-350€ 💻 Boutique en ligne : 350-550€.\nTout inclus : design responsive, SEO de base, formation à la livraison.\nTu veux un devis détaillé ?",
        "je veux un site": "Excellente décision 🚀 Dis-moi :\n1️⃣ Vitrine (présenter) ou boutique (vendre) ?\n2️⃣ Ton activité\n3️⃣ Tes couleurs/style\nEt on lance ça 💪",
        "boutique en ligne": "Boutique e-commerce complète : 350-550€ 💳\nPaiement en ligne, gestion des produits, paniers relancés automatiquement.\nTu vends quoi ?",
        "app mobile": "Apps mobiles sur devis 📱 Dis-moi l'idée et le nombre d'écrans.\nOn fait aussi les PWA (app web installable, moins chère). C'est pour quel usage ?",
        "landing page": "Landing page qui convertit : à partir de 150€ 🎯\nUne page, un objectif : vendre ou capter des contacts.\nParfaite pour une offre ou un lancement. Tu lances quoi ?",
        "hebergement": "L'hébergement c'est le terrain de ton site 🏗️\nOn gère tout : domaine, hébergement, certificat HTTPS, emails pro.\nÀ partir de 30€/an tout compris. On le met dans ton pack ?",
        "seo": "Le SEO c'est apparaître quand on te cherche sur Google 🔎\nChaque site livré inclut le SEO de base (titres, vitesse, mobile).\nSEO avancé : sur devis selon la concurrence de ton secteur. Tu vises quels clients ?",
        # ---------------- PRISE DE RDV ----------------
        "rdv": "Avec plaisir 📅 Aujourd'hui 16h-19h ou demain 10h-13h ?\nOu appelle directement le +212 701-986219 😊\n15 minutes suffisent pour cadrer ton projet.",
        "appel": "Ok pour un appel 📞 Matin ou après-midi ?\nJe te rappelle au +212 701-986219. Prépare juste ton idée en 2-3 phrases 😄",
        "tu es dispo": "Toujours dispo 💪 Aujourd'hui ou demain ? Donne-moi un créneau et je bloque 📅",
        # ---------------- CONSEIL ----------------
        "conseil": "Mon conseil honnête : commence par un site vitrine propre + WhatsApp Business 🎯\nBeaucoup veulent une boutique avant même d'avoir des clients.\nLa vitrine te rend crédible, le WhatsApp vend, la boutique suit. C'est quoi ton stade ?",
        "vitrine ou boutique": "Vitrine si tu veux être trouvé et crédible (150-350€) 💼\nBoutique si tu vends en ligne directement (350-550€) 💳\nTest rapide : tes clients paient plutôt sur place ou à distance ?",
        "faut il un site ou les reseaux sociaux suffisent": "Les réseaux c'est la vitrine rapide, le site c'est la boutique officielle 🌐\nSans site : tu dépends de l'algorithme (une page fermée = business fermé).\nAvec site + réseaux : tu possèdes ta base. Mon conseil : les deux, en commençant petit 😊",
        "comment etre visible sur google": "3 piliers : fiche Google Business (gratuite !), site optimisé, avis clients ⭐\nLa fiche Google, tu peux la créer dès aujourd'hui, gratuitement.\nLe site renforce le tout. Ton business est déjà sur Google Maps ?",
        # ---------------- OBJECTION ----------------
        "c'est cher": "Je comprends 😊 Mais regarde : un seul contrat gagné grâce au site rembourse la vitrine.\nC'est un investissement, pas une dépense. Et payable en 2 fois : 50% au départ, 50% à la livraison.\nOn calcule le retour pour TON business ?",
        "pas le temps": "C'est moi qui bosse, pas toi 😄 Côté client ça prend 2-3 échanges : le brief, la validation, la mise en ligne.\n1-2 semaines plus tard, ton site tourne. On cale le brief quand ?",
        "je vais reflechir": "Prends ton temps 👌 Une question par curiosité : c'est le budget, ou l'utilité qui te fait hésiter ?\nSelon ta réponse je peux t'éclairer tout de suite 😊",
        "arnaque": "Méfiance compréhensible 🙏 Chez nous : convention signée, paiement 50/50, maquette validée AVANT de payer la 2e moitié.\nSi la maquette ne plaît pas, on la refait jusqu'à satisfaction. Zéro risque.",
        "je fais le site moi meme": "Tu peux, avec Wix ou WordPress 👏 Mais compte 2-3 semaines d'apprentissage pour un rendu moyen.\nNous : 7 jours, pro, qui convertit. Ton temps vaut plus que ça, non ? 😉",
        "wix fait ca gratuitement": "Wix gratuit = publicités partout + nom de domaine Wix 🚫\nÇa fait amateur au premier coup d'œil. Un site pro sur ton domaine, c'est ta crédibilité.\n150€ pour être fier de ton adresse, ça vaut le coup 😊",
        "mon neveu sait coder": "Super pour lui 😊 Mais est-ce qu'il livre en 7 jours, avec support 1 an et maintenance ?\nOn signe une convention, tout est clair. C'est la tranquillité que tu achètes.",
        "et si le site ne me plait pas": "Tu valides la maquette AVANT la 2e moitié du paiement 🤝\nOn la retravaille jusqu'à ce qu'elle te plaise. Puis seulement, on met en ligne.\nC'est TON site, tu as le dernier mot.",
        "trop complique a gerer": "On te livre avec une formation simple 🎓 Modifier un texte = 2 clics.\nEt si tu veux zéro effort : maintenance à partir de 30€/mois, on gère tout.\nTu préfères gérer ou déléguer ?",
        "je demande a mon associe": "Bonne démarche 👌 Je vous prépare un récap du projet + maquettes d'exemples en PDF.\nJe vous rappelle vendredi pour la décision. Ça marche pour vous ?",
        "maintenance c'est quoi": "La maintenance c'est l'entretien : mises à jour, sauvegardes, corrections 🔧\nComme une voiture : sans entretien, elle tombe en panne.\nÀ partir de 30€/mois, on s'occupe de tout. Tranquillité totale.",
        # ---------------- CLOSING ----------------
        "on commence": "Parfait 🔥 Pour lancer j'ai besoin de :\n1️⃣ Nom du business + activité\n2️⃣ Contenus principaux (textes, photos si tu en as)\n3️⃣ Style/couleurs aimées\nEt on démarre sous 48h 🚀",
        "je suis interesse": "Super 😊 Vitrine 150-350€, boutique 350-550€, payable en 2 fois.\nOn cadre ton projet en 10 minutes ? Réponds juste : vitrine ou boutique ?",
        "valide je prends": "Top 🔥 50% pour lancer la maquette, 50% à la livraison.\nMobile Money, virement ou PayPal. Envoie-moi le brief et c'est parti 🚀",
    }


AGENT = DevWebAgent()
