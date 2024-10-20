import pytest
import requests
from requests.exceptions import HTTPError
from app import APIClient  # Adjust the import based on your file name

# Sample data for testing
mock_users = [
    {"id": 1, "name": "Best User", "email": "BestUser@example.com"},
    {"id": 2, "name": "Great User", "email": "GreatUser@example.com"},
]

mock_albums = [
    {"userId": 1, "id": 1, "title": "Best album"},
    {"userId": 1, "id": 2, "title": "Great album"},
]

mock_posts = [
    {"userId": 1, "id": 1, "title": "Best title", "body": "Best title body"},
    {"userId": 1, "id": 2, "title": "Great title", "body": "Great title body"},
]

# Fixture for the APIClient setup
@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.parametrize("endpoint, expected_data", [
    ("/users", mock_users),
    ("/albums", mock_albums),
    ("/posts", mock_posts),
])
def test_api_client_success(requests_mock, api_client, endpoint, expected_data):
    requests_mock.get(api_client.URL + endpoint, json=expected_data, status_code=200)

    if endpoint == "/users":
        data = api_client.get_users()
    elif endpoint == "/albums":
        data = api_client.get_albums()
    elif endpoint == "/posts":
        data = api_client.get_posts()

    assert data == expected_data  # Verify the returned data matches the expected data

@pytest.mark.parametrize("endpoint", [
    "/users",
    "/albums",
    "/posts",
])
def test_api_client_failure(requests_mock, api_client, endpoint):
    requests_mock.get(api_client.URL + endpoint, status_code=404)

    with pytest.raises(HTTPError):  # Ensure an HTTPError is raised for failed requests
        if endpoint == "/users":
            data = api_client.get_users()
        elif endpoint == "/albums":
            data = api_client.get_albums()
        elif endpoint == "/posts":
            data = api_client.get_posts()

       