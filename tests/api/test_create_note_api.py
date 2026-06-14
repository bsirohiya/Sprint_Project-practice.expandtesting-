import pytest

from pages.api.notes import NotesAPI
from api_utils.read_data import read_json

@pytest.mark.api
@pytest.mark.order(9)
def test_valid_create_note(headers):

    notes_api = NotesAPI()

    config = read_json("api_test_data/note.json")
    payload = config["valid_note_data"]

    response = notes_api.create_note(headers, payload)

    assert response.status_code == 200

@pytest.mark.api
@pytest.mark.order(10)
def test_invalid_create_note(headers):

    notes_api = NotesAPI()

    config = read_json("api_test_data/note.json")
    payload = config["invalid_note_data"]

    response = notes_api.create_note(headers, payload)

    # checking 400 (Bad request) status code means note is not created
    assert response.status_code == 400
