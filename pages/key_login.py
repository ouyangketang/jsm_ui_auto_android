from common.baseapp import BaseApp
from common.start import start_app

class Key_Login(BaseApp):

    def direct_login(self):
        '''第一条测试用例登录函数'''
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//*[@text='本机号码一键登录']").click()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//*[@text='一键登录']").click()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//*[@text='跳过']").click()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//*[@text='取消']").click()

    def get_login_sucess(self):
        '''获取登录成功'''
        result = self.get_text("com.jsmapp.jsm:id/immediate_target_number")
        return result

    def update_data_login(self):
        '''第二条测试用例修改资料页面点击返回键的登录函数'''
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//*[@text='本机号码一键登录']").click()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//*[@text='一键登录']").click()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//*[@resource-id='com.jsmapp.jsm:id/fl_base_header']/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()    #点击左上角返回键
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//*[@text='跳过']").click()    # 填写资料-左上角返回-跳过按钮
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//*[@text='取消']").click()     #取消授权


if __name__ == '__main__':
    app = start_app()
    test_login = Key_Login(app)

    test_login.direct_login()   #启动登录函数

    result = test_login.get_login_sucess()
    print(result)

    exp = "5000"
    if result== exp:
        print("yes")
    else:
        print("no")










