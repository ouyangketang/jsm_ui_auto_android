from common.base_app import BaseApp
from common.start import start_app
import time
class Redact_Message(BaseApp):

    def wait(self):
        self.driver.implicitly_wait(5)

    def update_photo_case01(self):
        '''修改头像栏'''
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
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

    def update_nickname_case02(self,nickname='柯基小王子'):
        '''修改昵称栏'''
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
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

    def update_sex_case03(self,sex_text = '男'):
        '''修改性别栏'''
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
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

    def update_adress_case04(self):
        '''修改地址栏'''
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()      # 点击个人信息按钮
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        # self.driver.swipe(start_x=360, start_y=1015, end_x=360, end_y=125, duration=1000)

        time.sleep(5)
        test = Redact_Message(self.driver)
        test.swipeUp()
        print(test.size['width'])
        print(test.size['height'])
        self.driver.find_element_by_xpath("//*[@text='四川省']").click()               #选择省份
        self.driver.find_element_by_xpath("//*[@text='乐山市']").click()
        self.driver.find_element_by_xpath("//*[@text='沐川县']").click()


    def update_date_case05(self):
        '''修改日期栏'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()      # 点击个人信息按钮
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          #点击日期栏
        self.wait()

        self.driver.swipe(start_x=128, start_y=791, end_x=128, end_y=1002)
        self.driver.swipe(start_x=304, start_y=791, end_x=432, end_y=995)
        self.driver.swipe(start_x=464, start_y=791, end_x=592, end_y=151)
        self.driver.find_element_by_xpath("//*[@text='确定']").click()

    def update_case06(self, name='魔力转圈圈', sex_text='男'):
        '''修改头像、昵称、性别、地址、日期'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改头像
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_changehead").click()    # 修改头像
        self.driver.find_element_by_xpath("//*[@text='拍照']").click()
        self.driver.find_element_by_id("com.oppo.camera:id/shutter_button").click()         #点击拍照按钮
        self.driver.find_element_by_id("com.oppo.camera:id/btn_done").click()               #选择照片按钮
        self.driver.find_element_by_id("com.coloros.gallery3d:id/action_apply").click()     #裁剪照片-确定按钮
        # 修改昵称
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    #点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       #清空昵称
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").send_keys(name)   #输入新的昵称
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    #点击保存
        # 修改性别
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        # 判断输入的条件是女生还是男生还是其他,再去点击
        if sex_text == '男':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvBoy").click()
        elif sex_text=='女':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvGirl").click()
        else:
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvOther").click()

        # 修改地址
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目

        time.sleep(5)
        test = Redact_Message(self.driver)
        test.swipeUp()
        self.driver.find_element_by_xpath("//*[@text='广东省']").click()               #选择省份
        self.driver.find_element_by_xpath("//*[@text='韶关市']").click()
        self.driver.find_element_by_xpath("//*[@text='武江区']").click()
        # 修改日期
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          #点击日期栏
        self.driver.swipe(start_x=190,start_y=791,end_x=200,end_y=1036)     #   年
        self.driver.swipe(start_x=312,start_y=791,end_x=546,end_y=779)      #   月
        self.driver.swipe(start_x=456,start_y=791,end_x=592,end_y=195)      #   日
        self.driver.find_element_by_xpath("//*[@text='确定']").click()

    def update_case07(self,name='测试账号5',sex_text='其他'):
        '''修改头像、昵称、性别、地址'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改头像
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_changehead").click()    # 修改头像
        self.driver.find_element_by_xpath("//*[@text='拍照']").click()
        self.driver.find_element_by_id("com.oppo.camera:id/shutter_button").click()         #点击拍照按钮
        self.driver.find_element_by_id("com.oppo.camera:id/btn_done").click()               #选择照片按钮
        self.driver.find_element_by_id("com.coloros.gallery3d:id/action_apply").click()     #裁剪照片-确定按钮
        # 修改昵称
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    #点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       #清空昵称
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").send_keys(name)   #输入新的昵称
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    #点击保存
        # 修改性别
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        # 判断输入的条件是女生还是男生还是其他,再去点击
        if sex_text == '男':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvBoy").click()
        elif sex_text=='女':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvGirl").click()
        else:
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvOther").click()
        # 修改地址
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        time.sleep(5)
        test = Redact_Message(self.driver)
        test.swipeUp()
        self.driver.find_element_by_xpath("//*[@text='云南省']").click()               #选择省份
        self.driver.find_element_by_xpath("//*[@text='丽江市']").click()
        self.driver.find_element_by_xpath("//*[@text='宁蒗彝族自治县']").click()

    def update_case08(self,name='测试账号4',sex_text= '其他'):
        '''修改昵称、性别、地区、日期'''
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
        # 修改性别
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        # 判断输入的条件是女生还是男生还是其他,再去点击
        if sex_text == '男':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvBoy").click()
        elif sex_text=='女':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvGirl").click()
        else:
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvOther").click()
        # 修改地址
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        time.sleep(5)
        test = Redact_Message(self.driver)
        test.swipeUp()
        self.driver.find_element_by_xpath("//*[@text='西藏自治区']").click()               #选择省份
        self.driver.find_element_by_xpath("//*[@text='那曲市']").click()
        self.driver.find_element_by_xpath("//*[@text='安多县']").click()
        # 修改日期
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          #点击日期栏
        self.driver.swipe(start_x=135,start_y=791,end_x=159,end_y=1100)     #   年
        self.driver.swipe(start_x=393,start_y=791,end_x=574,end_y=993)      #   月
        self.driver.swipe(start_x=568,start_y=791,end_x=600,end_y=136)      #   日
        self.driver.find_element_by_xpath("//*[@text='确定']").click()

    def update_case09(self,sex_text='男'):
        '''修改头像、性别、地区、日期'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改头像
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_changehead").click()    # 修改头像
        self.driver.find_element_by_xpath("//*[@text='拍照']").click()
        self.driver.find_element_by_id("com.oppo.camera:id/shutter_button").click()         #点击拍照按钮
        self.driver.find_element_by_id("com.oppo.camera:id/btn_done").click()               #选择照片按钮
        self.driver.find_element_by_id("com.coloros.gallery3d:id/action_apply").click()     #裁剪照片-确定按钮
        # 修改性别
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        # 判断输入的条件是女生还是男生还是其他,再去点击
        if sex_text == '男':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvBoy").click()
        elif sex_text=='女':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvGirl").click()
        else:
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvOther").click()
        # 修改地址
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        time.sleep(5)
        test = Redact_Message(self.driver)
        test.swipeUp()
        self.driver.find_element_by_xpath("//*[@text='陕西省']").click()               #选择省份
        self.driver.find_element_by_xpath("//*[@text='西安市']").click()
        self.driver.find_element_by_xpath("//*[@text='雁塔区']").click()
        # 修改日期
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          #点击日期栏
        self.driver.swipe(start_x=152,start_y=791,end_x=140,end_y=1120)     #   年
        self.driver.swipe(start_x=363,start_y=791,end_x=536,end_y=895)      #   月
        self.driver.swipe(start_x=578,start_y=791,end_x=598,end_y=153)      #   日
        self.driver.find_element_by_xpath("//*[@text='确定']").click()

    def update_case10(self,name='测试账号3'):
        '''修改头像、昵称、地区、日期'''
         # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改头像
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_changehead").click()    # 修改头像
        self.driver.find_element_by_xpath("//*[@text='拍照']").click()
        self.driver.find_element_by_id("com.oppo.camera:id/shutter_button").click()         # 点击拍照按钮
        self.driver.find_element_by_id("com.oppo.camera:id/btn_done").click()               # 选择照片按钮
        self.driver.find_element_by_id("com.coloros.gallery3d:id/action_apply").click()     # 裁剪照片-确定按钮
        # 修改昵称
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    # 点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       # 清空昵称
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").send_keys(name)   # 输入新的昵称
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    # 点击保存
        # 修改地址
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        time.sleep(5)
        test = Redact_Message(self.driver)
        test.swipeUp()
        # self.driver.swipe(start_x=0,start_y=125,end_x=720,end_y=1280)         # 调用滑动方法
        self.driver.find_element_by_xpath("//*[@text='甘肃省']").click()               # 选择省份
        self.driver.find_element_by_xpath("//*[@text='陇南市']").click()
        self.driver.find_element_by_xpath("//*[@text='武都区']").click()
        # 修改日期
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          # 点击日期栏
        self.driver.swipe(start_x=153,start_y=791,end_x=289,end_y=1080)     #   年
        self.driver.swipe(start_x=363,start_y=791,end_x=536,end_y=849)      #   月
        self.driver.swipe(start_x=536,start_y=791,end_x=587,end_y=154)      #   日
        self.driver.find_element_by_xpath("//*[@text='确定']").click()

    def update_case11(self,name='测试账号2',sex_text='男'):
        '''修改头像、昵称、性别、日期'''
         # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改头像
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_changehead").click()    # 修改头像
        self.driver.find_element_by_xpath("//*[@text='拍照']").click()
        self.driver.find_element_by_id("com.oppo.camera:id/shutter_button").click()         #点击拍照按钮
        self.driver.find_element_by_id("com.oppo.camera:id/btn_done").click()               #选择照片按钮
        self.driver.find_element_by_id("com.coloros.gallery3d:id/action_apply").click()     #裁剪照片-确定按钮
        # 修改昵称
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    #点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       #清空昵称
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").send_keys(name)   #输入新的昵称
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    #点击保存
        # 修改性别
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        # 判断输入的条件是女生还是男生还是其他,再去点击
        if sex_text == '男':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvBoy").click()
        elif sex_text=='女':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvGirl").click()
        else:
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvOther").click()
        # 修改日期
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          #点击日期栏
        self.driver.swipe(start_x=150,start_y=791,end_x=136,end_y=1080)     #   年
        self.driver.swipe(start_x=390,start_y=791,end_x=523,end_y=889)      #   月
        self.driver.swipe(start_x=564,start_y=791,end_x=592,end_y=151)      #   日
        self.driver.find_element_by_xpath("//*[@text='确定']").click()

    def update_case12(self,sex_text='其他',name='测试账号1'):
        '''修改头像、昵称、性别'''
         # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改头像
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_changehead").click()    # 修改头像
        self.driver.find_element_by_xpath("//*[@text='拍照']").click()
        self.driver.find_element_by_id("com.oppo.camera:id/shutter_button").click()         #点击拍照按钮
        self.driver.find_element_by_id("com.oppo.camera:id/btn_done").click()               #选择照片按钮
        self.driver.find_element_by_id("com.coloros.gallery3d:id/action_apply").click()     #裁剪照片-确定按钮
        # 修改昵称
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    #点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       #清空昵称
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").send_keys(name)   #输入新的昵称
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    #点击保存
        # 修改性别
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        # 判断输入的条件是女生还是男生还是其他,再去点击
        if sex_text == '男':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvBoy").click()
        elif sex_text=='女':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvGirl").click()
        else:
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvOther").click()

    def update_case13(self,name='测试账号哟'):
        '''修改头像、昵称、地区'''
         # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改头像
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_changehead").click()    # 修改头像
        self.driver.find_element_by_xpath("//*[@text='拍照']").click()
        self.driver.find_element_by_id("com.oppo.camera:id/shutter_button").click()         #点击拍照按钮
        self.driver.find_element_by_id("com.oppo.camera:id/btn_done").click()               #选择照片按钮
        self.driver.find_element_by_id("com.coloros.gallery3d:id/action_apply").click()     #裁剪照片-确定按钮
        # 修改昵称
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    #点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       #清空昵称
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").send_keys(name)   #输入新的昵称
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    #点击保存
        # 修改地址
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        time.sleep(5)
        test = Redact_Message(self.driver)
        test.swipeUp()
        self.driver.find_element_by_xpath("//*[@text='山西省']").click()               #选择省份
        self.driver.find_element_by_xpath("//*[@text='大同市']").click()
        self.driver.find_element_by_xpath("//*[@text='左云县']").click()

    def update_case14(self,name='新的昵称'):
        '''修改头像、昵称、日期'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改头像
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_changehead").click()    # 修改头像
        self.driver.find_element_by_xpath("//*[@text='拍照']").click()
        self.driver.find_element_by_id("com.oppo.camera:id/shutter_button").click()         #点击拍照按钮
        self.driver.find_element_by_id("com.oppo.camera:id/btn_done").click()               #选择照片按钮
        self.driver.find_element_by_id("com.coloros.gallery3d:id/action_apply").click()     #裁剪照片-确定按钮
        # 修改昵称
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    #点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       #清空昵称
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").send_keys(name)   #输入新的昵称
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    #点击保存
        # 修改日期
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          #点击日期栏
        self.driver.swipe(start_x=299,start_y=791,end_x=236,end_y=1063)     #   年
        self.driver.swipe(start_x=388,start_y=791,end_x=564,end_y=999)      #   月
        self.driver.swipe(start_x=577,start_y=791,end_x=599,end_y=263)      #   日
        self.driver.find_element_by_xpath("//*[@text='确定']").click()

    def update_case15(self, name='qwer', sex_text='其他'):
        '''修改昵称、性别、地区'''
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
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        # 判断输入的条件是女生还是男生还是其他,再去点击
        if sex_text == '男':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvBoy").click()
        elif sex_text=='女':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvGirl").click()
        else:
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvOther").click()
        # 修改地址
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        time.sleep(5)
        test = Redact_Message(self.driver)
        test.swipeUp()
        self.driver.find_element_by_xpath("//*[@text='北京市']").click()               #选择省份
        self.driver.find_element_by_xpath("//*[@text='市辖区']").click()
        self.driver.find_element_by_xpath("//*[@text='丰台区']").click()

    def update_case16(self,name='点歌货我',sex_text='男'):
        '''修改昵称、性别、日期'''
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
        self.wait()
        # 修改性别
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()
        # 判断输入的条件是女生还是男生还是其他,再去点击
        if sex_text == '男':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvBoy").click()
        elif sex_text=='女':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvGirl").click()
        else:
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvOther").click()
        # 修改日期
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          #点击日期栏
        self.driver.swipe(start_x=150,start_y=791,end_x=136,end_y=1080)     #   年
        self.driver.swipe(start_x=390,start_y=791,end_x=523,end_y=889)      #   月
        self.driver.swipe(start_x=564,start_y=791,end_x=592,end_y=151)      #   日
        self.driver.find_element_by_xpath("//*[@text='确定']").click()

    def update_case17(self, sex_text='女'):
        '''修改性别、地区、日期'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改性别
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        # 判断输入的条件是女生还是男生还是其他,再去点击
        if sex_text == '男':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvBoy").click()
        elif sex_text=='女':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvGirl").click()
        else:
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvOther").click()
        # 修改日期
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          #点击日期栏
        self.driver.swipe(start_x=154,start_y=791,end_x=156,end_y=1280)     #   年
        self.driver.swipe(start_x=393,start_y=791,end_x=541,end_y=999)      #   月
        self.driver.swipe(start_x=566,start_y=791,end_x=623,end_y=125)      #   日
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        # 修改地址
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        time.sleep(5)
        test = Redact_Message(self.driver)
        test.swipeUp()
        self.driver.find_element_by_xpath("//*[@text='湖南省']").click()               #选择省份
        self.driver.find_element_by_xpath("//*[@text='邵阳市']").click()
        self.driver.find_element_by_xpath("//*[@text='隆回县']").click()
    def update_case18(self, sex_text = '男'):
        '''修改性别、日期'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改性别
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        # 判断输入的条件是女生还是男生还是其他,再去点击
        if sex_text == '男':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvBoy").click()
        elif sex_text == '女':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvGirl").click()
        else:
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvOther").click()
        # 修改日期
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          #点击日期栏
        self.driver.swipe(start_x=150, start_y=791, end_x=136, end_y=1080)     #   年
        self.driver.swipe(start_x=390, start_y=791, end_x=523, end_y=889)      #   月
        self.driver.swipe(start_x=564, start_y=791, end_x=592, end_y=151)      #   日
        self.driver.find_element_by_xpath("//*[@text='确定']").click()

    def update_case19(self):
        '''修改地区、日期'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改日期
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          #点击日期栏
        self.driver.swipe(start_x=100,start_y=791,end_x=200,end_y=1056)     #   年
        self.driver.swipe(start_x=388,start_y=791,end_x=654,end_y=900)      #   月
        self.driver.swipe(start_x=511,start_y=791,end_x=623,end_y=161)      #   日
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        # 修改地址
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        time.sleep(5)
        test = Redact_Message(self.driver)
        test.swipeUp()
        self.driver.find_element_by_xpath("//*[@text='湖南省']").click()               #选择省份
        self.driver.find_element_by_xpath("//*[@text='长沙市']").click()
        self.driver.find_element_by_xpath("//*[@text='芙蓉区']").click()

    def update_case20(self):
        '''修改头像、地区、日期'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改日期
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          #点击日期栏
        self.driver.swipe(start_x=150,start_y=791,end_x=136,end_y=1080)     #   年
        self.driver.swipe(start_x=390,start_y=791,end_x=523,end_y=889)      #   月
        self.driver.swipe(start_x=564,start_y=791,end_x=592,end_y=151)      #   日
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        # 修改地址
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        time.sleep(5)
        test = Redact_Message(self.driver)
        test.swipeUp()
        self.driver.find_element_by_xpath("//*[@text='湖南省']").click()               #选择省份
        self.driver.find_element_by_xpath("//*[@text='衡阳市']").click()
        self.driver.find_element_by_xpath("//*[@text='蒸湘区']").click()
        # 修改头像
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_changehead").click()    # 修改头像
        self.driver.find_element_by_xpath("//*[@text='拍照']").click()
        self.driver.find_element_by_id("com.oppo.camera:id/shutter_button").click()         #点击拍照按钮
        self.driver.find_element_by_id("com.oppo.camera:id/btn_done").click()               #选择照片按钮
        self.driver.find_element_by_id("com.coloros.gallery3d:id/action_apply").click()     #裁剪照片-确定按钮

    def update_case21(self):
        '''修改头像、日期'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改日期
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          #点击日期栏
        self.driver.swipe(start_x=154,start_y=791,end_x=154,end_y=1080)     #   年
        self.driver.swipe(start_x=389,start_y=791,end_x=625,end_y=998)      #   月
        self.driver.swipe(start_x=547,start_y=791,end_x=600,end_y=457)      #   日
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        # 修改头像
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_changehead").click()    # 修改头像
        self.driver.find_element_by_xpath("//*[@text='拍照']").click()
        self.driver.find_element_by_id("com.oppo.camera:id/shutter_button").click()         #点击拍照按钮
        self.driver.find_element_by_id("com.oppo.camera:id/btn_done").click()               #选择照片按钮
        self.driver.find_element_by_id("com.coloros.gallery3d:id/action_apply").click()     #裁剪照片-确定按钮

    def update_case22(self, name='修改我以后'):
        '''修改头像、昵称'''
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
         # 修改头像
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_changehead").click()    # 修改头像
        self.driver.find_element_by_xpath("//*[@text='拍照']").click()
        self.driver.find_element_by_id("com.oppo.camera:id/shutter_button").click()         #点击拍照按钮
        self.driver.find_element_by_id("com.oppo.camera:id/btn_done").click()               #选择照片按钮
        self.driver.find_element_by_id("com.coloros.gallery3d:id/action_apply").click()     #裁剪照片-确定按钮

    def update_case23(self, sex_text='女'):
        '''修改头像、性别'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改头像
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_changehead").click()    # 修改头像
        self.driver.find_element_by_xpath("//*[@text='拍照']").click()
        self.driver.find_element_by_id("com.oppo.camera:id/shutter_button").click()         #点击拍照按钮
        self.driver.find_element_by_id("com.oppo.camera:id/btn_done").click()               #选择照片按钮
        self.driver.find_element_by_id("com.coloros.gallery3d:id/action_apply").click()     #裁剪照片-确定按钮
        # 修改性别
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        # 判断输入的条件是女生还是男生还是其他,再去点击
        if sex_text == '男':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvBoy").click()
        elif sex_text=='女':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvGirl").click()
        else:
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvOther").click()

    def update_case24(self):
        '''修改头像、地区'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改头像
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_changehead").click()    # 修改头像
        self.driver.find_element_by_xpath("//*[@text='拍照']").click()
        self.driver.find_element_by_id("com.oppo.camera:id/shutter_button").click()         #点击拍照按钮
        self.driver.find_element_by_id("com.oppo.camera:id/btn_done").click()               #选择照片按钮
        self.driver.find_element_by_id("com.coloros.gallery3d:id/action_apply").click()     #裁剪照片-确定按钮
        # 修改地址
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        time.sleep(5)
        test = Redact_Message(self.driver)
        test.swipeUp()
        self.driver.find_element_by_xpath("//*[@text='内蒙古自治区']").click()               #选择省份
        self.driver.find_element_by_xpath("//*[@text='包头市']").click()
        self.driver.find_element_by_xpath("//*[@text='包头稀土高新技术开发区']").click()

    def update_case25(self,name='修改的昵称',sex_text='其他'):
        '''修改昵称、性别'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改性别
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        # 判断输入的条件是女生还是男生还是其他,再去点击
        if sex_text == '男':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvBoy").click()
        elif sex_text=='女':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvGirl").click()
        else:
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvOther").click()
        # 修改昵称
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_username_layout").click()    #点击昵称栏目
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").clear()       #清空昵称
        self.driver.find_element_by_id("com.jsmapp.jsm:id/personal_edit").send_keys(name)   #输入新的昵称
        self.driver.find_element_by_xpath("//*[@text='保存']").click()    #点击保存

    def update_case26(self,name='啦啦啦啦'):
        '''修改昵称、地区'''
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
        # 修改地址
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        time.sleep(5)
        test = Redact_Message(self.driver)
        test.swipeUp()
        self.driver.find_element_by_xpath("//*[@text='新疆维吾尔自治区']").click()               #选择省份
        self.driver.find_element_by_xpath("//*[@text='克孜勒苏柯尔克孜自治州']").click()
        self.driver.find_element_by_xpath("//*[@text='乌恰县']").click()

    def update_case27(self,name='assassin'):
        '''修改昵称、日期'''
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
         # 修改日期
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_born").click()          #点击日期栏
        self.driver.swipe(start_x=156,start_y=791,end_x=156,end_y=1025)     #   年
        self.driver.swipe(start_x=395,start_y=791,end_x=525,end_y=888)      #   月
        self.driver.swipe(start_x=568,start_y=791,end_x=600,end_y=154)      #   日
        self.driver.find_element_by_xpath("//*[@text='确定']").click()

    def update_case28(self,sex_text='男'):
        '''修改性别、地区'''
        # 切换到我的页面
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me").click()
        # 点击个人信息按钮
        self.driver.find_element_by_id("com.jsmapp.jsm:id/me_user_layout").click()
        # 修改性别
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_me_sex").click()           # 点击性别栏目
        # 判断输入的条件是女生还是男生还是其他,再去点击
        if sex_text == '男':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvBoy").click()
        elif sex_text=='女':
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvGirl").click()
        else:
            self.driver.find_element_by_id("com.jsmapp.jsm:id/tvOther").click()
        # 修改地址
        self.wait()
        self.driver.find_element_by_id("com.jsmapp.jsm:id/ll_get_region").click()       # 点击地址栏目
        time.sleep(5)
        test = Redact_Message(self.driver)
        test.swipeUp()
        self.driver.find_element_by_xpath("//*[@text='安徽省']").click()               #选择省份
        self.driver.find_element_by_xpath("//*[@text='合肥市']").click()
        self.driver.find_element_by_xpath("//*[@text='长丰县']").click()

    def get_nickname_success(self):
        '''获取昵称更改成功后的信息'''
        result = self.get_text("com.jsmapp.jsm:id/personal_name")
        return result

    def get_sex_success(self):
        '''获取性别更改成功的信息'''
        result = self.get_text("com.jsmapp.jsm:id/tv_me_sex")
        return result

    def get_address_success(self):
        '''获取地址更改成功的信息'''
        result = self.get_text("com.jsmapp.jsm:id/tv_personal_region")
        return result

    def get_date_success(self):
        '''获取日期更改成功的信息'''
        result = self.get_text("com.jsmapp.jsm:id/tv_me_born")
        return result

if __name__ == '__main__':
    app =start_app()
    test_update = Redact_Message(app)

    # 测试修改五种资料信息
    # test_update.update_case06()
    # res = []
    # res.append(test_update.get_nickname_success())
    # res.append(test_update.get_sex_success())
    # res.append(test_update.get_address_success())
    # res.append(test_update.get_date_success())
    #
    # print(res)
    # exp =['人这一生呐','女','贵州省铜仁市','2018-05-02']
    #
    # for x, y in zip(res, exp):
    #     print(x,y)
    #     assert x in y


    test_update.update_adress_case04()
    res = test_update.is_toast_in("保存成功")
    print(res)
    exp = "保存成功"
    assert res != exp









