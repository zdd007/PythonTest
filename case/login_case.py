#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: login_case.py
@time: 2018/11/17 1:26
"""
import os
import sys
# 引入本地文件
sys.path.append('F:\myworkplace\PythonTest')
from business.login_business import LoginBusiness
from selenium import webdriver
import unittest
import time
import HTMLTestRunner


class LoginCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        time.sleep(5)
        cls.driver.get('https://rd.bosma.cn/uc/#/welcome')
        cls.driver.maximize_window()

    def setUp(self):
        self.login = LoginBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        


    def test_login(self):
        self.login.login('1451953028@qq.com','zdd123456')


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd() + "/report/" + "login_case.html")
    f = open(file_path, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(LoginCase('test_login'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is bosma report",description=u"这个是我们第一次测试报告",verbosity=2)
    runner.run(suite)
