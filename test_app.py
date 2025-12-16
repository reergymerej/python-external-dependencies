import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_post_data(client):
    response = client.get("/posts/1")

    assert response.status_code == 200

    data = response.get_json()
    assert "title" in data
    assert "body" in data
