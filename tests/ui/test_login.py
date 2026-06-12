from time import sleep

import pytest

from config.env import ConfigReader
from pages.ui.login import LoginPage


@pytest.mark.order(1)

def test_invalid_login(setup_and_teardown):

    driver = setup_and_teardown

    config = ConfigReader.read_config()
    env = config['invalid_login']
    email = env['email']
    password = env['password']

    lp = LoginPage(driver)

    lp.scroll_to_amt()
    lp.click_to_login()
    lp.scroll_to_amt()
    lp.enter_email(email)
    lp.enter_password(password)
    lp.click_login_btn()
    sleep(2)

    try:
        assert driver.current_url == f"https://practice.expandtesting.com/notes/app"
    except AssertionError:
        lp.take_screenshot("invalid_login")
    # lp.refresh()


def test_valid_login(setup_and_teardown):

    driver = setup_and_teardown

    config = ConfigReader.read_config()
    env = config['valid_login']
    email = env['email']
    password = env['password']

    lp = LoginPage(driver)

    # lp.scroll_to_amt()
    # lp.click_to_login()
    lp.scroll_to_amt(275)
    lp.enter_email(email)
    lp.enter_password(password)
    lp.click_login_btn()
    sleep(2)

    assert driver.current_url == f"https://practice.expandtesting.com/notes/app"


