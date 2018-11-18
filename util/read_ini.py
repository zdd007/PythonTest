#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: read_ini.py
@time: 2018/11/17 0:33
"""
import configparser
class ReadIni():
    '''
    读取ini文件的数据
    '''
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = "F:\myworkplace\PythonTest\config\LocalElement.ini"
        if node == None:
            self.node = "LoginElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)
    # 加载文件
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf
    def get_value(self, key):
        data = self.cf.get(self.node,key)
        return data

# if __name__ == '__main__':
#    read_init = ReadIni()
#    print(read_init.get_value('email'))


