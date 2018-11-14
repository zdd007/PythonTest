from webDriver import driver
from base.baseload import BosmaSmart
from time import sleep
import unittest


class register(unittest.TestCase):
    def setUp(self):
        self.driver = driver.get_driver(self)
        self.driver.get('https://rd.bosma.cn/uc/#/welcome')

    def test_admin_register(self):
        # driver = self.driver
        sleep(2)
        nickname = self.driver.find_element_by_xpath("//form[2]//input[@type='text']")
        email = self.driver.find_element_by_xpath("//form[2]//input[@type='email']")
        password = self.driver.find_element_by_xpath("//form[2]//input[@type='password']")
        button = self.driver.find_element_by_xpath("//form[2]//button")
        nickname.send_keys("admin1")
        email.send_keys("hnojmd12947@chacuo.net")
        password.send_keys("qwert123")
        sleep(2)
        button.click()
        sleep(3)
    def test_has_email(self):
        # driver.get('https://rd.bosma.cn/uc/#/welcome')
        sleep(2)
        nickname = self.driver.find_element_by_xpath("//form[2]//input[@type='text']")
        email = self.driver.find_element_by_xpath("//form[2]//input[@type='email']")
        password = self.driver.find_element_by_xpath("//form[2]//input[@type='password']")
        button = self.driver.find_element_by_xpath("//form[2]//button")
        nickname.send_keys("admin1")
        email.send_keys("1210800501@qq.com")
        password.send_keys("qwert123")
        sleep(2)
        button.click()
        sleep(3)
    def test_email_is_empty(self):
        # driver.get('https://rd.bosma.cn/uc/#/welcome')
        sleep(2)
        nickname = self.driver.find_element_by_xpath("//form[2]//input[@type='text']")
        email = self.driver.find_element_by_xpath("//form[2]//input[@type='email']")
        password = self.driver.find_element_by_xpath("//form[2]//input[@type='password']")
        button = self.driver.find_element_by_xpath("//form[2]//button")
        nickname.send_keys("admin1")
        email.send_keys("")
        password.send_keys("qwert123")
        sleep(2)
        button.click()
        sleep(3)
    def tearDown(self):
        self.driver.quit()
        sleep(3)

