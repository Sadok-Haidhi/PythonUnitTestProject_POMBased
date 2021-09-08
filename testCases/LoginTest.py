import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys
sys.path.append("C:/Users/shafidhi/PycharmProjects/PythonUnitTestProject_POMBased")
from pageObjects.LoginPage import LoginPage #we can call all methods in the class LoginPage

class LoginTest(unittest.TestCase):
    baseURL = 'https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F'
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.clickLogin()
        time.sleep(3)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "Login Page title does not match")
        lp.clickLogout()
        time.sleep(2)
        self.assertEqual("Your store. Login", self.driver.title, "Logout Page title does not match")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/shafidhi/PycharmProjects/PythonUnitTestProject_POMBased/reports'))
