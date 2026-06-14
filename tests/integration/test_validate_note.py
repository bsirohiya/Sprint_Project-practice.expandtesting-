import pytest

from config.env import ConfigReader
from pages.api.notes import NotesAPI
from pages.ui.create_note import CreateNote
from pages.ui.login import LoginPage
from utils.loggers import get_logger
from utils.performance import get_page_load_time


@pytest.mark.integration
@pytest.mark.order(14)
def test_validate_note(headers, setup_and_teardown):

    logger = get_logger(__name__)
    logger.info("Starting test_validate_note")

    driver = setup_and_teardown

    load_time = get_page_load_time(driver)
    logger.info(f"Login Page Load Time: {load_time} ms")

    create_note = CreateNote(driver)
    lp = LoginPage(driver)

    config = ConfigReader.read_config()
    env = config["add_note_validate"]
    category = env["category"]
    title = env["title"]
    description = env["description"]

    logger.info(f"Creating and validating note with title: {title}")

    lp.login()

    load_time_after_login = get_page_load_time(driver)
    logger.info(f"Notes Page Load Time: {load_time_after_login} ms")

    create_note.click_add_note()
    create_note.select_work(category)
    create_note.enter_title(title)
    create_note.enter_description(description)
    create_note.click_create()
    logger.info("Note created via UI")

    note_api = NotesAPI()

    response = note_api.get_all_notes(headers)
    logger.info(f"Fetched notes via API, status: {response.status_code}")

    # assert response.status_code == 200

    notes = response.json()["data"]

    matched = False

    for i in notes:
        if i["title"] == title and i["description"] == description:
            matched = True
            assert matched == True
            logger.info(f"Note found in API response with ID: {i['id']}")
            logger.info("test_validate_note passed")
            break

    assert matched == True, "Can't find pair of title + desc note in API response"


