from Pages.Login import Login
from selenium import webdriver
from time import sleep
from Pages.MainPage import MainPage
import unittest


class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test2(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_on_login_button()
        sleep(3)
        main_page.check_main_page()
        sleep(2)

    def test1(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        login.enter_username('Admin')
        login.enter_password('admin1235')
        login.click_on_login_button()
        sleep(3)
        main_page.check_main_page()
        sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
