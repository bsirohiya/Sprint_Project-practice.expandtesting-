import pytest
from api_core.auth import get_auth_data

@pytest.fixture(scope="function")
def auth_data():
    return get_auth_data()

@pytest.fixture(scope="function")
def headers(auth_data):
    return {
        "x-auth-token": auth_data['token']
    }

