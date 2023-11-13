from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from pathlib import Path

driver = webdriver.Chrome()

driver.get("http://192.168.1.186:3000/Login")
sleep(3)

driver.find_element('id', "outlined-basic").click()
driver.find_element('id', "outlined-basic").send_keys('hllo@gmail.com')
driver.find_element('id', "password").click()
driver.find_element('id', "password").send_keys("1212121212")
driver.find_element('xpath', "//button[text()='Login']").click()
sleep(10)