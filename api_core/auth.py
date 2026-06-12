from pages.api.login import LoginAPI
from api_utils.read_data import read_json

def get_auth_data():
    data = read_json("api_test_data/login.json")
    payload = data["valid_user"]

    login_api = LoginAPI()

    response = login_api.login(payload)

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())

    assert response.status_code == 200

    res_json = response.json()

    token = res_json["data"]["token"]
    user_id = res_json["data"]["id"]   # confirm key

    return {
        "token": token,
        "user_id": user_id
    }