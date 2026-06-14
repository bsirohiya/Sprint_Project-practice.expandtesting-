from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.ui.base_page_ui import BasePage

class CreateNote(BasePage):

    add_note = (By.XPATH, '//button[.="+ Add Note"]')
    title = (By.XPATH, '//input[@id="title"]')
    description = (By.XPATH, '//textarea[@id="description"]')
    create = (By.XPATH, '//button[.="Create"]')
    category = (By.XPATH, '//select[@id="category"]')
    valid_note_title_text = (By.XPATH, '//div[@data-testid="note-card-title"]')
    valid_note_desc = (By.XPATH, '//p[@class="card-text"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_add_note(self):
        self.click(self.add_note)

    def select_work(self, work):
        self.select_dropdown(self.category,work)

    def enter_title(self, title):
        self.enter_text(self.title, title)

    def enter_description(self, description):
        self.enter_text(self.description, description)

    def click_create(self):
        self.click(self.create)

    def valid_note_content(self):
        return self.validate_note(self.valid_note_desc)

    def valid_note_title(self):
        return self.validate_note(self.valid_note_title_text)

    def is_note_present(self, title):
        titles = self.driver.find_elements(*self.valid_note_title_text)

        for note in titles:
            if note.text.strip() == title:
                return True

        return False