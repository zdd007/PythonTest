from webDriver import driver
class register():
    def test_admin_register(self,nickname,email,password):
        nickname = driver.find_element_by_xpath("//form[2]//input[@type='text']")
        email = driver.find_element_by_xpath("//form[2]//input[@type='email']")
        password = driver.find_element_by_xpath("//form[2]//input[@type='password']")
        button = driver.find_element_by_xpath("//form[2]//button")
        nickname.send_keys("admin1")
        email.send_keys("1210800501@qq.com")
        password.send_keys("qwert123")
        button.click()
