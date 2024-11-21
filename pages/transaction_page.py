from selenium.webdriver.common.by import By

class TransactionPage:

    def __init__(self, driver):
        self.driver = driver
        self.product_name = (By.LINK_TEXT, "Argus All-Weather Tank")
        self.product_size = (By.XPATH, "//div[@id='option-label-size-143-item-166']")
        self.product_colour = (By.XPATH, "//div[@id='option-label-color-93-item-52']")
        self.product_qty = (By.XPATH, "//input[@id='qty']")
        self.button_cart = (By.XPATH, "//span[contains(text(),'Add to Cart')]")
        self.cart = (By.XPATH, "//span[@class='counter-number']")
        self.button_checkout = (By.XPATH, "//button[@id='top-cart-btn-checkout']")
        self.button_next = (By.XPATH, "//span[contains(text(),'Next')]")
        self.button_order = (By.XPATH, "//span[contains(text(),'Place Order')]")
        


    def click_product(self):
        self.driver.find_element(*self.product_name).click()
    
    def click_size(self):
        self.driver.find_element(*self.product_size).click()

    def click_colour(self):
        self.driver.find_element(*self.product_colour).click()
    
    def input_qty(self, qty):
        self.driver.find_element(*self.product_qty).clear()
        self.driver.find_element(*self.product_qty).send_keys(qty)

    def input_cart(self):
        self.driver.find_element(*self.button_cart).click()

    def select_cart(self):
        self.driver.find_element(*self.cart).click()

    def click_checkout(self):
        self.driver.find_element(*self.button_checkout).click()

    def click_next(self):
        self.driver.find_element(*self.button_next).click()

    def click_order(self):
        self.driver.find_element(*self.button_order).click()