from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from pathlib import Path

driver = webdriver.Chrome()
driver.maximize_window()
sleep(5)

driver.get("https://membersgram.com/")
sleep(5)

elem1 = driver.find_element('xpath', "//*[text()='Blog']")
elem1.click()
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
current_path = Path(__file__).parent
file_name = os.path.join(str(current_path), 'session2.png')
driver.save_screenshot(file_name)
