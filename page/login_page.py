from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def name_input(self, name_key):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/form/div[2]/div/div/input').send_keys(
            name_key)

    def password_input(self, password_key):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/form/div[3]/div/div/input').send_keys(
            password_key)

    def login_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/form/button').click()

    def login_name(self):
        var = self.driver.find_element(By.CLASS_NAME, 'username').text
        return var
