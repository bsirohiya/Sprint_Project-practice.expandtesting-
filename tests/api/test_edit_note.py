from time import sleep

from api_utils.read_data import read_json
from pages.api.notes import NotesAPI
from pages.ui.create_note import CreateNote
from pages.ui.login import LoginPage

def test_edit_note(setup_and_teardown, headers):

    driver = setup_and_teardown

    notes_api = NotesAPI()
    response = notes_api.get_all_notes(headers)

    response_json = response.json()
    notes = response_json["data"]
    note_id = notes[0]["id"]

    data = read_json("api_test_data/note.json")
    payload = data["edit_note_data"]

    notes_api.edit_note(note_id, headers, payload)

    lp = LoginPage(driver)
    cn = CreateNote(driver)

    # sleep(2)
    lp.login()
    # sleep(2)

    assert cn.valid_note_title() == payload["title"]
    assert cn.valid_note_content() == payload["description"]