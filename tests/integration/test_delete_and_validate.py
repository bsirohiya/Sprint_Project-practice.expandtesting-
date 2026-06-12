from pages.api.notes import NotesAPI
from pages.ui.base_page_ui import BasePage
from pages.ui.login import LoginPage
from pages.ui.create_note import CreateNote
from time import sleep

def test_delete_and_validate(setup_and_teardown, headers):

    driver = setup_and_teardown
    notes_api = NotesAPI()

    # Get all notes and store the note to be deleted
    response = notes_api.get_all_notes(headers)
    assert response.status_code == 200, f"Failed to fetch notes. Status code: {response.status_code}"

    response_json = response.json()
    notes = response_json["data"]
    assert len(notes) > 0, "No notes available to delete"

    # Store the note details to be deleted (both title and description to handle duplicates)
    note_to_delete = notes[0]
    note_id = note_to_delete["id"]
    note_title = note_to_delete["title"]
    note_description = note_to_delete.get("description", "")

    # Count occurrences of this (title, description) pair in API before deletion
    api_count_before = sum(1 for n in notes if n.get("title") == note_title and n.get("description", "") == note_description)

    # Login to access UI
    lp = LoginPage(driver)
    lp.login()
    sleep(2)

    # Count occurrences of (title, description) pair in UI before deletion
    cn = CreateNote(driver)
    ui_count_before = cn.count_note_by_title_desc(note_title, note_description)

    # Delete the note via API
    delete_response = notes_api.delete_note(note_id, headers=headers)
    assert delete_response.status_code in (200, 204), f"Failed to delete note. Status code: {delete_response.status_code}"

    # Verify deletion via API - count should decrease by 1
    remaining_notes = notes_api.get_all_notes(headers)
    remaining_notes_json = remaining_notes.json()["data"]
    api_count_after = sum(1 for n in remaining_notes_json if n.get("title") == note_title and n.get("description", "") == note_description)

    assert api_count_after == api_count_before - 1, \
        f"API: Note (title='{note_title}', desc='{note_description}') count did not decrease by 1. Before: {api_count_before}, After: {api_count_after}"

    # Refresh UI to get latest data
    bp = BasePage(driver)
    bp.refresh()
    sleep(2)

    # Verify deletion in UI - count should decrease by 1
    ui_count_after = cn.count_note_by_title_desc(note_title, note_description)

    assert ui_count_after == ui_count_before - 1, \
        f"UI: Note (title='{note_title}', desc='{note_description}') count did not decrease by 1. Before: {ui_count_before}, After: {ui_count_after}"

