from selenium.webdriver.common.by import By

class LoginPage :

    def __init__(self, driver):
        self.driver = driver
        self.login_account = (By.LINK_TEXT, "Sign In")
        self.email_textbox = (By.ID, "email")
        self.password_textbox = (By.ID, "pass")
        self.login_button = (By.ID, "send2")

    def click_login_page(self):
        self.driver.find_element(*self.login_account).click()

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.login_button).click()