from fastapi.testclient import TestClient
from main import app

client = TestClient(app)   # локальный HTTP-клиент

def test_ping():
    response = client.get("/ping")        # обращаемся к эндпоинту
    assert response.status_code == 200    # проверяем статус
    assert response.json() == {"pong": True}
