from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from pathlib import Path

driver = webdriver.Chrome()

# browser Action 1 > Open web
driver.get("https://membersgram.com/")
sleep(1)
driver.set_window_size(1000,768)
sleep(3)
driver.find_element('id', 'Blog').click()
sleep(3)
driver.set_window_size(1920,768)
sleep(2)

current_path = Path(__file__).parent
file_name = os.path.join(str(current_path), 'session3.png')
driver.save_screenshot(file_name)


driver.set_window_size(1366,768)
sleep(2)

current_path = Path(__file__).parent
file_name = os.path.join(str(current_path), 'session2.png')
driver.save_screenshot(file_name)

sleep(2)

driver.set_window_size(360,768)
sleep(2)

current_path = Path(__file__).parent
file_name = os.path.join(str(current_path), 'session1.png')
driver.save_screenshot(file_name)

