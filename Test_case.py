#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from appium import webdriver
import Config
import Element
import pytest
import time
from flaky import flaky

class Test():
    def wait(self):
        self.driver.implicitly_wait(15)


    def startapp(self):
        self.driver = webdriver.Remote('http://0.0.0.0:4444/wd/hub', Config.desired_caps)

    @pytest.mark.case()
    @flaky(max_runs=3, min_passes=1)
    def test_pwdlogin(self):
        self.startapp()
        self.driver.find_element_by_id(Element.onekey_register_topwd).click()
        #self.driver.implicitly_wait(15)
        self.driver.find_element_by_id(Element.et_UserName).send_keys("15675456460")
        #self.driver.implicitly_wait(15)
        self.driver.find_element_by_id(Element.et_Password).send_keys("a111111")
        #self.driver.implicitly_wait(15)
        self.driver.find_element_by_id(Element.loginBtn).click()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id(Element.iv_me_normal).click()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id(Element.ll_immediate).click()

        print("pass")


if __name__ == "__main__":
    pytest.main(['-s','Test_case.py','-m=not test'])