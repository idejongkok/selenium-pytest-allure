from selenium.webdriver.common.by import By
import json

with open("config/locators.json") as f:
    locators = json.load(f)


class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, locators["login"]["input_usrname"]).send_keys(
            username
        )

    def enter_password(self, password):
        self.driver.find_element(By.NAME, locators["login"]["input_pw"]).send_keys(
            password
        )

    def click_login(self):
        self.driver.find_element(By.XPATH, locators["login"]["button_login"]).click()


class Alert:
    def __init__(self, driver):
        self.driver = driver

    def invalid_credential_alert(self):
        alert = self.driver.find_element(
            By.XPATH, locators["login"]["text_invalid_credential"]
        )
        status = alert.is_displayed()

        return status
