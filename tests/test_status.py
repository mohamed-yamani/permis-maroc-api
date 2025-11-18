from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_status_endpoint_returns_ok():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"ok": True, "service": "Permis de Conduire Maroc API"}


