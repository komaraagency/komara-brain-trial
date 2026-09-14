"""Classe de base pour tous les agents Komara Agency."""
from __future__ import annotations
import re
from typing import Optional


class BaseAgent:
    """Tous les agents héritent d'ici : nom, mots-clés, mini-cerveau, réponse."""

    name: str = "base"
    section: str = "général"
    # mots-clés d'intention -> score de routage
    KEYWORDS: list[str] = []
    # mini-cerveau embarqué : question -> réponse
    KNOWLEDGE: dict[str, str] = {}
    FALLBACK: str = "Je note ta demande 😊 Peux-tu me donner un peu plus de détails ?"

    def normalize(self, text: str) -> str:
        t = text.lower().strip()
        t = re.sub(r"[éèêë]", "e", t); t = re.sub(r"[àâä]", "a", t)
        t = re.sub(r"[îï]", "i", t); t = re.sub(r"[ôö]", "o", t)
        t = re.sub(r"[ùûü]", "u", t); t = re.sub(r"[ç]", "c", t)
        return re.sub(r"\s+", " ", t)

    def match_score(self, text: str) -> int:
        """Score de routage : combien de mots-clés reconnus dans le message."""
        t = self.normalize(text)
        return sum(1 for kw in self.KEYWORDS if self.normalize(kw) in t)

    def find_answer(self, text: str) -> Optional[str]:
        """Recherche exacte puis partielle dans le mini-cerveau."""
        t = self.normalize(text)
        # 1) correspondance directe (une question du cerveau contenue dans le message, ou l'inverse)
        for question, answer in self.KNOWLEDGE.items():
            q = self.normalize(question)
            if q == t or q in t or t in q:
                return answer
        # 2) correspondance par mots significatifs (>= 70% des mots de la question)
        t_words = set(t.split())
        best, best_score = None, 0.0
        for question, answer in self.KNOWLEDGE.items():
            q_words = set(self.normalize(question).split())
            if not q_words:
                continue
            overlap = len(q_words & t_words) / len(q_words)
            if overlap > best_score:
                best, best_score = answer, overlap
        if best and best_score >= 0.7:
            return best
        return None

    def respond(self, message: str, context: Optional[dict] = None) -> dict:
        answer = self.find_answer(message) or self.FALLBACK
        return {
            "agent": self.name,
            "section": self.section,
            "reply": answer,
            "handoff": answer == self.FALLBACK,
        }
