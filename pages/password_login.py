from appium import webdriver
from common.baseapp import Base

import time
caps = {
    "platformName":"Android",
    "deviceName":"5fc8dc42",
    "platformVersion" : "8.1.0",
    "appPackage":"com.jsmapp.jsm",
    "appActivity":"com.anyong.instantcat.ui.GuideActivity"

}
driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)

class Test_Password_Login(Base):

    loc1 = {"name": "切换账号", "by": "", "value": ""}
    loc2 = {"name": "密码登录", "by": "", "value": ""}
    loc3 = {"name": "输入手机号", "by": "", "value": ""}
    loc4 = {"name": "输入密码", "by": "", "value": ""}
    loc5 = {"name": "登录", "by": "", "value": ""}

