from selenium.webdriver.common.by import By
import time


class ZutaimangePage:

    def __init__(self, driver):
        self.driver = driver

    # 背景色
    def backcolor_button(self):
        time.sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/div/div[1]/div/div[1]').click()
        time.sleep(1)

    # 背景色红色
    def backcolor_red_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[5]/div/div/div[21]/div').click()

    # 背景色蓝色
    def backcolor_blue_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[5]/div/div/div[14]/div').click()

    # 背景色橙色
    def backcolor_orange_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[5]/div/div/div[28]/div').click()

    # 背景色透明度
    def backcolor_trans(self, trans):
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[5]/input').clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[5]/input').send_keys(trans)

    # 背景色透明度查询
    def backcolor_trans2(self):
        time.sleep(2)
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
