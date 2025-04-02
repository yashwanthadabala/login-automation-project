import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

CHROMEDRIVER_PATH = "C:\\chromedriver\\chromedriver.exe"

@pytest.fixture
def driver():
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Logged In Successfully" in driver.page_source

def test_login_failure(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Your username is invalid!" in driver.page_source
