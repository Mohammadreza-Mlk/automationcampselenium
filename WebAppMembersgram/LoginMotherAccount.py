from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get("http://192.168.1.186:3000/Login")
sleep(2)

EmailBOx = driver.find_element('id', "outlined-basic")
PasswordBox = driver.find_element('id', "password")
loginButton = driver.find_element('xpath', "//button[text()='Login']")

# ############## Email & password is incorrect


EmailBOx.click()
EmailBOx.send_keys('incorrect@gmail.com')
PasswordBox.click()
PasswordBox.send_keys("1212121212")
loginButton.click()
sleep(5)

# ############## ٍEmail correct & password is incorrect
EmailBOx_Error = driver.find_element('xpath', "//input[@id='outlined-error-helper-text']")
EmailBOx_Error.click()

EmailBOx_Error.send_keys(Keys.BACKSPACE)

EmailBOx_Error.send_keys(Keys.CONTROL + "a")

EmailBOx_Error.send_keys("testphoenixmlk@gmail.com")
sleep(2)

loginButton.click()

sleep(3)
# ############## ٍEmail  & password is correct
sleep(10)