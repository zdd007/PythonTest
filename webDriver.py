from selenium import webdriver
class driver():
    def get_driver(self):
        driver = webdriver.Firefox()
        return driver
driver = driver().get_driver()

