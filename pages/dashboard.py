from selenium.webdriver.common.by import By
import json

with open("config/locators.json") as f:
    locators = json.load(f)


class Dashboard:
    def __init__(self, driver):
        self.driver = driver

    def dashboard_title_text(self):
        title = self.driver.find_element(
            By.TAG_NAME, locators["dashboard"]["text_title"]
        ).text

        return title
