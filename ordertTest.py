from selenium import webdriver
from selenium.webdriver.common.by import By

#agar chromdriver tidak close sendiri
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.implicitly_wait(50)

driver.get("https://magento.softwaretestingboard.com/")

#Login
login = driver.find_element(By.LINK_TEXT, "Sign In")
login.click()
emailInput = driver.find_element(By.ID, "email")
emailInput.send_keys("andredwiputra0413@gmail.com")
passInput = driver.find_element(By.ID, "pass")
passInput.send_keys("Password_123")
buttonSignin = driver.find_element(By.ID, "send2")
buttonSignin.click()

#checkout product
product = driver.find_element(By.LINK_TEXT, "Argus All-Weather Tank")
product.click()
sizeProduct = driver.find_element(By.ID, "option-label-size-143-item-166")
sizeProduct.click()
colourProduct = driver.find_element(By.ID, "option-label-color-93-item-52")
colourProduct.click()
quantity = driver.find_element(By.ID, "qty")
quantity.clear()
quantity.send_keys('5')
addCart = driver.find_element(By.ID, "product-addtocart-button")
addCart.click()
showCart = driver.find_element(By.LINK_TEXT, "shopping cart")
showCart.click()
checkout = driver.find_element(By.XPATH, "//span[contains(text(),'Proceed to Checkout')]")
checkout.click()