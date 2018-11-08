from selenium import webdriver
import unittest


class login(unittest.TestSuite):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://rd.bosma.cn/uc/#/welcome")
    def test_admin_login(self):
        email = self.driver.find_element_by_xpath("")
        password = self.driver.find_element_by_xpath("")
        button = self.driver.find_element_by_xpath("")