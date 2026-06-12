import pytest

from config.env import ConfigReader
from pages.api.notes import NotesAPI
from pages.ui.create_note import CreateNote
from pages.ui.login import LoginPage


@pytest.mark.order(4)

def test_validate_note(headers, setup_and_teardown):

    driver = setup_and_teardown
    create_note = CreateNote(driver)
    lp = LoginPage(driver)

    config = ConfigReader.read_config()
    env = config["add_note_validate"]
    category = env["category"]
    title = env["title"]
    description = env["description"]

    lp.login()

    create_note.click_add_note()
    create_note.select_work(category)
    create_note.enter_title(title)
    create_note.enter_description(description)
    create_note.click_create()

    note_api = NotesAPI()

    response = note_api.get_all_notes(headers)

    # assert response.status_code == 200

    notes = response.json()["data"]

    matched = False

    for i in notes:
        if i["title"] == title and i["description"] == description:
            matched = True
            assert matched == True
            break

    assert matched == True, "Not equal"

