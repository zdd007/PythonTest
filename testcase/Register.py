from webDriver import driver
from selenium import webdriver
import unittest
import time
from base.baseload import BosmaSmart
class register(BosmaSmart):
    def setUp(self):
        self.url = 'https://rd.bosma.cn/uc/#/welcome'
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)  # 隐性等待30秒
        self.driver.get(self.url)

    def test_admin_register(self):#成功注册用例
        self.nickname = driver.find_element_by_xpath(".//*[@id='app']/div/div/div/form[2]/div[3]/div/div[1]/input")
        self.email = driver.find_element_by_xpath("//form[2]//input[@type='email']")
        self.password = driver.find_element_by_xpath("//form[2]//input[@type='password']")
        self.button = driver.find_element_by_xpath("//form[2]//button")
        self.nickname.send_keys("admin1")
        self.email.send_keys("1210800501@qq.com")
        self.password.send_keys("qwert123")
        self.button.click()
        self.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
     unittest.main()