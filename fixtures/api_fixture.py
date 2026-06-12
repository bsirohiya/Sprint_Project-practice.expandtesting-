import pytest
from api_core.auth import get_auth_data

@pytest.fixture(scope="session")
def auth_data():
    return get_auth_data()

@pytest.fixture(scope="session")
def headers(auth_data):
    return {
        "x-auth-token": auth_data['token']
    }