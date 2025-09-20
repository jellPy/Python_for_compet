from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_crud_flow():
    # create
    r = client.post("/items", json={
        "name": "Book",
        "price": 12.5,
        "tags": ["education"]
    })
    assert r.status_code == 201
    item = r.json()
    assert item["id"] == 1

    # read by id
    r = client.get("/items/1")
    assert r.status_code == 200
    assert r.json()["name"] == "Book"

    # list with filter
    r = client.get("/items?min_price=10&tag=education")
    assert len(r.json()) == 1

def test_not_found():
    r = client.get("/items/999")
    assert r.status_code == 404
