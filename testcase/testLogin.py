from selenium import webdriver
import unittest
import time

class login(unittest.TestSuite):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://rd.bosma.cn/uc/#/welcome")
    def test_admin_login(self):
        email = self.driver.find_element_by_xpath("//form[1]//input[@type='email']")
        password = self.driver.find_element_by_xpath("//form[1]//input[@type='password']")
        button = self.driver.find_element_by_xpath("//form[1]//button")
        email.send_keys("1451953028@qq.com")
        password.send_keys("zdd123456")
        button.click()
        time.sleep(2)