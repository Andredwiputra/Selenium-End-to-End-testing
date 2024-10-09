from selenium import webdriver
from selenium.webdriver.common.by import By

#agar chromdriver tidak close sendiri
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://magento.softwaretestingboard.com/")

#sign-up
signupClick = driver.find_element(By.LINK_TEXT, "Create an Account")
signupClick.click()
inputFirstname = driver.find_element(By.ID, "firstname")
inputFirstname.send_keys("Andre")
inputLastname = driver.find_element(By.ID, "lastname")
inputLastname.send_keys("Dwi Putra")
inputEmail = driver.find_element(By.ID, "email_address")
inputEmail.send_keys("andredwiputra0413@gmail.com")
inputPass = driver.find_element(By.ID, "password")
inputPass.send_keys("Bukal666")
inputConfirm = driver.find_element(By.ID, "password-confirmation")
inputConfirm.send_keys("Bukal666")
buttonSubmit = driver.find_element(By.XPATH, "//span[contains(text(),'Create an Account')]")
buttonSubmit.click()