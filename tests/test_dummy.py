from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict_endpoint():
    payload = {
        "revenu_mensuel": 3500,
        "annees_dans_l_entreprise": 5,
        "satisfaction_employee_environnement": 3
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    json_resp = response.json()
    assert "prediction" in json_resp
    assert json_resp["prediction"] in [0, 1]
