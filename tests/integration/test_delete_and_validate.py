import pytest
from time import sleep, time

from config.env import ConfigReader
from pages.api.notes import NotesAPI
from pages.ui.login import LoginPage
from pages.ui.create_note import CreateNote
from pages.ui.base_page_ui import BasePage
from utils.loggers import get_logger
from utils.performance import get_page_load_time


@pytest.mark.integration
@pytest.mark.order(13)
def test_delete_and_validate(setup_and_teardown, headers):

    logger = get_logger(__name__)
    logger.info("Starting test_delete_and_validate")

    driver = setup_and_teardown

    load_time = get_page_load_time(driver)
    logger.info(f"Login Page Load Time: {load_time} ms")

    # Read test data
    config = ConfigReader.read_config()
    note_data = config["delete_note"]

    note_title = f"Note to be deleted_{int(time())}"
    note_description = note_data["description"]
    note_category = note_data["category"]

    logger.info(f"Creating test note with title: {note_title}")

    # Login
    lp = LoginPage(driver)
    lp.login()

    load_time_after_login = get_page_load_time(driver)
    logger.info(f"Notes Page Load Time: {load_time_after_login} ms")
    logger.info("User logged in successfully")

    # Create note using UI
    cn = CreateNote(driver)

    cn.click_add_note()
    cn.enter_title(note_title)
    cn.enter_description(note_description)
    cn.select_work(note_category)
    cn.click_create()

    logger.info("Note created via UI")

    sleep(2)

    # Verify note created in UI
    assert cn.is_note_present(note_title)
    logger.info("Note verified in UI")

    # Find note through API
    notes_api = NotesAPI()

    response = notes_api.get_all_notes(headers)
    assert response.status_code == 200
    logger.info("Fetched all notes via API")

    notes = response.json()["data"]

    note_id = None

    for note in notes:
        if note["title"] == note_title:
            note_id = note["id"]
            break

    assert note_id is not None, "Created note not found through API"
    logger.info(f"Note found in API with ID: {note_id}")

    # Delete note using API
    delete_response = notes_api.delete_note(note_id, headers)

    assert delete_response.status_code in (200, 204)
    logger.info(f"Note deleted via API, status: {delete_response.status_code}")

    # Refresh UI
    BasePage(driver).refresh()
    sleep(3)
    logger.info("UI refreshed")

    # Verify note deleted in UI
    assert not cn.is_note_present(note_title), \
        f"Note '{note_title}' is still visible after deletion"
    logger.info("Note verified as deleted in UI")
    logger.info("test_delete_and_validate passed")
