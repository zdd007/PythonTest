#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: register_page.py
@time: 2018/11/18 10:40
"""
from base.find_element import FindElement


class RegisterPage():
    '''
    注册页面
    '''
    def __init__(self, driver):
        self.driver = driver
        self.fd = FindElement(driver)

    def get_nickname_element(self):
        '''
        获取昵称
        :return:
        '''
        return self.fd.get_element('nickname')

    def get_email_element(self):
        '''
        获取邮箱元素数据
        :return:
        '''
        return self.fd.get_element('email')

    def get_createpassword_element(self):
        '''
        获取创建密码元素数据
        :return:
        '''
        return self.fd.get_element('createpassword')

    def get_signup_element(self):
        '''
        获取注册按钮元素数据
        :return:
        '''
        return self.fd.get_element('signup')

