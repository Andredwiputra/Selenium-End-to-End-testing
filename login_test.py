import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.register_page import RegisterPage
from pages.login_page import LoginPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_login_page(driver):
    register_page = RegisterPage(driver)
    login_page = LoginPage(driver)
    register_page.open_page("https://magento.softwaretestingboard.com/")
    time.sleep(1)
    login_page.click_login_page()
    time.sleep(1)
    login_page.enter_email("foxylos666@gmail.com")
    login_page.enter_password("Bukal666")
    time.sleep(5)
    login_page.click_login()
    time.sleep(1)