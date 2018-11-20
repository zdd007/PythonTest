#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: register_handle.py
@time: 2018/11/18 13:12
"""
from page.register_page import RegisterPage

class RegisterHandle():
    '''
    处理注册业务功能
    '''
    def __init__(self, driver):
        self.driver = driver
        self.register_page = RegisterPage(self.driver)

    def send_nickname(self,nickname):
        self.register_page.get_nickname_element().sendKey(nickname)

    def send_email(self, email):
        self.register_page.get_email_element().sendKey(email)

    def send_createpassword(self, createpassword):
        self.register_page.get_createpassword_element().sendKey(createpassword)

    def click_signin(self):
        self.register_page.get_signup_element().click()











