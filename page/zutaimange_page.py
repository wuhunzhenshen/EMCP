from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


class ZutaimangePage:

    def __init__(self, driver):
        self.driver = driver

    # ------顶部按钮---------------------------------------------
    # 点击保存
    def slave_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/header/div/div[4]/a[2]').click()
        time.sleep(1)

    # ------页面属性---------------------------------------------
    # 背景色
    def backcolor_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/div/div[1]/div/div[1]').click()
        time.sleep(1)

    # 背景色红色
    def backcolor_red_button(self):
        time.sleep(0.3)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[5]/div/div/div[21]/div').click()

    # 背景色蓝色
    def backcolor_blue_button(self):
        time.sleep(0.3)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[5]/div/div/div[14]/div').click()

    # 背景色橙色
    def backcolor_orange_button(self):
        time.sleep(0.3)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[5]/div/div/div[28]/div').click()

    # 背景色透明度
    def backcolor_trans(self, trans):
        time.sleep(0.8)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[5]/input').clear()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[5]/input').send_keys(trans)

    # 背景色透明度查询
    def backcolor_trans2(self):
        time.sleep(1)
        var = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[5]/input')
        return var

    # 背景色的Hex颜色值
    def backcolor_hex(self):
        hex = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[1]/input')
        return hex

    # 关闭背景色弹窗
    def backcolor_close_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/h4/i').click()

    # 勾选自定义分辨率按钮
    def custom_resolution_button(self):
        time.sleep(0.3)
        self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/'
                                           'div/div[2]/div[3]/div[1]/label/span[1]').click()
        time.sleep(1)

    # 输入自定义分辨率宽度和高度
    def custom_resolution_width_height(self, width, height):
        time.sleep(0.1)
        # 清空宽和高
        for i in range(5):
            self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/'
                                               'div/div[2]/div[3]/div[2]/div[2]/div/div/input').send_keys(
                Keys.BACKSPACE)

        time.sleep(1)
        # 设置宽
        self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/'
                                           'div/div[2]/div[3]/div[2]/div[2]/div/div/input').send_keys(width)

        for j in range(5):
            self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/'
                                               'div/div[2]/div[3]/div[2]/div[5]/div/div/input').send_keys(
                Keys.BACKSPACE)
        # 设置高
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/'
                                           'div/div[2]/div[3]/div[2]/div[5]/div/div/input').send_keys(height)

    # 读取宽
    def resolution_width(self):

        var = self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/'
                                                 'div/div[2]/div[3]/div[2]/'
                                                 'div[2]/div/div/input').get_attribute("value")
        return var

    # 读取高
    def resolution_height(self):

        var = self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/'
                                                 'div/div[2]/div[3]/div[2]/div[5]/div/div/'
                                                 'input').get_attribute("value")
        return var

    # 设置页面密码
    def set_page_key(self):
        self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/'
                                           'div/div[3]/div[2]/div[1]/label/span[1]').click()

    # 输入页面密码
    def input_page_key(self, key2):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/'
                                           'div/div[3]/div[2]/div[2]/form/div/div/div/input').clear()

        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/'
                                           'div/div[3]/div[2]/div[2]/form/div/div/div/input').send_keys(key2)

    # 读取页面密码
    def read_page_key(self):
        var = self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/'
                                                 'div/div[3]/div[2]/div[2]/form/div/div/'
                                                 'div/input').get_attribute("value")
        return var

    # 判断是否勾选启用页面密码
    def read_set_page_key(self):
        var = self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/'
                                                 'div/div[3]/div[2]/div[1]/label/span[1]').get_attribute("class")
        if var == "el-checkbox__input is-checked":
            return True
        else:
            return False

    # -----左侧控件---------------------------------------
    # 数显框
    def digital_display_frame(self):
        self.driver.find_element(By.XPATH, '//*[@id="el-collapse-content-1842"]/div/ul/li[1]').click()
