#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: login_page.py
@time: 2018/11/16 23:47
"""
from base.find_element import FindElement


class LoginPage():
    '''
    页面元素读取
    '''
    def __init__(self,driver):
        self.fd = FindElement(driver)

    # 获取邮箱
    def get_email_element(self):
        return self.fd.get_element("email")

    # 获取密码
    def get_password_element(self):
        return self.fd.get_element("password")

    def get_signin_element(self):
        return self.fd.get_element('signin')
