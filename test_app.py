from unittest.mock import Mock
import pytest
from app import app, get_post_data


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_post_data(client):
    mock_response = Mock()
    mock_response.json.return_value = {
        "id": 1,
        "title": "Test Post Title",
        "body": "Test post body content",
        "userId": 1,
    }
    mock_response.raise_for_status.return_value = None

    def mock_http_client(url):
        assert url == "https://jsonplaceholder.typicode.com/posts/1"
        return mock_response

    with app.test_request_context():
        result = get_post_data(1, get_data_abstraction=mock_http_client)
        data = result.get_json()

        assert result.status_code == 200
        assert "title" in data
        assert "body" in data
