#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jeu de devinette de mot de passe faibles.
Version starter pour activité GitHub collaborative.
Objectif pédagogique :
- pratiquer Git (branch, commit, push, PR, merge, conflits)
- améliorer progressivement ce script via 4 fonctionnalités
"""

import random
import argparse
from typing import List


# Liste par défaut (sera remplacée par un chargement fichier dans la feature D)
WORDS = ["password", "123456", "qwerty", "letmein", "admin", "welcome"]


def common_letters(a: str, b: str) -> List[str]:
    """Retourne les lettres communes (sans doublon) triées alphabétiquement."""
    return sorted(set(a) & set(b))


def load_words_from_file(path: str) -> List[str]:
    """Charge une liste de mots depuis un fichier texte (un mot par ligne).
    TODO (Feature D): Améliorer la gestion d'erreurs (fichier manquant, vide, encodage).
    """
    words = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            w = line.strip()
            if w:
                words.append(w)
    return words


def parse_args():
    """Analyse la ligne de commande.
    TODO (Feature A): ajouter un argument --max-attempts (int, 0 = illimité)
    TODO (Feature B): ajouter un flag --cheat pour afficher le mot secret (debug/test)
    TODO (Feature D): ajouter un argument --words-file pour charger la liste depuis un fichier
    """
    p = argparse.ArgumentParser(description="Jeu: deviner un mot de passe faible.")
    # TODO (A) p.add_argument("--max-attempts", type=int, default=0, help="Nombre maximum d'essais (0 = illimité)")
    # TODO (B) p.add_argument("--cheat", action="store_true", help="Affiche le mot secret (debug)")
    # TODO (D) p.add_argument("--words-file", type=str, help="Chemin du fichier de mots faibles")
    return p.parse_args()


def choose_password(words: List[str]) -> str:
    """Sélectionne un mot aléatoire dans la liste fournie."""
    return random.choice(words) if words else ""


def game():
    """Boucle de jeu simple (starter).

    TODO (A): si --max-attempts > 0, interrompre après N essais et révéler le mot.
    TODO (B): si --cheat, afficher le mot au lancement (debug/test).
    TODO (C): enregistrer l'historique des tentatives et l'afficher à la fin.
    TODO (D): si --words-file fourni, charger les mots depuis ce fichier.
    """
    args = parse_args()

    # Source des mots
    words = WORDS[:]  # copie
    # TODO (D): if args.words_file: words = load_words_from_file(args.words_file)

    secret = choose_password(words)
    if not secret:
        print("Aucun mot disponible. Vérifiez la liste ou le fichier de mots.")
        return

    # TODO (B): if args.cheat: print(f"[CHEAT] Mot secret: {secret}")

    print("Indices: longueur et première lettre.")
    print(f"Longueur: {len(secret)}")
    print(f"Première lettre: {secret[0]}")

    attempts = 0
    attempts_history = []  # TODO (C): remplir et afficher à la fin

    while True:
        guess = input("Proposez un mot : ").strip()
        attempts += 1
        # TODO (C): attempts_history.append(guess)

        if guess == secret:
            print("Bravo !")
            break

        print(f"Lettres communes : {common_letters(guess, secret)}")

        # TODO (A): gérer la limite d'essais (--max-attempts)

    print(f"Nombre d'essais : {attempts}")
    # TODO (C): print("Historique des tentatives :", attempts_history)


if __name__ == "__main__":
    game()
