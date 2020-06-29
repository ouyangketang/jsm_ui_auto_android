from page.wo_de_module.personal_information_module.redact_message_other import Redact_Message_Other
from flaky import flaky
import pytest
import allure
from common.start import start_app
from page.wo_de_module.personal_information_module.redact_message import Redact_Message

class Test_Redact_Message_Other():
    @pytest.mark
    @flaky(max_runs=1, min_passes=1)

    @allure.story("第一条用例: 昵称输入空格情况")
    def test_update_case_error01(self):
        app = start_app()
        test_update = Redact_Message_Other(app)
        test_update.update_nickname_error01()
        res = test_update.is_toast_in("请填写昵称")
        exp = '请填写昵称'
        assert res == exp

    @allure.story("第二条用例: 昵称英文输入符号")
    def test_update_case_error02(self):
        app = start_app()
        test_update = Redact_Message_Other(app)
        test_update.update_nickname_error02()
        res = test_update.is_toast_in("保存成功")
        exp = '保存成功'
        assert res == exp

    @allure.story("第三条用例: 昵称清空后保存")
    def test_update_case_error03(self):
        app = start_app()
        test_update = Redact_Message_Other(app)
        test_update.update_nickname_error03()
        res = test_update.is_toast_in("请填写昵称")
        exp = '请填写昵称'
        assert res == exp

    @allure.story("第四条用例: 昵称清空后手机物理键返回")
    def test_update_case_error04(self):
        app = start_app()
        test_update = Redact_Message_Other(app)
        test_update.update_nickname_error03()

        test_res = Redact_Message(app)
        res = test_res.get_nickname_success()
        exp = 'assassin'
        assert res == exp

    @allure.story("第五条用例: 点击性别后点击取消按钮")
    def test_update_case_error05(self):
        app = start_app()
        test_update = Redact_Message_Other(app)
        test_update.update_sex_error01()

        test_res = Redact_Message(app)
        res = test_res.get_sex_success()
        exp = '男'
        assert res == exp

    @allure.story("第六条用例: 点击日期后点击取消按钮")
    def test_update_case_error06(self):
        app = start_app()
        test_update = Redact_Message_Other(app)
        test_update.update_date_error01()

        test_res = Redact_Message(app)
        res = test_res.get_date_success()
        exp = '2013-08-12'
        assert res != exp

    @allure.story("第七条用例: 进入地址栏后点击物理返回键")
    def test_update_case_error07(self):
        app= start_app()
        test_update = Redact_Message_Other(app)
        test_update.update_address_error01()

        test_res = Redact_Message(app)
        res = test_res.get_address_success()
        exp = '安徽省合肥市'
        assert res == exp

if __name__ == '__main__':
    pytest.main('-v', 'test_redact_message_other.py')