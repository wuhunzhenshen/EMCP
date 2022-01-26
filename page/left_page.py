from selenium.webdriver.common.by import By


class LeftPage:

    def __init__(self, driver):
        self.driver = driver

    # 设备中心
    def equip_center_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[1]').click()

    # 设备管理
    def equip_mange_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[1]/ul/li[1]').click()

    # 数据规则
    def data_rules_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[1]/ul/li[2]').click()

    # 模块管理
    def module_mange_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[1]/ul/li[3]').click()

    # EG设备管理
    def eg_equip_mange_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[1]/ul/li[4]').click()

    # 数据中心管理
    def data_center_mange_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[2]').click()

    # 数据中心组态编辑
    def data_center_zutai_mange_button(self):
        self.driver.find_element(By.LINK_TEXT, "组态管理").click()

    # 运营中心管理
    def opera_center_mange_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[3]').click()

    # 账号管理
    def user_mange_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[4]').click()

    # 组织架构
    def organ_mange_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[5]').click()

    # 短信管理
    def short_message_ange_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[6]').click()

    # 萤石云秘钥
    def key_mange_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[7]').click()

    # 物联卡管理
    def iot_mange_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[8]').click()

    # 风格管理
    def style_mange_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[9]').click()

    # api配置
    def api_mange_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[10]').click()
