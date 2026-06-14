import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from config.env import ConfigReader

@pytest.fixture(scope="function")
def setup_and_teardown():
    """
    Set up and tear down Selenium WebDriver for UI tests.

    NOTE: Run UI tests with limited parallelization (--n 1 or -n 2 max).
    Too many concurrent browsers cause resource exhaustion and UI failures.
    """

    config = ConfigReader.read_config()
    env = config['qa']
    base_url_ui = env['base_url_ui']

    o = ChromeOptions()
    o.add_argument("--disable-notifications")
    o.add_argument("--disable-gpu")  # Disable GPU for stability
    o.add_argument("--no-sandbox")   # Disable sandbox

    driver = webdriver.Chrome(options=o)
    driver.maximize_window()
    driver.implicitly_wait(10)  # Implicit wait for element discovery
    driver.get(base_url_ui)

    yield driver

    driver.quit()

