from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# Charger le modèle entraîné
model = joblib.load("models/final_model.pkl")
with open("models/threshold.txt", "r") as f:
    threshold = float(f.read())

# Définition des features attendues (43 colonnes sauf la cible)
class EmployeeFeatures(BaseModel):
    revenu_mensuel: int
    annees_dans_l_entreprise: int
    satisfaction_employee_environnement: int
    note_evaluation_precedente: int
    satisfaction_employee_nature_travail: int
    satisfaction_employee_equipe: int
    satisfaction_employee_equilibre_pro_perso: int
    note_evaluation_actuelle: int
    augmentation_salaire_precedente_pourcent: float
    distance_domicile_travail: int
    niveau_education: int
    annees_depuis_la_derniere_promotion: int
    experience_externe: int
    score_satisfaction: float
    augmentation_par_formation: float
    pee_par_anciennete: float

    genre: int
    heure_supplementaires: int
    frequence_deplacement: int
    a_suivi_formation: int
    tranche_age: int
    statut_marital_Celibataire: int
    statut_marital_Divorce: int
    statut_marital_Marie: int
    departement_Commercial: int
    departement_Consulting: int
    departement_RessourcesHumaines: int
    poste_AssistantdeDirection: int
    poste_CadreCommercial: int
    poste_Consultant: int
    poste_DirecteurTechnique: int
    poste_Manager: int
    poste_ReprésentantCommercial: int
    poste_RessourcesHumaines: int
    poste_SeniorManager: int
    poste_TechLead: int
    promotion_recente: int
    domaine_etude_Autre: int
    domaine_etude_Entrepreunariat: int
    domaine_etude_InfraCloud: int
    domaine_etude_Marketing: int
    domaine_etude_RessourcesHumaines: int
    domaine_etude_TransformationDigitale: int

app = FastAPI()

@app.post("/predict")
def predict(features: EmployeeFeatures):
    data = pd.DataFrame([features.model_dump()])
    proba = model.predict_proba(data)[:, 1][0]
    prediction = int(proba >= threshold)
    return {"prediction": prediction, "probability": float(proba)}