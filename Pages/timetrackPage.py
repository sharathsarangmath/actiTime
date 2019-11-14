class TimeTrackPage():

    def __init__(self,driver):
        self.driver = driver

        self.logout_link_text = "Logout"

    def logout(self):
        self.driver.find_element_by_link_text(self.logout_link_text ).click()
