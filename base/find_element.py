#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: find_element.py
@time: 2018/11/16 23:55
"""
from util.read_ini import ReadIni
class FindElement():
    '''
    查找元素
    '''
    def __init__(self,driver):
        self.driver = driver
        # get_user_log = UserLog()
        # self.logger = get_user_log.get_log()
    def get_element(self,key):
        # 从ini文件中获取元素
        read_ini = ReadIni()
        # 获取到的数据
        data = read_ini.get_value(key)
        # 对数据进行分片
        by = data.split('>')[0]
        value = data.split('>')[1]
        # self.logger.info("定位方式:"+by+"--->定位值:"+value)
        try:
            if by == 'id':
                # 返回id的查找方式
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None