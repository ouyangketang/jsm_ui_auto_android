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

    def swipeUp(self, t=500, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.2  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)


    def swipeDown(self, t=500, n=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(self, t=500, n=1):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipRight(self, t=500, n=1):
        '''向右滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

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
