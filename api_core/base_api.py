import requests

class BaseAPI:
    def __init__(self, base_url_api):
        self.base_url_api = base_url_api
        self.session = requests.Session()

    def get(self, endpoint, headers=None, params=None):
        return self.session.get(f"{self.base_url_api}{endpoint}", headers=headers, params=params, verify=False)

    def post(self, endpoint, headers=None, json=None, params=None):
        return self.session.post(f"{self.base_url_api}{endpoint}", headers=headers, json=json, params=params)

    def put(self, endpoint, headers=None, json=None, params=None):
        return self.session.put(f"{self.base_url_api}{endpoint}", headers=headers, json=json, params=params, verify=False)

    def delete(self, endpoint, headers=None, params=None):
        return self.session.delete(f"{self.base_url_api}{endpoint}", headers=headers, params=params, verify=False)

