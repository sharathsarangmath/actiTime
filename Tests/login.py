from selenium import webdriver
import time
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.loginPage import LoginPage
from Pages.timetrackPage import TimeTrackPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/sharathsarangmath/Desktop/Test_Automation_Projects/drivers/chromedriver")
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_01_login_valid(self):

        driver=self.driver

        #Enter url
        driver.get("https://online.actitime.com/ssarangmath/login.do")

        lgn = LoginPage(driver)
        lgn.enter_username("sharathsarang@gmail.com")
        lgn.enter_pwd("Shar@8971")
        lgn.click_login()
        driver.implicitly_wait(10)
        time.sleep(3)

        #Verify successful login
        pageTitle = self.driver.title
        self.assertEqual("actiTIME - Enter Time-Track",pageTitle,"Login not success")

    def test_03_login_invalid_username(self):
        driver = self.driver
        # Enter url
        driver.get("https://online.actitime.com/ssarangmath/login.do")
        lgn = LoginPage(driver)
        lgn.enter_username("sharathsarang1@gmail.com")
        lgn.enter_pwd("Shar@8971")
        lgn.click_login()
        driver.implicitly_wait(10)
        time.sleep(3)
        # verify unsuccesful login
        exp_errmsg="Username or Password is invalid. Please try again."
        errmsg=lgn.invalid_err_msg()
        self.assertEqual(exp_errmsg,errmsg,"Test Failed")


    def test_04_login_invalid_pwd(self):
        driver = self.driver
        # Enter url
        driver.get("https://online.actitime.com/ssarangmath/login.do")
        lgn = LoginPage(driver)
        lgn.enter_username("sharathsarang@gmail.com")
        lgn.enter_pwd("Shar@89711")
        lgn.click_login()
        driver.implicitly_wait(10)
        time.sleep(3)
        # verify unsuccesful login
        exp_errmsg="Username or Password is invalid. Please try again."
        errmsg = lgn.invalid_err_msg()
        self.assertEqual(exp_errmsg, errmsg, "Test Failed")


    def test_05_login_invalid_both(self):
        driver = self.driver
        # Enter url
        driver.get("https://online.actitime.com/ssarangmath/login.do")
        lgn = LoginPage(driver)
        lgn.enter_username("sharathsarang1@gmail.com")
        lgn.enter_pwd("Shar@89711")
        lgn.click_login()
        driver.implicitly_wait(10)
        time.sleep(3)
        # verify unsuccesful login
        exp_errmsg="Username or Password is invalid. Please try again."
        errmsg = lgn.invalid_err_msg()
        self.assertEqual(exp_errmsg, errmsg, "Test Failed")


    def test_06_login_blank_username(self):
        driver = self.driver
        # Enter url
        driver.get("https://online.actitime.com/ssarangmath/login.do")
        lgn = LoginPage(driver)
        #lgn.enter_username("sharathsarang@gmail.com")
        lgn.enter_pwd("Shar@8971")
        lgn.click_login()
        driver.implicitly_wait(10)
        time.sleep(3)
        # verify unsuccesful login
        exp_errmsg="Username or Password is invalid. Please try again."
        errmsg = lgn.invalid_err_msg()
        self.assertEqual(exp_errmsg, errmsg, "Test Failed")


    def test_07_login_blank_pwd(self):
        driver = self.driver

        # Enter url
        driver.get("https://online.actitime.com/ssarangmath/login.do")

        lgn = LoginPage(driver)
        lgn.enter_username("sharathsarang@gmail.com")
        #lgn.enter_pwd("Shar@8971")
        lgn.click_login()
        driver.implicitly_wait(10)
        time.sleep(3)

        # verify unsuccesful login
        exp_errmsg="Username or Password is invalid. Please try again."
        errmsg = lgn.invalid_err_msg()
        self.assertEqual(exp_errmsg, errmsg, "Test Failed")


    def test_08_login_blank_both(self):
        driver = self.driver
        # Enter url
        driver.get("https://online.actitime.com/ssarangmath/login.do")
        lgn = LoginPage(driver)
        #lgn.enter_username("sharathsarang@gmail.com")
        #lgn.enter_pwd("Shar@8971")
        lgn.click_login()
        driver.implicitly_wait(10)
        time.sleep(3)
        # verify unsuccesful login
        exp_errmsg="Username or Password is invalid. Please try again."
        errmsg = lgn.invalid_err_msg()
        self.assertEqual(exp_errmsg, errmsg, "Test Failed")


    def test_02_logout(self):
        driver = self.driver
        # Enter url
        driver.get("https://online.actitime.com/ssarangmath/login.do")
        lgn = LoginPage(driver)
        lgn.enter_username("sharathsarang@gmail.com")
        lgn.enter_pwd("Shar@8971")
        lgn.click_login()
        driver.implicitly_wait(10)
        time.sleep(3)
        lgt = TimeTrackPage(driver)
        lgt.logout()

        # Verify successful logout
        exp_title="actiTIME - Login"
        pageTitle = self.driver.title
        self.assertEqual(exp_title, pageTitle, "Logout not success")

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print ("Login Test Complete")

    #dfklklflks

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/sharathsarangmath/Desktop/Test_Automation_Projects/actiTime/Reports"))






















