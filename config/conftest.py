from selenium import webdriver
import allure


def init_driver():
    # Initialize WebDriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--log-level=3")
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(30)
    # driver.maximize_window()

    return driver


class Head:
    def __init__(self, title, desc, name, feature):
        self.title = title
        self.desc = desc
        self.name = name
        self.feature = feature

    def label(self):
        allure.dynamic.title(self.title)
        allure.dynamic.description(self.desc)
        # allure.dynamic.tag("Smoke Test", "Authentication", "Regression")
        # allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.label("owner", self.name)
        allure.dynamic.feature(self.feature)
