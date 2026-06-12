from selenium.webdriver.common.by import By

from pages.ui.base_page_ui import BasePage


class DeleteNote(BasePage):

    delete_btn = (By.XPATH, '(//button[@data-testid="note-delete"])[3]')
    confirm_delete_btn = (By.XPATH, '//button[@data-testid="note-delete-confirm"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_delete_btn(self):
        self.click(self.delete_btn)

    def click_confirm_delete_btn(self):
        self.click(self.confirm_delete_btn)