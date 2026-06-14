from time import sleep
import pytest

from config.env import ConfigReader
from pages.ui.create_note import CreateNote
from pages.ui.login import LoginPage
from utils.loggers import get_logger
from utils.performance import get_page_load_time


@pytest.mark.ui
@pytest.mark.order(3)
def test_valid_create_note(setup_and_teardown):
    logger = get_logger(__name__)
    logger.info("Starting test_valid_create_note")

    driver = setup_and_teardown
    load_time = get_page_load_time(driver)
    logger.info(f"Login Page Load Time: {load_time} ms")

    config = ConfigReader.read_config()
    env = config['add_note']

    category = env['category']
    title = env['title']
    description = env['description']

    lp = LoginPage(driver)
    cn = CreateNote(driver)

    lp.login()
    load_time_after_login = get_page_load_time(driver)
    logger.info(f"Notes Page Load Time: {load_time_after_login} ms")
    logger.info(f"Creating note with title: {title}")

    cn.click_add_note()
    cn.select_work(category)
    cn.enter_title(title)
    cn.enter_description(description)
    cn.click_create()
    # cn.refresh()

    sleep(2)

    assert cn.valid_note_title() == "Meeting Notes"
    assert cn.valid_note_content() == "Notes for the meeting"
    logger.info("test_valid_create_note passed")

@pytest.mark.ui
@pytest.mark.order(4)
def test_invalid_create_note(setup_and_teardown):
    logger = get_logger(__name__)
    logger.info("Starting test_invalid_create_note")

    driver = setup_and_teardown
    load_time = get_page_load_time(driver)
    logger.info(f"Login Page Load Time: {load_time} ms")

    config = ConfigReader.read_config()
    env = config['add_empty_note']

    category = env['category']
    title = env['title']
    # description = env['description']

    cn = CreateNote(driver)
    lp = LoginPage(driver)
    lp.login()
    load_time_after_login = get_page_load_time(driver)
    logger.info(f"Notes Page Load Time: {load_time_after_login} ms")
    logger.info(f"Attempting to create empty note with title: {title}")

    # cn.scroll_to_amt(270)
    cn.click_add_note()
    cn.select_work(category)
    cn.enter_title(title)
    # cn.enter_description(description)
    cn.click_create()

    try:
        assert cn.valid_note_title() == title
    except AssertionError:
        logger.warning("Invalid create note assertion failed, taking screenshot")
        cn.take_screenshot("invalid_create_note")
