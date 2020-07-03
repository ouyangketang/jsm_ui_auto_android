# coding:UTF-8
from common.start import start_app
from common.base_app import BaseApp
import time
class Test_Pwd_Login(BaseApp):

    def pwd_login01(self, username='12345678912', psword='qwer1234'):
        '''错误用例:手机号格式错误'''
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@resource-id='com.jsmapp.jsm:id/onekey_login_topwd']").click()   # 首页点击密码登录
        self.driver.find_element_by_xpath("//*[@text='切换账号']").click()      # 切换账号
        self.driver.find_element_by_xpath("//*[@text='密码登录']").click()      # 切换账号后点击密码登录
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_UserName").send_keys(username)     # 输入账号
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_Password").send_keys(psword)       # 输入密码
        self.driver.find_element_by_id("com.jsmapp.jsm:id/loginBtn").click()            # 点击登录

    def pwd_login02(self, username='1234567', psword='qwer1234'):
        '''错误用例:手机号位数错误'''
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_UserName").clear()     # 清空账号
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_UserName").send_keys(username)  # 输入账号
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_Password").clear()     # 清空密码
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_Password").send_keys(psword)  # 输入密码
        self.driver.find_element_by_id("com.jsmapp.jsm:id/loginBtn").click()  # 点击登录

    def pwd_login03(self, username='15387399093', psword='qwer234'):
        '''错误用例:密码错误'''
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_UserName").clear()  # 清空账号
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_UserName").send_keys(username)  # 输入账号
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_Password").clear()  # 清空密码
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_Password").send_keys(psword)  # 输入密码
        self.driver.find_element_by_id("com.jsmapp.jsm:id/loginBtn").click()  # 点击登录

    def pwd_login04(self, username='15387399093', psword='qwer234'):
        '''错误用例:账号被冻结'''
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_UserName").clear()  # 清空账号
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_UserName").send_keys(username)  # 输入账号
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_Password").clear()  # 清空密码
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_Password").send_keys(psword)  # 输入密码
        self.driver.find_element_by_id("com.jsmapp.jsm:id/loginBtn").click()  # 点击登录

    def pwd_login05(self, username='15387399093', psword='       '):
        '''错误用例:密码有空格'''
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_UserName").clear()  # 清空账号
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_UserName").send_keys(username)  # 输入账号
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_Password").clear()  # 清空密码
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_Password").send_keys(psword)  # 输入密码
        self.driver.find_element_by_id("com.jsmapp.jsm:id/loginBtn").click()  # 点击登录

    def pwd_login06(self, username='15387399093', psword='qwer1234'):
        '''密码登录成功的用例'''
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_UserName").clear()  # 清空账号
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_UserName").send_keys(username)  # 输入账号
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_Password").clear()  # 清空密码
        self.driver.find_element_by_id("com.jsmapp.jsm:id/et_Password").send_keys(psword)  # 输入密码
        self.driver.find_element_by_id("com.jsmapp.jsm:id/loginBtn").click()  # 点击登录
        time.sleep(4)
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()

    def get_success(self):
        result = self.get_text("com.jsmapp.jsm:id/me_username")
        return result

if __name__ == '__main__':
    app = start_app()
    test_pwd_login = Test_Pwd_Login(app)

    # test_pwd_login.pwd_login01()
    # res = test_pwd_login.is_toast_in("账号不存在")
    # exp = "账号不存在"
    # assert res != exp

    # test_pwd_login.pwd_login03()
    # res = test_pwd_login.is_toast_in("密码错误")
    # print(str(res))
    # exp = "密码错误"
    # assert res != exp

    # test_pwd_login.pwd_login05()
    # res =test_pwd_login.is_toast_in("密码格式错误")
    # print(str(res))
    # exp = "密码格式错误"
    # assert res!=exp

    test_pwd_login.pwd_login06()
    res = test_pwd_login.get_success()
    print(res)
    exp = "柯基小王子"
    assert res == exp


