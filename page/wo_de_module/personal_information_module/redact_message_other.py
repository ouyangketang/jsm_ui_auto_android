from common.base_app import BaseApp
from common.start import start_app
from common.appkey import key
class Redact_Message_Other(BaseApp):

    def wait(self):
        self.driver.implicitly_wait(5)

    def update_nickname_error01(self, name='    '):
        '''昵称输入空格情况'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改昵称
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    #点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       #清空昵称
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").send_keys(name)   #输入新的昵称
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    #点击保存

    def update_nickname_error02(self,name='!@#$%^&*'):
        '''昵称英文输入符号'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改昵称
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    #点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       #清空昵称
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").send_keys(name)   #输入新的昵称
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    #点击保存

    def update_nickname_error03(self):
        '''昵称清空后保存'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改昵称
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    #点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       #清空昵称
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    #点击保存

    def update_nickname_error04(self):
        '''昵称清空后手机物理键返回'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改昵称
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    #点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       #清空昵称
        self.driver.keyevent(4)         # 手机物理返回键

    def update_nickname_error05(self):
        '''点击昵称后左上角返回'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改昵称
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    #点击昵称栏目
        self.driver.keyevent(4)

    def update_sex_error01(self):
        '''点击性别后点击取消按钮'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/tvCancel").click()            # 点击取消按钮

    def update_date_error01(self):
        '''点击日期后点击取消按钮'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          # 点击日期栏
        self.driver.find_element_by_id("com.jsmapp.jsm:id/cancelButton").click()        # 点击取消按钮

    def update_address_error01(self):
        '''进入地址栏后点击物理返回键'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        test = Redact_Message_Other(self.driver)
        test.swipe_up()
        self.driver.keyevent(4)

if __name__ == '__main__':
    app =start_app()
    test = Redact_Message_Other(app)
    