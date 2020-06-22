from common.base_app import BaseApp
from common.start import start_app

class One_Key_login(BaseApp):

    def wait(self):
        self.driver.implicitly_wait(15)

    def one_key_login01(self):
        '''第一条一键登录的测试用例'''
        self.wait()
        self.driver.find_element_by_xpath("//*[@text='本机号码一键登录']").click()
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/authsdk_login_view").click()
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/perfection_user_info_skip").click()
        self.wait()
        self.driver.find_element_by_xpath("//*[@resource-id='com.jsmapp.jsm:id/ll_me']").click()
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/fragment_me_setup_layout").click()
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ubtExitapp").click()


    def get_login_sucess(self):
        '''获取登录成功'''
        result = self.get_text("com.jsmapp.jsm:id/me_username")
        return result

    def one_key_login02(self):
        self.wait()
        self.driver.find_element_by_xpath("//*[@text='本机号码一键登录']").click()
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/authsdk_login_view").click()
        self.wait()
        self.driver.find_element_by_xpath("//*[@resource-id='com.jsmapp.jsm:id/fl_base_header']/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
        self.wait()
        self.driver.find_element_by_xpath("//*[@resource-id='com.jsmapp.jsm:id/btn_cancel']").click()
        self.wait()
        self.driver.find_element_by_xpath("//*[@resource-id='com.jsmapp.jsm:id/ll_me']").click()

if __name__ == '__main__':
    app = start_app()
    test_login = One_Key_login(app)    #初始化类

    test_login.one_key_login01()    # 调用登录函数1

    test_login.one_key_login02()
    res = test_login.get_login_sucess()     #调用登录成功的函数
    print(res)

    exp = "用户352"
    assert  res == exp
