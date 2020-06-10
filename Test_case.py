#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from appium import webdriver
import Config
import Element
import pytest
import time
from flaky import flaky

class Test():
    def startapp(self):
        self.driver = webdriver.Remote('http://0.0.0.0:4444/wd/hub', Config.desired_caps)

    @pytest.mark.case()
    @flaky(max_runs=3, min_passes=1)
    def test_pwdlogin(self):
        self.startapp()
        self.driver.find_element_by_id(Element.onekey_register_topwd).click()
        print("pass")


if __name__ == "__main__":
    pytest.main(['-s','Test_case.py','-m=not test'])