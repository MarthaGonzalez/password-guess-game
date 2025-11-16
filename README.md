# password-guess-game

Projet d'activité collaborative GitHub (SRC — DevOps & Git).
Création d'un script Python qui permet d’évaluer la robustesse des mots de passe
## Objectifs
- Pratiquer GitHub en équipe : branches, commits, push, Pull Requests, revue, merge, résolution de conflits.
- Améliorer un script Python simple par itérations.

## Démarrage rapide
```bash
git clone https://github.com/<org-or-user>/password-guess-game.git
```
## Tâches à réaliser (features)
- **A. Limite d'essais** : ajouter `--max-attempts` (0 = illimité). Arrêter et révéler le mot quand la limite est atteinte.
- **B. Option "triche"** : `--cheat` affiche le mot (debug/test).
- **C. Historique des tentatives** : lister toutes les propositions à la fin.
- **D. Fichier de mots** : `--words-file` charge la liste depuis `words.txt`.

## Workflow collaboratif recommandé
1. Créer une branche pour chaque feature : `git checkout -b feature/max-attempts-<initiales>`
2. Committer régulièrement avec des messages clairs.
3. Pousser la branche : `git push -u origin feature/max-attempts-<initiales>`
4. Ouvrir une PR, demander une revue, intégrer les changements.
5. Mettre à jour la branche `main` localement : `git checkout main && git pull origin main`

## CI/CD
- **CI simple** : `.github/workflows/python-tests.yml` exécute `pytest` sur chaque push/PR.
- **CI complète** : `.github/workflows/python-lint-test.yml` exécute `flake8` + `pytest`.

## Exécution
- Python 3.9+ recommandé.
- Fichier `words.txt` fourni (une entrée par ligne).
- Sous Windows : utilisez `py` ou `python` selon l'installation.

