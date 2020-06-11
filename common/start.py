from appium import webdriver


caps_vivoZ5x = {
    "platformName":"Android",
    "deviceName":"37e7c58f",
    "platformVersion" :"9",
    "appPackage":"com.jsmapp.jsm",
    "appActivity":"com.anyong.instantcat.ui.GuideActivity",
    # "noReset": True,  # 启动时不清除数据
    "automationName": "Uiautomator2"

}
driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps_vivoZ5x)

# des_yeshen = {
#                 "platformName": "Android",
#                 "deviceName": "127.0.0.1:62001",
#                 "platformVersion": "4.4.2",
#                 "appPackage": "com.yipiao",
#                 "appActivity": "com.yipiao.activity.LaunchActivity",
#                 "udid": "127.0.0.1:62001",  # 识别手机唯一标识
#                 "noReset": True,
#                 "automationName": "Uiautomator2"  # toast 必须用Uiautomator2
#                 }

def start_app(deviceName="caps_vivoZ5x", port=4723):
    '''启动app'''
    if deviceName == "caps_vivoZ5x":
        des = caps_vivoZ5x
    # elif deviceName == "yeshen":
    #     des = des_yeshen
    # else:
    #     des = des_yeshen
    driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub'%port, des)
    return driver
if __name__ == '__main__':
    driver = start_app()