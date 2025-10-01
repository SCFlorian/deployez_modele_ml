from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Je charge le modèle et seuil
model = joblib.load("models/final_model.pkl")
with open("models/threshold.txt", "r") as f:
    best_thr = float(f.read())

# Définition de l’application FastAPI
app = FastAPI(title="API CatBoost - Déploiement ML")

# Schéma d’entrée
class EmployeeFeatures(BaseModel):
    revenu_mensuel: int
    annees_dans_l_entreprise: int
    satisfaction_employee_environnement: int

# Endpoint de prédiction
@app.post("/predict")
def predict(features: EmployeeFeatures):
    # Transformation des features en tableau numpy
    X = np.array([[features.revenu_mensuel,
                   features.annees_dans_l_entreprise,
                   features.satisfaction_employee_environnement]])
    
    # Prédire proba
    proba = model.predict_proba(X)[:, 1][0]
    prediction = int(proba >= best_thr)

    return {
        "probability": proba,
        "prediction": prediction
    }