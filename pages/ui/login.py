from time import sleep

from selenium.webdriver.common.by import By

from config.env import ConfigReader
from pages.ui.base_page_ui import BasePage

class LoginPage(BasePage):

    to_login = (By.XPATH, '//a[.="Login"]')
    email = (By.XPATH, '//input[@id="email"]')
    password = (By.XPATH, '//input[@id="password"]')
    login_btn = (By.XPATH, '//button[.="Login"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_to_login(self):
        self.click(self.to_login)

    def enter_email(self, email):
        self.enter_text(self.email, email)

    def enter_password(self, password):
        self.enter_text(self.password, password)

    def click_login_btn(self):
        self.click(self.login_btn)

    def login(self):

        config = ConfigReader.read_config()
        env = config['valid_login']
        email = env['email']
        password = env['password']

        sleep(2)
        self.scroll_to_amt(270)
        self.click_to_login()
        self.scroll_to_amt(265)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_btn()
        sleep(2)