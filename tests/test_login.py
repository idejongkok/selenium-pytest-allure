import pytest
import allure
import os
from dotenv import load_dotenv, find_dotenv
from config.conftest import init_driver, Head
from pages.login import *
from pages.dashboard import *

load_dotenv(find_dotenv("config/.env"))
url = os.environ.get("MAIN_URL")
username = os.environ.get("USRNAME")
password = os.environ.get("PSWD")


@pytest.fixture
@allure.title("Initialize driver")
def browser():
    driver = init_driver()

    yield driver

    png_bytes = driver.get_screenshot_as_png()
    allure.attach(
        png_bytes, name="Screenshot", attachment_type=allure.attachment_type.PNG
    )
    driver.quit()


def test_login_positive(browser):
    allure_head = Head(
        title="As an user, I should be able to login with correct username and password",
        desc="This test attempts to log into the website using a username and a password",
        name="Aria Suseno",
        feature="Login",
    )
    allure_head.label()
    allure.dynamic.tag("Smoke Test", "Regression")

    with allure.step("I open OrangeHRM web apps"):
        browser.get(url)

    login = Login(browser)
    dashboard = Dashboard(browser)

    with allure.step("I input correct Username"):
        login.enter_username(username)
        
    with allure.step("I input correct Password"):
        login.enter_password(password)
        
    with allure.step("I click Login Button"):
        login.click_login()
        
    with allure.step("I should go to dashboard page"):
        title = dashboard.dashboard_title_text()
        assert title == "Dashboard"
        assert "OrangeHRM" in browser.title


wrong_data_input = [
    ("invalid_username", "admin123", True),
    ("Admin", "admin123", True),
    ("invalid_username", "invalid_password", True),
]


@pytest.mark.parametrize("username, password, alert_status", wrong_data_input)
def test_login_negative(browser, username, password, alert_status):
    allure_head = Head(
        title="As an user, I should not be able to login with wrong username and or password",
        desc="This test attempts to log into the website using a username and a password",
        name="Aria Suseno",
        feature="Login",
    )
    allure_head.label()
    allure.dynamic.tag("Smoke Test", "Regression")

    with allure.step("I open OrangeHRM web apps"):
        browser.get(url)

    login = Login(browser)
    with allure.step("I Input Username"):
        login.enter_username(username)

    with allure.step("I Input Password"):
        login.enter_password(password)

    with allure.step("I Click Login Button"):
        login.click_login()

    alert = Alert(browser)
    with allure.step("I see the alert for Invalid credential appeared"):
        assert alert.invalid_credential_alert() == alert_status
