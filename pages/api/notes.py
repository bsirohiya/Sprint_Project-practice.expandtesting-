# from fixtures.api_fixture import headers
from pages.api.login import BaseAPI
from api_utils.config import base_url_api

class NotesAPI:

    def __init__(self):
        self.api = BaseAPI(base_url_api)

    def create_note(self, headers, payload):
        return self.api.post(
            endpoint="/notes",
            headers=headers,
            json=payload
        )

    def get_all_notes(self, headers):
        return self.api.get(
            endpoint="/notes",
            headers=headers
        )

    def delete_note(self, note_id, headers):
        return self.api.delete(
            endpoint=f"/notes/{note_id}",
            headers=headers
        )

    def edit_note(self, note_id, headers, payload):
        return self.api.put(
            endpoint=f"/notes/{note_id}",
            headers=headers,
            json=payload
        )