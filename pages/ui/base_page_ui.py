from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import os

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # UI functions

    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def hover_to(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scroll_to(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element).perform()

    def scroll_to_amt(self, y):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(0, y).perform()

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_to_iframe(self, locator):
        iframe = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.switch_to.frame(iframe)

    def select_dropdown(self, locator, value):
        dropdown = self.wait.until(EC.visibility_of_element_located(locator))
        option = Select(dropdown)
        option.select_by_value(value)

    def refresh(self):
        self.driver.refresh()

    def validate_note(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def take_screenshot(self, name):
        folder = os.path.join(os.getcwd(), "screenshots")  # To create folder
        os.makedirs(folder, exist_ok=True)
        self.driver.save_screenshot(f"{folder}/screenshot_{name}.png")
