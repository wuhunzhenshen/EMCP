from selenium.webdriver.common.by import By
import time

class ZutaimangePage:

    def __init__(self, driver):
        self.driver = driver

    # 背景色
    def backcolor_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="formBar"]/aside[1]/div/div[2]/div/div[1]/div/div[1]').click()

    # 背景色红色
    def backcolor_red_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[5]/div/div/div[21]/div').click()

    # 背景色蓝色
    def backcolor_blue_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[5]/div/div/div[14]/div').click()

    # 背景色橙色
    def backcolor_orange_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[5]/div/div/div[28]').click()

