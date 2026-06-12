from selenium.webdriver.common.by import By
from pages.ui.base_page_ui import BasePage

class EditNote(BasePage):

    edit_btn = (By.XPATH, '(//button[@data-testid="note-edit"])[2]')
    title = (By.XPATH, '//input[@id="title"]')
    description = (By.XPATH, '//textarea[@id="description"]')
    category = (By.XPATH, '//select[@id="category"]')
    save = (By.XPATH, '//button[.="Save"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_edit_btn(self):
        self.click(self.edit_btn)

    def select_home(self, home):
        self.select_dropdown(self.category, home)

    def enter_title(self, title):
        self.enter_text(self.title, title)

    def enter_description(self, description):
        self.enter_text(self.description, description)

    def click_save(self):
        self.click(self.save)
