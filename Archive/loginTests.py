from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://membersgram.com/login-english/")
sleep(3)

login.enter_username("Admin")
login.enter_password("admin123")
login.click_on_login_button()
sleep(3)