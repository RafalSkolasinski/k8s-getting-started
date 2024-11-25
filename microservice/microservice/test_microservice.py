import pytest
from fastapi.testclient import TestClient
from microservice.microservice import app


@pytest.fixture
def test_client():
    return TestClient(app)


def test_root_endpoint(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello world!"


def test_hello_endpoint(test_client):
    name = "Alice"
    response = test_client.get(f"/hello/{name}")
    assert response.status_code == 200
    assert response.json() == f"Hello, {name}!"


def test_ping_endpoint(test_client):
    response = test_client.get("/ping")
    assert response.status_code == 200
    assert response.json() == "pong"


def test_secrets_endpoint(test_client):
    response = test_client.get("/secrets")
    assert response.status_code == 200
    assert response.json() == [
        "There would be some secrets here...",
        "... but there are none.",
    ]


def test_date_endpoint(test_client):
    response = test_client.get("/date")
    assert response.status_code == 200
    data = response.json()
    assert "year" in data
    assert "month" in data
    assert "day" in data
    assert "now" in data

    assert isinstance(data["year"], int)
    assert isinstance(data["month"], int)
    assert isinstance(data["day"], int)
    assert isinstance(data["now"], str)
