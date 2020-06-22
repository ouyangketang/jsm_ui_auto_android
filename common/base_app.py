from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

class BaseApp():
    def __init__(self,driver:webdriver.Remote):
        self.driver = driver
        self.size =self.driver.get_window_size()

    def get_text(self, locator):
        '''获取元素文本'''
        try:
            t = self.driver.find_element_by_id(locator).text
        except:
            t = ""
        return t

    def get_text_xpath(self, locator):
        '''获取元素文本'''
        try:
            t = self.driver.find_element_by_xpath(locator).text
        except:
            t = ""
        return t

    def is_toast_in(self, text):
        '''定位toast消息, 判断toast信息是否包含text文本内容'''
        toast = ('xpath', '//*[contains(@text, "%s")]' % text)
        try:
            el = WebDriverWait(self.driver, 30, 0.2).until(EC.presence_of_element_located(toast))
            print("toast内容：%s" % el.text)
            if text in el.text:
                return True
            else:
                return False
        except:
            return True

    def swipe_up(self, n=1):
        '''
        往上滑
        :param driver:
        :return:  None
        '''
        x1 = self.size['width']/2
        y1 = self.size['height'] * 3 /4
        x2 = self.size['width']/2
        y2 = self.size['height'] /4
        for i in range(n):
            self.driver.swipe(x1, y1,  x2, y2, 500)

    def swipe_down(self, n=1):
        '''
        往下滑
        :param driver:
        :return: None
        '''
        x1 = self.size['width']/2
        y1 = self.size['height'] /4
        x2 = self.size['width']/2
        y2 = self.size['height'] * 3 /4
        for i in range(n):
            self.driver.swipe(x1, y1,  x2, y2, 500)

    def tap_native(self, el=None, x=None, y=None, count=1):
        '''
        触摸操作，native原生app上的元素，tap事件
        :param driver:
        :param el:  元素对象
        :param x:  x坐标
        :param y:  y坐标
        :param count: 次数
        :return:
        '''
        action = TouchAction(self.driver)
        if el:
            action.tap(element=el, count=count).perform()
        else:
            action.tap(x=x, y=y, count=count).perform()
