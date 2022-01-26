from selenium import webdriver
import time
import os

driver=webdriver.Chrome()

driver.get("http://lfemcp.com/login")
time.sleep(0.2)
driver.maximize_window()
#登录
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[2]/div/div/input').clear()
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[2]/div/div/input').send_keys("gl3")
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[3]/div/div/input').clear()
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[3]/div/div/input').send_keys("11111111")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/button').click()
time.sleep(1)












