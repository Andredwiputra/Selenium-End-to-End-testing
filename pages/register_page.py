from selenium.webdriver.common.by import By


class RegisterPage :
    
    def __init__(self, driver):
        self.driver = driver
        self.create_account = (By.LINK_TEXT, "Create an Account")
        self.firstname_textbox = (By.ID, "firstname")
        self.lastname_textbox = (By.ID, "lastname")
        self.email_textbox = (By.ID, "email_address")
        self.password_textbox = (By.ID, "password")
        self.confirmpass_textbox = (By.ID, "password-confirmation")
        self.create_account_button = (By.XPATH, "//span[contains(text(),'Create an Account')]")

    def open_page(self, url):
        self.driver.get(url)

    def click_register_page(self):
        self.driver.find_element(*self.create_account).click()

    def enter_firstname(self, firstname):
        self.driver.find_element(*self.firstname_textbox).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(*self.lastname_textbox).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.confirmpass_textbox).send_keys(confirm_password)
    
    def click_register(self):
        self.driver.find_element(*self.create_account_button).click()


    