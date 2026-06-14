import pytest

from api_utils.read_data import read_json
from pages.api.notes import NotesAPI

@pytest.mark.api
@pytest.mark.order(11)
def test_valid_edit_note(headers):

    notes_api = NotesAPI()
    response = notes_api.get_all_notes(headers)

    response_json = response.json()
    notes = response_json["data"]
    note_id = notes[0]["id"]

    data = read_json("api_test_data/note.json")
    payload = data["edit_note_data"]

    notes_api.edit_note(note_id, headers, payload)

    res = notes_api.get_all_notes(headers)
    res_json = res.json()
    res_data = res_json["data"]

    edited_note_title = res_data[0]["title"]
    edited_note_desc = res_data[0]["description"]

    assert edited_note_title == payload["title"]
    assert edited_note_desc == payload["description"]


@pytest.mark.api
@pytest.mark.order(12)
def test_invalid_edit_note(headers):

    notes_api = NotesAPI()

    response = notes_api.get_all_notes(headers)

    response_json = response.json()
    notes = response_json["data"]

    note_id = notes[0]["id"]

    data = read_json("api_test_data/note.json")
    payload = data["invalid_edit_note_data"]

    edit_response = notes_api.edit_note(note_id, headers, payload)

    assert edit_response.status_code == 400
