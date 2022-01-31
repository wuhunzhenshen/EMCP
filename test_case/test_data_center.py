from selenium import webdriver
import time
import unittest
import warnings
import sys
from ddt import ddt, data, file_data, unpack
from login_page import LoginPage
from top_page import TopPage
from left_page import LeftPage


@ddt
class Test_data_center(unittest.TestCase):
    base_url = None
    driver = None

    # 初始化浏览器
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = "http://www.lfemcp.com/login.jsp"
        cls.driver.get(cls.base_url)
        cls.driver.maximize_window()
        time.sleep(1)

    # 登录公用函数
    def login(self, name, password):
        warnings.simplefilter('ignore', ResourceWarning)
        lg = LoginPage(self.driver)
        lg.name_input(name)
        lg.password_input(password)
        time.sleep(0.3)
        lg.login_button()
        time.sleep(2)

    # 登录
    @file_data('login.json')
    def test_yn_login(self, name, password):
        self.login(name, password)
        lg = LoginPage(self.driver)
        mingzi = lg.login_name()
        print(" 用户: " + mingzi + " 登录成功")
        self.assertIn(mingzi, name)
        time.sleep(2)

    # 找到数据中心
    def test_find_data_center_mange(self):
        # 点击后台管理
        time.sleep(2)
        mange = TopPage(self.driver)
        mange.management_button()

        # 点击数据中心
        time.sleep(2)
        data_center = LeftPage(self.driver)
        data_center.data_center_mange_button()
        data_center.data_center_zutai_mange_button()

    # 关闭浏览器
    @classmethod
    def tearDownClass(cls):
        cls.driver.back()
        time.sleep(2)
        cls.driver.quit()


if __name__ == '__main__':
    # suit = unittest.TestSuite()
    # suit.addTest(TestC("test_yn_login"))
    # runner = unittest.TextTestRunner()
    # runner.run(suit)
    unittest.main(verbosity=2)
