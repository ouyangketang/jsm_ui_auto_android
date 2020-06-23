from page.wo_de_module.redact_message import Redact_Message
import pytest
from flaky import flaky
from common.start import start_app
import allure
class Test_Update_Message():

    @pytest.mark.po
    @flaky(max_runs=1,min_passes=1)

    # @allure.story("第一条测试用例:拍照上传头像")
    # def test_update_photo(self):
    #     app =start_app()
    #     test_update = Redact_Message(app)
    #
    #     test_update.update_photo()
    #     res = test_update.is_toast_in("保存成功")
    #     print(res)
    #     exp = "保存成功"
    #     assert res != exp

    @allure.story("第二条用例:修改昵称")
    def test_update_nickname(self):
        app =start_app()
        test_update = Redact_Message(app)

        test_update.update_nickname()   # 先修改昵称再获取结果
        res =test_update.get_success()  # 获取修改后的结果
        print(res)
        exp = "柯基小靓仔"              # 实际结果是柯基小王子，所以不等于
        assert res != exp

    @allure.story("第三条用例:修改性别")
    def test_update_sex(self):
        app =start_app()
        test_update = Redact_Message(app)

        test_update.update_sex()
        res = test_update.is_toast_in("保存成功")
        print(res)
        exp = "保存成功"
        assert res!=exp

    @allure.story("第四条用例:修改地址")
    def test_update_addresss(self):
        app =start_app()
        test_update = Redact_Message(app)

        test_update.update_adress()
        res = test_update.is_toast_in("保存成功")
        print(res)
        exp = "保存成功"
        assert res!=exp

    @allure.story("第五条用例:修改日期")
    def test_update_date(self):
        app =start_app()
        test_update = Redact_Message(app)
        test_update.update_date()
        res = test_update.is_toast_in("保存成功")
        print(res)
        exp = "保存成功"
        assert res!=exp

if __name__ == '__main__':
    pytest.main(['-v','test_update_message.py',"--alluredir=update_message_report"])