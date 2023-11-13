from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from pathlib import Path

driver = webdriver.Chrome()

driver.get("https://newpanel.membersgram.com/Register")


driver.find_element('id', "outlined-basic").click()
driver.find_element('id', "outlined-basic").send_keys('h21l12lo@gmail.com')

sleep(1)
driver.find_element('xpath', "//*[text()='Next']").click()
sleep(2)


driver.find_element('id', "password").click()
driver.find_element('id', "password").send_keys("1212121212")

sleep(1)

driver.find_element('id', "Confirmpassword").click()
driver.find_element('id', "Confirmpassword").send_keys("1212121212")

driver.find_element('xpath', "//input[@class='PrivateSwitchBase-input css-1m9pwf3']").click()

driver.find_element('xpath', "//button[text()='Register']").click()

sleep(30)
