import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

chromedriver_autoinstaller.install()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_search(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium WebDriver" + Keys.RETURN)
    print("driver.title == " + driver.title)
    #time.sleep(10)
    assert "Selenium+WebDriver" in driver.title
