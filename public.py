from selenium import webdriver
from driver import driver
from time import sleep
class LoginTest():

    def admin_login(self,email,password):
        sleep(2)
        email_element = driver.find_element_by_xpath("//form[1]//input[@type='email']")
        email_element.clear()
        email_element.send_keys(email)
        sleep(1)
        password_element = driver.find_element_by_xpath("//form[1]//input[@type='password']")
        password_element.clear()
        sleep(1)
        password_element.send_keys(password)
        sleep(1)
        driver.find_element_by_xpath("//form[1]//button[@type='button']").click()

