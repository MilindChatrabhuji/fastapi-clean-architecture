from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "healthy", "architecture": "clean_ddd"}

def test_create_user():
    payload = {"email": "architect@example.com", "full_name": "Senior Systems Architect"}
    res = client.post("/api/v1/users/", json=payload)
    assert res.status_code == 201
    data = res.json()
    assert data["email"] == "architect@example.com"
    assert "id" in data
