from selenium import webdriver
import time
import unittest
import warnings
import sys
from ddt import ddt, data, file_data, unpack
from login_page import LoginPage
from top_page import TopPage
from left_page import LeftPage
from zutaimange_page import ZutaimangePage


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
        time.sleep(1)

    # 登录
    @file_data('login.json')
    def test_1_login(self, name, password):
        self.login(name, password)
        lg = LoginPage(self.driver)
        mingzi = lg.login_name()
        print("用户: " + mingzi + " 登录成功")
        self.assertIn(mingzi, name)
        time.sleep(0.3)

    # 找到数据中心
    def test_2_data_center_mange(self):
        # 点击后台管理
        time.sleep(0.3)
        mange = TopPage(self.driver)
        time.sleep(1)
        mange.management_button()

        # 点击数据中心
        time.sleep(0.3)
        data_center = LeftPage(self.driver)
        time.sleep(0.3)
        data_center.data_center_mange_button()
        time.sleep(1)
        data_center.data_center_zutai_mange_button()

        # 关闭引导页
        time.sleep(0.6)
        data_center.data_center_leader()

    def test_3_backcolor_mange(self):
        # 组态编辑
        time.sleep(1)
        zutai = ZutaimangePage(self.driver)
        # 打开设置背景色
        zutai.backcolor_button()
        time.sleep(2)

        # 选择背景颜色为橙色
        zutai.backcolor_red_button()
        time.sleep(0.2)
        zutai.backcolor_blue_button()
        time.sleep(0.2)
        zutai.backcolor_orange_button()
        time.sleep(0.2)
        # 设置背景色透明度
        zutai.backcolor_trans("0.2")
        time.sleep(0.2)
        zutai.backcolor_trans("0.5")
        time.sleep(0.2)
        zutai.backcolor_trans("0.9")
        print("背景透明度为： ", zutai.backcolor_trans2().get_attribute("value"))
        # 判断背景颜色
        hex2 = zutai.backcolor_hex().get_attribute("value")
        self.assertIn("FF8D02", hex2)
        print("背景HEX颜色为： ", hex2)

        # 关闭背景色设置弹窗
        zutai.backcolor_close_button()
        time.sleep(0.6)
        # 勾选自定义分辨率

        zutai.custom_resolution_button()
        time.sleep(1)
        # 设置宽和高
        width = '1920'
        height = '1080'
        zutai.custom_resolution_width_height(width, height)
        # 保存
        time.sleep(1)
        zutai.slave_button()
        # 断言宽和高设置成功与否
        wi = zutai.resolution_width()
        he = zutai.resolution_height()
        self.assertIn(wi, width)
        self.assertIn(he, height)
        if wi == width and he == height:
            print("分辨率设置成功！宽为：" + wi, "高为：" + he)
        else:
            print("分辨率设置失败！")

        # 设置页面密码
        keys3 = "123456"
        if zutai.read_set_page_key():
            zutai.input_page_key(keys3)
            time.sleep(1)
            zutai.slave_button()
        else:
            zutai.set_page_key()
            zutai.input_page_key(keys3)
            zutai.slave_button()
            # 判断页面密码是否设置成功
        pagekeys = zutai.read_page_key()
        self.assertIn(keys3, pagekeys)
        print("页面密码为："+pagekeys)

    # 关闭浏览器
    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.back()
        time.sleep(2)
        cls.driver.quit()

# if __name__ == '__main__':
# suits = unittest.TestSuite()
# suits.addTest(Test_data_center("test_1_login"))
# suits.addTest(Test_data_center("test_2_data_center_mange"))
# runner = unittest.TextTestRunner()
# runner.run(suits)
# unittest.main(verbosity=2)
