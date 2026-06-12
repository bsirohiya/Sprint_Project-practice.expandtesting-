from api_core.base_api import BaseAPI
from api_utils.config import base_url_api

class LoginAPI:

    def __init__(self):
        self.api = BaseAPI(base_url_api)

    def login(self, payload):
        return self.api.post("/users/login", json=payload)