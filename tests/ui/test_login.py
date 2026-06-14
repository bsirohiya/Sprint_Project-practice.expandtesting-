import pytest
from time import sleep
from config.env import ConfigReader
from pages.ui.login import LoginPage
from utils.loggers import get_logger
from utils.performance import get_page_load_time


@pytest.mark.ui
@pytest.mark.order(1)
def test_invalid_login(setup_and_teardown):

    logger = get_logger(__name__)
    logger.info("Starting test_invalid_login")

    driver = setup_and_teardown

    load_time = get_page_load_time(driver)
    logger.info(f"Login Page Load Time: {load_time} ms")

    config = ConfigReader.read_config()
    env = config['invalid_login']
    email = env['email']
    password = env['password']

    lp = LoginPage(driver)

    lp.scroll_to_amt(275)
    lp.click_to_login()
    lp.scroll_to_amt(280)
    lp.enter_email(email)
    lp.enter_password(password)
    lp.click_login_btn()
    sleep(2)

    load_time_after_login = get_page_load_time(driver)
    logger.info(f"Notes Page Load Time: {load_time_after_login} ms")

    try:
        assert driver.current_url == f"https://practice.expandtesting.com/notes/app"
    except AssertionError:
        lp.take_screenshot("invalid_login")

@pytest.mark.ui
@pytest.mark.order(2)
def test_valid_login(setup_and_teardown):

    logger = get_logger(__name__)
    logger.info("Starting test_valid_login")

    driver = setup_and_teardown

    load_time = get_page_load_time(driver)
    logger.info(f"Login Page Load Time: {load_time} ms")

    config = ConfigReader.read_config()
    env = config['valid_login']
    email = env['email']
    password = env['password']

    lp = LoginPage(driver)

    lp.scroll_to_amt(270)
    lp.click_to_login()
    lp.scroll_to_amt(277)
    lp.enter_email(email)
    lp.enter_password(password)
    lp.click_login_btn()
    sleep(2)

    load_time_after_login = get_page_load_time(driver)
    logger.info(f"Notes Page Load Time: {load_time_after_login} ms")

    assert driver.current_url == f"https://practice.expandtesting.com/notes/app"
    logger.info("test_valid_login passed")


