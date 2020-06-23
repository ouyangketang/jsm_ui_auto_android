from common.base_app import BaseApp
from common.start import start_app
from page.login_module.pwd_login import Test_Pwd_Login

import time
class Redact_Message(BaseApp):

    def wait(self):
        self.driver.implicitly_wait(6)

    def update_photo(self):
        test_login  = Test_Pwd_Login(self.driver)
        test_login.pwd_login06()            # 登录方法到个人中心

        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()      # 点击个人信息按钮
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_changehead").click()    # 修改头像
        self.wait()
        self.driver.find_element_by_xpath("//*[@text='拍照']").click()
        self.wait()
        self.driver.find_element_by_id("com.oppo.camera:id/shutter_button").click()         #点击拍照按钮
        self.wait()
        self.driver.find_element_by_id("com.oppo.camera:id/btn_done").click()               #选择照片按钮
        self.wait()
        self.driver.find_element_by_id("com.coloros.gallery3d:id/action_apply").click()     #裁剪照片-确定按钮

    def update_nickname(self,nickname='柯基小王子'):
        test_login  = Test_Pwd_Login(self.driver)
        test_login.pwd_login06()            # 登录方法到个人中心

        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()      # 点击个人信息按钮
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    #点击昵称栏目
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       #清空昵称
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").send_keys(nickname)   #输入新的昵称
        self.wait()
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    #点击保存

    def get_success(self):
        '''获取昵称更改成功后的信息'''
        result = self.get_text("com.jsmapp.jsm:id/personal_name")
        return result

    def update_sex(self,sex_text = '男'):
        test_login  = Test_Pwd_Login(self.driver)
        test_login.pwd_login06()            # 登录方法到个人中心
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()      # 点击个人信息按钮
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        self.wait()

        # 判断输入的条件是女生还是男生还是其他,再去点击
        if sex_text == '男':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvBoy").click()
        elif sex_text=='女':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvGirl").click()
        else:
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvOther").click()

    def update_adress(self):
        test_login  = Test_Pwd_Login(self.driver)
        test_login.pwd_login06()            # 登录方法到个人中心
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()      # 点击个人信息按钮
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        time.sleep(2)
        test_login.swipe_up()       # 调用滑动方法
        self.driver.find_element_by_xpath("//*[@text='贵州省']").click()               #选择省份
        self.driver.find_element_by_xpath("//*[@text='铜仁市']").click()
        self.driver.find_element_by_xpath("//*[@text='思南县']").click()

        # self.driver.keyevent(keycode=4)

    def update_date(self):
        test_login  = Test_Pwd_Login(self.driver)
        test_login.pwd_login06()            # 登录方法到个人中心
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()      # 点击个人信息按钮
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          #点击日期栏
        self.wait()

        self.driver.swipe(start_x=128,start_y=791,end_x=128,end_y=1002)
        self.driver.swipe(start_x=304,start_y=791,end_x=432,end_y=995)
        self.driver.swipe(start_x=464,start_y=791,end_x=592,end_y=151)
        self.driver.find_element_by_xpath("//*[@text='确定']").click()

if __name__ == '__main__':
    app =start_app()
    test_update = Redact_Message(app)

    # 测试拍照上传照片
    # test_update.update_photo()
    # res = test_update.is_toast_in("保存成功")
    # print(res)
    # exp = "保存成功"
    # assert res != exp

    # 测试修改昵称
    # test_update.update_nickname()   # 先修改昵称再获取结果
    # res =test_update.get_success()  # 获取修改后的结果
    # print(res)
    # exp = "柯基小靓仔"              # 实际结果是柯基小王子，所以不等于
    # assert res != exp

    # 测试修改性别
    # test_update.update_sex()
    # res = test_update.is_toast_in("保存成功")
    # print(res)
    # exp = "保存成功"
    # assert res!=exp

    # 测试修改地址
    # test_update.update_adress()
    # res = test_update.is_toast_in("保存成功")
    # print(res)
    # exp = "保存成功"
    # assert res!=exp

    # 测试修改生日日期
    test_update.update_date()
    res = test_update.is_toast_in("保存成功")
    print(res)
    exp = "保存成功"
    assert res!=exp









