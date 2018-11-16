#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: login_handle.py
@time: 2018/11/16 23:23
"""
from page.login_page import LoginPage

class LoginHandle():

    '''
    处理登陆的操作：输入email、密码的几种情况
    '''
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)

    def send_emial(self, email):
        '''
        input your emial.
        :return:
        '''
        self.login_page.get_email_element().sendKey(email)

    def send_password(self, password):
        '''
        input your password.
        :return:
        '''
        self.login_page.get_password_element().sendKey(password)



