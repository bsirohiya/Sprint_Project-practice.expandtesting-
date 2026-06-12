from pages.api.notes import NotesAPI
from api_utils.read_data import read_json


def test_valid_create_note(headers):

    notes_api = NotesAPI()

    payload = read_json("api_test_data/note.json")

    response = notes_api.create_note(headers, payload)

    assert response.status_code == 200