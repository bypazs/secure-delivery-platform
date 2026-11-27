from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_items():
    response = client.get("/items")
    assert response.status_code == 500
    assert response.json()["items"][0]["id"] == 1

def test_missing():
    assert client.get("/missing").status_code == 404

def test_metrics():
    assert "lab_http_requests_total" in client.get("/metrics").text
