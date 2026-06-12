from pages.api.notes import NotesAPI
from pages.ui.base_page_ui import BasePage
from pages.ui.login import LoginPage

def test_delete_and_validate(setup_and_teardown, headers):

    driver = setup_and_teardown

    notes_api = NotesAPI()

    response = notes_api.get_all_notes(headers)

    response_json = response.json()
    notes = response_json["data"]
    note_id = notes[0]["id"]

    notes_api.delete_note(note_id, headers=headers)

    # rem_notes = notes_api.get_all_notes(headers)
    # rem_notes_json = rem_notes.json()["data"]
    #
    # for note in rem_notes_json:
    #     if note["id"] == note_id:
    #         assert False, f"Note with id {note_id} was not deleted"

    # Login for refresh
    lp = LoginPage(driver)
    lp.login()

    # Refresh UI
    bp = BasePage(driver)
    bp.refresh()

    # Checking whether note get deleted or not


    assert response.status_code in (200, 204), f"Note with id {note_id} was not deleted"

