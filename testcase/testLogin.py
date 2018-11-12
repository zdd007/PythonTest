from webDriver import driver
from base.baseload import BosmaSmart
from time import sleep
import unittest


class login(unittest.TestSuite):
    '''登录模块'''
    def setUp(self):
        self.driver = driver.get_driver(self)
        self.driver.get('https://rd.bosma.cn/uc/#/welcome')
    def test_admin_login(self):
        '''正确流程的登录操作'''
        email = self.driver.find_element_by_xpath("//form[1]//input[@type='email']")
        password = self.driver.find_element_by_xpath("//form[1]//input[@type='password']")
        button = self.driver.find_element_by_xpath("//form[1]//button")
        email.send_keys("1451953028@qq.com")
        password.send_keys("zdd123456")
        button.click()
        sleep(2)
    def test_login_emailempty(self):
        '''登录邮箱未空'''
        email = self.driver.find_element_by_xpath("//form[1]//input[@type='email']")
        password = self.driver.find_element_by_xpath("//form[1]//input[@type='password']")
        button = self.driver.find_element_by_xpath("//form[1]//button")
        email.send_keys("")
        password.send_keys("zdd123456")
        button.click()
        sleep(2)
    def test_login_wrongpassword(self):
        '''登录密码错误'''
        email = self.driver.find_element_by_xpath("//form[1]//input[@type='email']")
        password = self.driver.find_element_by_xpath("//form[1]//input[@type='password']")
        button = self.driver.find_element_by_xpath("//form[1]//button")
        email.send_keys("1451953028@qq.com")
        password.send_keys("12345665fgdf")
        button.click()
        sleep(2)
    def tearDown(self):
        self.driver.quit()
        sleep(3)