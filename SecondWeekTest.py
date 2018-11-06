from selenium import webdriver
import time
from public import Login
class test():
    def __init__(self):
        driver = webdriver.Firefox()
        url = "https://rd.bosma.cn/uc/#/welcome"
        driver.get(url)
        LoginTest().admin_login()
        Login.()

