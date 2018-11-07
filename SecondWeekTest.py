from selenium import webdriver
import time
from public import LoginTest
from driver import driver
class test1():

    def test1(self):
        url = "https://rd.bosma.cn/uc/#/welcome"
        url = driver.get(url)
        user_file = open('user.txt','r')
        line = user_file.readline()
        email = line.split(',')[0]
        password = line.split(',')[1]
        print(email)
        print(password)
        LoginTest().admin_login(email,password)
if __name__ == '__main__':
    test = test1()
    test.test1()


