import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_post_data(client):
    """
    This test demonstrates the problems with testing external APIs.

    This test 'passes' but violates fundamental testing principles:

    1. SLOW: Makes real HTTP calls (hundreds of ms vs microseconds)
    2. NON-DETERMINISTIC: External data can change at any time
    3. ENVIRONMENT-DEPENDENT: May not work in CI, behind firewall, etc.
    4. CREDENTIAL ISSUES: Different environments need different access
    5. BRITTLE: External service changes break unrelated code

    A good test should be fast, predictable, and isolated.
    This is none of those things.
    """
    # This makes a real HTTP call - SLOW and UNRELIABLE
    response = client.get('/posts/1')

    # Passes now, but what if JSONPlaceholder is down during CI?
    assert response.status_code == 200

    # Non-deterministic: What if the external API changes this data?
    data = response.get_json()
    assert 'title' in data  # Fragile: depends on external service contract
    assert 'body' in data   # What if they rename these fields tomorrow?

    # We have no control over what data we get back
    # How do we test error cases? Edge cases? Specific scenarios?