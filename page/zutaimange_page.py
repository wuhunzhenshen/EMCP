from selenium.webdriver.common.by import By


class ZutaimangePage:

    def __init__(self, driver):
        self.driver = driver

    # 数显框
    def shuxiankuang_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="el-collapse-content-5809"]/div/ul/li[1]').click()

