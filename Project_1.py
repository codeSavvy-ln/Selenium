from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj = Service("C:\Driver\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
driver.get("https://www.saucedemo.com/")
driver.find_element(By.NAME, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.NAME, "login-button").click()

act_title =driver.title
exp_title = "Swag Labs"
if act_title == exp_title :
    print("Login test passed")

else:
    print("Login test failed")

time.sleep(10)
driver.close()

