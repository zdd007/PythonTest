#!/usr/bin/python
#coding:utf-8
import os
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
        # 初始化
        if file_name == None:
            # 因为我们不知道file_name究竟有没有值，所以为了容错，假设他没有值的时候，给他赋值
            file_name = os.path.join(os.path.dirname(os.getcwd())+'\config\\'+'LocalElement.ini')
        if node == None:
            # 同上，假设配置文件中没有node节点没有的话，就加上配置文件中的第一个node节点值
            self.node = "LoginElement"
        else:
            # 如果有节点的话，就使用读取过来的节点
            self.node = node

        self.cf = self.load_ini(file_name)
        # 引用load_ini()方法


    # 加载文件
    def load_ini(self, file_name):
        # 使用configparser这个方法进行配置文件ini的读取
        cf = configparser.ConfigParser()
        # read（）方法读取配置文件
        cf.read(file_name)
        return cf

    def get_value(self, key):
        # 获取配置文件中值：通过Key，value的键值对中的key获取到对应的value值
        data = self.cf.get(self.node,key)
        return data

# if __name__ == '__main__':
# 这是测试该py文件的代码
#    print(os.path.join(os.path.dirname(os.getcwd())+'\config\\'+'LocalElement.ini'))
#    read_init = ReadIni()
#    print(read_init.get_value('email'))
#

