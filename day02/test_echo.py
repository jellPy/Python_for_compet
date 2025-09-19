from fastapi.testclient import TestClient
from main import app   # импортируем приложение FastAPI

client = TestClient(app)   # создаём клиент для тестирования

def test_echo_ok():
    resp = client.post("/echo", json={"message": "a", "times": 2})
    assert resp.status_code == 201
    assert resp.json() == ["a", "a"]

def test_echo_validation():
    resp = client.post("/echo", json={"message": "a", "times": "x"})
    assert resp.status_code == 422
