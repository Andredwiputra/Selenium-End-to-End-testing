from selenium.webdriver.common.by import By

class AddressPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.dropdown_button = (By.XPATH, "//button[@class='action switch']")
        self.user_profile = (By.LINK_TEXT, "My Account")
        self.address = (By.LINK_TEXT, "Manage Addresses")
        self.company_textbox = (By.ID, "company")
        self.phone_textbox = (By.ID, "telephone")
        self.street_address1 = (By.ID, "street_1")
        self.city_textbox = (By.ID, "city")
        self.region_dropdown = (By.ID, "region_id")
        self.zip_textbox = (By.ID, "zip")
        self.country_dropdown = (By.ID, "country")
        self.save_button = (By.XPATH, "//span[contains(text(),'Save Address')]")
    
    def click_dropdown(self):
        self.driver.find_element(*self.dropdown_button).click()
    
    def click_user_profile(self):
        self.driver.find_element(*self.user_profile).click()

    def click_address(self):
        self.driver.find_element(*self.address).click()
    
    def enter_company(self, company):
        self.driver.find_element(*self.company_textbox).send_keys(company)
    
    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_textbox).send_keys(phone)

    def enter_address1(self, address1):
        self.driver.find_element(*self.street_address1).send_keys(address1)
    
    def enter_city(self, city):
        self.driver.find_element(*self.city_textbox).send_keys(city)
    
    def click_region(self):
        self.driver.find_element(*self.region_dropdown).click()