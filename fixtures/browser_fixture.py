import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from config.env import ConfigReader

@pytest.fixture(scope="session")
def setup_and_teardown():

    config = ConfigReader.read_config()
    env = config['qa']
    base_url_ui = env['base_url_ui']

    o = ChromeOptions()
    o.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=o)
    driver.maximize_window()
    driver.get(base_url_ui)

    yield driver

    input("Press enter to close the browser")
    driver.quit()