class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "username"
        self.pwd_textbox_name = "pwd"
        self.login_btn_id = "loginButton"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_pwd(self,password):
        self.driver.find_element_by_name(self.pwd_textbox_name).clear()
        self.driver.find_element_by_name(self.pwd_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_btn_id ).click()

    def invalid_err_msg(self):
        msg=self.driver.find_element_by_xpath("//*[@id='ErrorsTable']/tbody/tr/td[2]/table/tbody/tr/td/span").text
        return msg




