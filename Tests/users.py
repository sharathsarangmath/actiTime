from lib2to3.pgen2 import driver

from selenium import webdriver
import unittest
import time
from Pages.loginPage import LoginPage


class UserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="/Users/sharathsarangmath/Desktop/Test_Automation_Projects/drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_add_dept(self):

        driver=self.driver
        driver.get("https://online.actitime.com/ssarangmath/login.do")

        lgn = LoginPage(driver)
        lgn.enter_username("sharathsarang@gmail.com")
        lgn.enter_pwd("Shar@8971")
        lgn.click_login()
        driver.implicitly_wait(10)
        time.sleep(3)

        #Verify successful login
        pageTitle = self.driver.title
        self.assertEqual("actiTIME - Enter Time-Track", pageTitle, "Login not success")

    def test_02_add_user(self):
        driver=self.driver
        #
        # driver.get("https://online.actitime.com/ssarangmath/login.do")
        #
        # lgn = LoginPage(driver)
        # lgn.enter_username("sharathsarang@gmail.com")
        # lgn.enter_pwd("Shar@8971")
        # lgn.click_login()
        # driver.implicitly_wait(10)
        # time.sleep(3)
        #
        # # Verify successful login
        # pageTitle = self.driver.title
        # self.assertEqual("actiTIME - Enter Time-Track", pageTitle, "Login not success")

        driver.find_element_by_xpath("//*[@id='topnav']/tbody/tr/td[5]/a").click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath("//*[@id='pageBody']/tbody/tr[1]/td[3]/div/div[3]").click()

        driver.find_element_by_id("createUserPanel_firstNameField").clear()
        driver.find_element_by_id("createUserPanel_firstNameField").send_keys("Sharath")

        driver.find_element_by_id("createUserPanel_lastNameField").clear()
        driver.find_element_by_id("createUserPanel_lastNameField").send_keys("Sarangmath")

        driver.find_element_by_id("createUserPanel_emailField").clear()
        driver.find_element_by_id("createUserPanel_emailField").send_keys("createUserPanel_emailField")






