from time import sleep

from config.env import ConfigReader
from pages.ui.create_note import CreateNote
from pages.ui.edit_note import EditNote
from pages.ui.login import LoginPage


def test_valid_edit_note(setup_and_teardown):

    driver = setup_and_teardown

    config = ConfigReader.read_config()["edit_valid_note"]
    title = config["title"]
    description = config["description"]
    category = config["category"]

    lp = LoginPage(driver)
    lp.login()

    en = EditNote(driver)
    sleep(2)
    en.scroll_to_amt(330)
    en.click_edit_btn()
    en.select_home(category)
    en.enter_title(title)
    en.enter_description(description)
    en.click_save()

def test_invalid_edit_note(setup_and_teardown):

    driver = setup_and_teardown

    config = ConfigReader.read_config()["edit_invalid_note"]
    title = config["title"]
    description = config["description"]
    category = config["category"]

    # lp = LoginPage(driver)
    # lp.login()

    en = EditNote(driver)
    sleep(2)
    en.scroll_to_amt(325)
    en.click_edit_btn()
    en.select_home(category)
    en.enter_title(title)
    en.enter_description(description)
    en.click_save()

    cn = CreateNote(driver)

    try:
        assert cn.valid_note_title() == ""
    except AssertionError:
        en.take_screenshot("invalid_edit_note")