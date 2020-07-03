# coding:UTF-8
import pytest
from appium import webdriver
from common.start import desired_caps

driver = None
@pytest.fixture(scope='session', autouse=True)
def startapp(request):
    global driver
    if driver is None:
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def end():
        driver.quit()
    request.addfinalizer(end)
    return driver