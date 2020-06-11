#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from appium import webdriver
desired_caps = {}
# desired_caps['platformName'] = 'Android'  # 系统名称
# desired_caps['platformVersion'] = '5.1'  # 系统的版本号
# desired_caps['deviceName'] = 'QKKRNZNN99999999'  # 设备名称
# #desired_caps['appPackage'] = 'com.immuxin.muxin'  # APP包名
# #desired_caps['appActivity'] = '.ui.activity.GuideActivity'  # APP入口的activity
# desired_caps['appPackage'] = 'com.jsmapp.jsm'  # APP包名
# desired_caps['appActivity'] = 'com.anyong.instantcat.ui.GuideActivity'  # APP入口的activity
caps_vivoZ5x = {
    "platformName":"Android",
    "deviceName":"37e7c58f",
    "platformVersion" :"9",
    "appPackage":"com.jsmapp.jsm",
    "appActivity":"com.anyong.instantcat.ui.GuideActivity",
    # "noReset": True,  # 启动时不清除数据
    "automationName": "Uiautomator2"

}
# driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps_vivoZ5x)