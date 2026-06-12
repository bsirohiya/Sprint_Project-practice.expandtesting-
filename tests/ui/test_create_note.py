from time import sleep
from pages.ui import login
import pytest

from config.env import ConfigReader
from pages.ui.create_note import CreateNote
from pages.ui.login import LoginPage


@pytest.mark.order(2)

def test_valid_create_note(setup_and_teardown):

    driver = setup_and_teardown

    config = ConfigReader.read_config()
    env = config['add_note']

    category = env['category']
    title = env['title']
    description = env['description']

    lp = LoginPage(driver)
    cn = CreateNote(driver)

    lp.login()
    cn.click_add_note()
    cn.select_work(category)
    cn.enter_title(title)
    cn.enter_description(description)
    cn.click_create()
    # cn.refresh()

    sleep(2)

    assert cn.valid_note_title() == "Meeting Notes", "Note not created / title not found"
    assert cn.valid_note_content() == "Notes for the meeting", "Note not created / description not found"


def test_invalid_create_note(setup_and_teardown):

    driver = setup_and_teardown

    config = ConfigReader.read_config()
    env = config['add_empty_note']

    category = env['category']
    title = env['title']
    # description = env['description']

    cn = CreateNote(driver)

    sleep(2)
    cn.click_add_note()
    cn.select_work(category)
    cn.enter_title(title)
    # cn.enter_description(description)
    cn.click_create()
    # cn.refresh()

    try:
        assert cn.valid_note_title() == ""
    except AssertionError:
        cn.take_screenshot("invalid_create_note")
