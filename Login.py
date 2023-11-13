class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"


    def enter_username(self, username):
        self.driver.find('id', self.username_textbox_id).click()
        self.driver.find('name', self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find('id', self.password_textbox_id).click()
        self.driver.find('id', self.password_textbox_id).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element('id', self.login_button_id).click()