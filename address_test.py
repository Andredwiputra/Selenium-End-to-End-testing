import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.address_page import AddressPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_address_page(driver):
    register_page = RegisterPage(driver)
    login_page = LoginPage(driver)
    address_page = AddressPage(driver)
    register_page.open_page("https://magento.softwaretestingboard.com/")
    time.sleep(1)
    login_page.click_login_page()
    time.sleep(1)
    login_page.enter_email("foxylos666@gmail.com")
    login_page.enter_password("Bukal666")
    time.sleep(5)
    login_page.click_login()
    time.sleep(1)
    address_page.click_dropdown()
    time.sleep(1)
    address_page.click_user_profile()
    time.sleep(1)
    address_page.click_address()
    time.sleep(1)
    address_page.enter_company("Satu Jaya")
    address_page.enter_phone("08123546545")
    address_page.enter_address1("Ayani Street")
    address_page.enter_city("Denpasar")
    address_page.click_region()
