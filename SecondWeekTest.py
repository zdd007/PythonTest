from selenium import webdriver
import time
from public import LoginTest
class test():
    def __init__(self):
        driver = webdriver.Firefox()
        url = "https://rd.bosma.cn/uc/#/welcome"
        driver.get(url)
        LoginTest().admin_login()

