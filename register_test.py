import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.register_page import RegisterPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, 750)")
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_create_account(driver):
    register_page = RegisterPage(driver)
    register_page.open_page("https://magento.softwaretestingboard.com/")
    time.sleep(1)
    register_page.click_register_page()
    time.sleep(1)
    register_page.enter_firstname("Andre")
    register_page.enter_lastname("Dwi Putra")
    register_page.enter_email("foxylos666@gmail.com")
    register_page.enter_password("Bukal666")
    register_page.enter_confirm_password("Bukal666")
    time.sleep(5)
    register_page.click_register()
    time.sleep(1)


    # assert "Successful" in driver.page_source
    # time.sleep(1)