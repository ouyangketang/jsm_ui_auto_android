from common.base_app import BaseApp
from common.start import start_app
from common.appkey import key
import time
class Redact_Message_Other(BaseApp):


    def update_nickname_error01(self, name='    '):
        '''昵称输入空格情况'''
        # 切换到我的页面
        # time.sleep(3)
        # self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # # 点击个人信息按钮
        # time.sleep(3)
        # self.driver.find_element_by_xpath("//*[@text='编辑个人信息']").click()
        time.sleep(3)
        # 修改昵称
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    # 点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       # 清空昵称
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").send_keys(name)   # 输入新的昵称
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    # 点击保存

    def update_nickname_error02(self, name='!@#$%^&*'):
        '''昵称英文输入符号'''
        self.driver.keyevent(4)         # 返回个人信息页面
        time.sleep(2)
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    # 点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       # 清空昵称
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").send_keys(name)   # 输入新的昵称
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    # 点击保存

    def update_nickname_error03(self):
        '''昵称清空后保存'''
        time.sleep(2)
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    # 点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       # 清空昵称
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    # 点击保存
        self.driver.keyevent(4)  # 返回个人信息页面

    def update_nickname_error04(self):
        '''昵称清空后手机物理键返回'''

        time.sleep(2)
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    # 点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       # 清空昵称
        self.driver.keyevent(4)         # 手机物理返回键

    def update_sex_error01(self):
        '''点击性别后点击取消按钮'''
        time.sleep(2)
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/tvCancel").click()            # 点击取消按钮

    def update_date_error01(self):
        '''点击日期后点击取消按钮'''
        time.sleep(2)
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          # 点击日期栏
        self.driver.find_element_by_id("com.jsmapp.jsm:id/cancelButton").click()        # 点击取消按钮

    def update_address_error01(self):
        '''进入地址栏后点击物理返回键'''
        time.sleep(2)
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        time.sleep(3)
        test = Redact_Message_Other(self.driver)
        test.swipeUp()
        self.driver.keyevent(4)

if __name__ == '__main__':
    app = start_app()
    test = Redact_Message_Other(app)
    