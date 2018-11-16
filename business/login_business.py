#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: login_business.py
@time: 2018/11/16 23:42
"""
from handle.login_handle import LoginHandle
class LoginBusiness():
    '''
    run your operation
    '''
    def __init__(self, driver):
        self.login_h = LoginHandle(driver)


    def login(self, emial, password):
        self.login_h.send_emial(emial)
        self.login_h.send_password(password)
        return True


