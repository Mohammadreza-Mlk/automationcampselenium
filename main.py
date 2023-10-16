from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

# browser Action 1 > Open web
driver.get("https://membersgram.com/")
sleep(1)

# browser Action 2 > viw title of  site
window_title = driver.title
print("Title = " + window_title)
sleep(1)

# browser Action 3 > go to Order
# driver.find_element('id','OrderNowNavForTagmanager').click()
# sleep(5)

# browser Action 4 > Refresh web
# driver.refresh()

# browser Action 5 > Open new window and switch to it(tab)
# driver.switch_to.new_window('tab')
# sleep(2)

# browser Action 6 > Open new window and switch to it(window)
# driver.switch_to.new_window('window')
# driver.get("https://google.com")
# sleep(2)

# browser Action 7 > Quite tab
# driver.close()
# sleep(2)

# browser Action 8 > what my driver size?
window_size = driver.get_window_size()
print(window_size)
width = window_size['width']
print("width = ", width)
height = window_size['height']
print('height = ', height)
# browser Action 9 > Set Window size
driver.set_window_size(1500,524)

size = driver.get_window_size()
print(size)
# assert size['width'] == 2000

# browser Action 10 > get Window size
current_position = driver.get_window_position()
print(current_position)
sleep(5)

# browser Action 11 > set Window size
driver.set_window_position(0,0)
sleep(2)

# browser Action 11 > minimize Window
driver.minimize_window()
sleep(2)
# browser Action 12 > maximize Window
driver.maximize_window()
sleep(2)

# browser Action 13 > full screen Window
driver.fullscreen_window()
sleep(2)

# browser Action 7 > Quite session
driver.quit()