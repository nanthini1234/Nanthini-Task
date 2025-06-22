from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_banks():
    response = client.get("/banks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_branches_success():
    response = client.get("/branches/ABHYUDAYA COOPERATIVE BANK LIMITED")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_branches_valid_bank():
    bank = "ABHYUDAYA COOPERATIVE BANK LIMITED"
    response = client.get(f"/branches/{bank}")
    assert response.status_code in [200, 404]  # Adjust as needed


def test_get_branches_fail():
    response = client.get("/branches/UnknownBank")
    assert response.status_code == 404
