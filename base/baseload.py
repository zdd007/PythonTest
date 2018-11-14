import time
from selenium import webdriver
import unittest

class BosmaSmart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        baseURL = "https://rd.bosma.cn/uc/#/welcome"
        self.driver.get(baseURL)
        self.verificationErrors = []  # 脚本运行时，错误的信息将被打印到这个列表中
        self.accept_next_alert = True  # 是否继续接受下一下警告

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
