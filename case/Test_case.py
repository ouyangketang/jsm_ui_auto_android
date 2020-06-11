#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from appium import webdriver
from common import Config
from pages.key_login import Key_Login
import pytest
from flaky import flaky

class Test():
    def wait(self):
        self.driver.implicitly_wait(15)

    def startapp(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Config.caps_vivoZ5x)

    @pytest.mark.case()
    @flaky(max_runs=3, min_passes=1)
    def test_key_login(self):
        self.startapp()     # 启动app
        test_login = Key_Login(self.driver)    # 登录函数
        test_login.direct_login()   # 第一条测试用例登录

        # 判断是否登录成功
        exp = "5000"
        res = test_login.get_login_sucess()  #获取登录结果

        print(res)
        assert exp == res     # 断言

if __name__ == "__main__":
    pytest.main(['-s','Test_case.py','-m=not test'])