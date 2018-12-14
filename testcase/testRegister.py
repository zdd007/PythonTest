from webDriver import driver
from base.baseload import BosmaSmart
from time import sleep
import unittest
import datetime


class Register(unittest.TestCase):

    def setUp(self):
        self.driver = driver.get_driver(self)
        self.driver.get('https://rd.bosma.cn/uc/#/welcome')

    def test_admin_register(self):
        '''正常的注册流程'''
        date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        # 你获取的是当前时间作为账号，也就是注册的账号都是有效的，能正常注册的。
        emaildata = date + '@python.com'
        sleep(2)
        nickname = self.driver.find_element_by_xpath("//form[2]//input[@type='text']")
        email = self.driver.find_element_by_xpath("//form[2]//input[@type='email']")
        password = self.driver.find_element_by_xpath("//form[2]//input[@type='password']")
        button = self.driver.find_element_by_xpath("//form[2]//button")
        nickname.send_keys("admin1")
        email.send_keys(emaildata)
        password.send_keys("qwert123")
        sleep(2)
        button.click()
        self.driver.implicitly_wait(10)
        #然后你又在这里判断一个有误的，这不是有误的，注册成功也有弹出框，提示语是这个：
        successAlert = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/span")
        print("what is this:%s"%successAlert.text)
        # print(successAlert.text)
        self.assertEqual('Alert', successAlert.text)
        click_ok = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/button").click()

    @unittest.skip("忽略")
    def test_has_email(self):
        '''已经注册过的邮箱'''
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
        emailhint = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/p")
        self.assertEquals('This email address has already been registered.',  emailhint.text())

    @unittest.skip("忽略")
    def test_email_is_empty(self):
        '''邮箱号为空'''
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
        emailEmpty = self.driver.find_element_by_link_text("/html/body/div[1]/div/div/div/div/form[2]/div[2]/div/div[2]")
        self.assertEquals('Please input your email.',  emailEmpty.text())

    def tearDown(self):
        self.driver.quit()
        sleep(3)

if __name__ == '__main__':
    unittest.main()
