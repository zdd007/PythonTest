from selenium import webdriver
class driver():
    # def __init__(self):
    #     self.driver = self.get_driver()

    def get_driver(self):
        driver = webdriver.Firefox()
        return driver
driver = driver().get_driver()
