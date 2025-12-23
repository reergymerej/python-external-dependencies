from unittest.mock import Mock, patch
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("requests.get")
def test_get_post_data(mock_get, client):
    mock_response = Mock()
    mock_response.json.return_value = {
        "id": 1,
        "title": "Test Post Title",
        "body": "Test post body content",
        "userId": 1,
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    response = client.get("/posts/1")

    assert response.status_code == 200

    data = response.get_json()
    assert "title" in data
    assert "body" in data
