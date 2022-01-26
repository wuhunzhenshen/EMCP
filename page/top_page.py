from selenium.webdriver.common.by import By


class TopPage:

    def __init__(self, driver):
        self.driver = driver

    # 设备监控
    def monitor_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/header/div/ul/li[1]').click()

    # 数据中心
    def datacenter_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/header/div/ul/li[2]').click()

    # 设备地图
    def map_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/header/div/ul/li[3]').click()

    # 后台管理
    def management_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/header/div/ul/li[4]').click()

    # 帮助
    def help_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/header/div/ul/li[5]').click()

    # 消息
    def message_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/header/div/ul/li[6]').click()

    # 用户中心
    def user_center_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/header/div/ul/li[7]').click()
