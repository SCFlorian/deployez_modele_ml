from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_predict_endpoint():
    payload = {
        "revenu_mensuel": 3500,
        "annees_dans_l_entreprise": 5,
        "satisfaction_employee_environnement": 3,
        "note_evaluation_precedente": 4,
        "satisfaction_employee_nature_travail": 3,
        "satisfaction_employee_equipe": 4,
        "satisfaction_employee_equilibre_pro_perso": 3,
        "note_evaluation_actuelle": 4,
        "augmentation_salaire_precedente_pourcent": 5,
        "distance_domicile_travail": 10,
        "niveau_education": 2,
        "annees_depuis_la_derniere_promotion": 1,
        "experience_externe": 3,
        "score_satisfaction": 3,
        "augmentation_par_formation": 2,
        "pee_par_anciennete": 1,

        "genre": 1,
        "heure_supplementaires": 0,
        "frequence_deplacement": 1,
        "a_suivi_formation": 1,
        "tranche_age": 2,
        "statut_marital_Celibataire": 1,
        "statut_marital_Divorce": 0,
        "statut_marital_Marie": 0,
        "departement_Commercial": 1,
        "departement_Consulting": 0,
        "departement_RessourcesHumaines": 0,
        "poste_AssistantdeDirection": 0,
        "poste_CadreCommercial": 0,
        "poste_Consultant": 1,
        "poste_DirecteurTechnique": 0,
        "poste_Manager": 0,
        "poste_ReprésentantCommercial": 0,
        "poste_RessourcesHumaines": 0,
        "poste_SeniorManager": 0,
        "poste_TechLead": 0,
        "promotion_recente": 1,
        "domaine_etude_Autre": 0,
        "domaine_etude_Entrepreunariat": 0,
        "domaine_etude_InfraCloud": 0,
        "domaine_etude_Marketing": 0,
        "domaine_etude_RessourcesHumaines": 0,
        "domaine_etude_TransformationDigitale": 1
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    result = response.json()
    assert "prediction" in result
    assert "probability" in result
    assert result["prediction"] in [0, 1]