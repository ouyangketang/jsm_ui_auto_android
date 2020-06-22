from appium import webdriver
desired_caps = {
    "platformName":"Android",
    "deviceName":"QKKRNZNN99999999",
    "platformVersion" :"5.1.0",
    "appPackage":"com.jsmapp.jsm",
    "appActivity":"com.anyong.instantcat.ui.GuideActivity",
    # "noReset": True,  # 启动时不清除数据
    "automationName": "Uiautomator2"

}

# desired_caps02 = {
#     "platformName":"Android",
#     "deviceName":"37e7c58f",
#     "platformVersion" :"9",
#     "appPackage":"com.jsmapp.jsm",
#     "appActivity":"com.anyong.instantcat.ui.GuideActivity",
#     # "noReset": True,  # 启动时不清除数据
#     "automationName": "Uiautomator2"
#
# }
# driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

def start_app(deviceName="desired_caps", port=4723):
    '''启动app'''
    if deviceName == "desired_caps":
        des = desired_caps
        driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub'%port, des)
        return driver
if __name__ == '__main__':
    driver = start_app()