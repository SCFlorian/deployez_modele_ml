# Déploiement d’un modèle de machine learning

## Description
Ici nous reprenons le modèle construit dans le projet "Classifez automatiquement des informations" et nous préparons son déploiement.  
L’objectif est de rendre le modèle accessible via une API développée avec **FastAPI**,  
et de gérer la persistance des données dans une base **PostgreSQL**, avec un suivi Git complet.

---

## Installation

### 1. Cloner le dépôt
```bash
git clone git@github.com:SCFlorian/deployez_modele_ml.git
cd deployez_modele_ml
```

### 2. Créer un environnement virtuel
```bash
python -m venv .venv
source .venv/bin/activate    # Mac / Linux
.venv\Scripts\activate       # Windows
```
### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

## Organisation du projet
- notebooks/ : notebooks du Projet 4 (entraînement et expérimentation)
- models/ : modèle sauvegardé (model.pkl)
- src/ : scripts Python
- api/ : API FastAPI
- tests/ : tests unitaires

## Utilisation

L’API sera exposée via FastAPI et servira les prédictions du modèle.
Des instructions détaillées sur l’utilisation seront ajoutées à l’étape 3.

## Authentification & Sécurisation

Une authentification par token et la gestion des secrets via .env seront mises en place aux étapes suivantes.

## Historique
- v1.0 : Mise en place de la structure de base (requirements, README, organisation des dossiers)