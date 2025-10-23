import os

import extras
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from pages.login_page import LoginPage
#from pages.inventory_page import InventoryPage

# Logger Setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

@pytest.fixture(scope="session")
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('incognito')
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
    logger.info("Driver closed")

@pytest.fixture(scope="session")
def login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call, extras=None):
    """
        Take screenshot on test failure and attach it to pytest-html report.
        """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver=item.funcargs.get("driver",'none')
        if driver:
            os.makedirs("reports/screenshots",exist_ok=True)
            screenshot_path=os.path.join("reports/screenshots",f"{item.name}.png")
            driver.save_screenshot(screenshot_path)

            if hasattr(report,"extra"):
                from pytest_html import extras
                report.extra.append(extras.image(screenshot_path))

            else:
                report.extra = [extras.image(screenshot_path)]

