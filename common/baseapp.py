from appium import webdriver
class BaseApp():
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.a = self.driver.get_window_size()

    def get_text(self, locator):
        try:
            t = self.driver.find_element_by_id(locator).text
        except:
            t = ""
        return t

    def get_text_xpath(self, locator):
        try:
            t = self.driver.find_element_by_xpath(locator).text
        except:
            t = ""
        return t