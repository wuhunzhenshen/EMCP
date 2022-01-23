from selenium import webdriver
import time
import unittest
import warnings
from ddt import ddt, data, file_data, unpack

from login_page import LoginPage


@ddt
class TestC(unittest.TestCase):
    base_url = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = "http://www.lfemcp.com/login.jsp"
        cls.driver.get(cls.base_url)
        cls.driver.maximize_window()
        time.sleep(1)

    def login(self, name, password):

        warnings.simplefilter('ignore', ResourceWarning)
        lg = LoginPage(self.driver)
        lg.name_input(name)
        lg.password_input(password)
        time.sleep(0.3)
        lg.login_button()
        time.sleep(2)

    #@data(("case1", "gl3", "11111111"), ("case2", "gl6", "11111111"))
    #@unpack
    @file_data('login.json')
    def test_yn_login(self, case, name, password):
        print("IS_OK2 ")
        self.login(name, password)
        lg = LoginPage(self.driver)
        mingzi = lg.login_name()
        print(case + " name: " + mingzi)
        self.assertIn(mingzi, name)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


#if __name__ == '__main__':
    #suit = unittest.TestSuite()
    #suit.addTest(TestC("test_yn_login"))

    #runner = unittest.TextTestRunner()
    #runner.run(suit)
    #unittest.main(verbosity=2)
