# Déploiement d'un modèle de Machine Learning - Explication CI/CD

## Conventions de code
- Respecter le style Python PEP8.
- Bien commenter le code et ajouter des docstrings simples pour les fonctions.

## Organisation Git
- main : branche stable.
- notebooks : pour les notebooks.
- model : pour le code lié au modèle.
- tests : pour les tests automatiques.

## CI/CD
- Les actions GitHub se trouvent dans .github/workflows/ci.yaml
- Le pipeline s’exécute automatiquement quand :
    - On fait un push sur main,
    - Ou une pull request vers main.

## Étapes du pipeline :
	1.	Installer Python et les dépendances.
	2.	Lancer les tests (dans tests/).
	3.	Déployer sur Hugging Face Spaces si les tests passent.

## Tests
- Les tests se trouvent dans tests/.
- Pour lancer les tests en local :
```bash
    pytest tests/
```

## Modèles & Notebooks
- Les modèles entraînés vont dans models/.
- Les expérimentations sont dans notebooks/.