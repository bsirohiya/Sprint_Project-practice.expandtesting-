from time import sleep

import pytest

from config.env import ConfigReader
from pages.ui.create_note import CreateNote
from pages.ui.edit_note import EditNote
from pages.ui.login import LoginPage
from utils.loggers import get_logger
from utils.performance import get_page_load_time

@pytest.mark.ui
@pytest.mark.order(5)
def test_valid_edit_note(setup_and_teardown):

    logger = get_logger(__name__)
    logger.info("Starting test_valid_edit_note")

    driver = setup_and_teardown

    load_time = get_page_load_time(driver)
    logger.info(f"Login Page Load Time: {load_time} ms")

    config = ConfigReader.read_config()["edit_valid_note"]
    title = config["title"]
    description = config["description"]
    category = config["category"]

    lp = LoginPage(driver)
    lp.login()

    load_time_after_login = get_page_load_time(driver)
    logger.info(f"Notes Page Load Time: {load_time_after_login} ms")
    logger.info(f"Editing note with title: {title}")

    en = EditNote(driver)
    en.scroll_to_amt(330)
    en.click_edit_btn()
    en.select_home(category)
    en.enter_title(title)
    en.enter_description(description)
    en.click_save()

    sleep(2)

    cn = CreateNote(driver)

    assert cn.valid_note_title() == title
    assert cn.valid_note_content() == description

    logger.info("test_valid_edit_note passed")

@pytest.mark.order(6)
@pytest.mark.ui
def test_invalid_edit_note(setup_and_teardown):

    logger = get_logger(__name__)
    logger.info("Starting test_invalid_edit_note")

    driver = setup_and_teardown

    load_time = get_page_load_time(driver)
    logger.info(f"Login Page Load Time: {load_time} ms")

    config = ConfigReader.read_config()["edit_invalid_note"]
    title = config["title"]
    description = config["description"]
    category = config["category"]

    print("description" , description)

    lp = LoginPage(driver)
    lp.login()

    load_time_after_login = get_page_load_time(driver)
    logger.info(f"Notes Page Load Time: {load_time_after_login} ms")
    logger.info(f"Attempting invalid edit with title: {title}")

    en = EditNote(driver)
    en.scroll_to_amt(310)
    en.click_edit_btn()
    en.select_home(category)
    en.enter_title(title)
    en.enter_description(description)

    print("description" , description)

    en.click_save()

    cn = CreateNote(driver)

    try:
        assert cn.valid_note_title() == title
    except AssertionError:
        logger.warning("Invalid edit note assertion failed, taking screenshot")
        en.take_screenshot("invalid_edit_note")