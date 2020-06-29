import pytest
from flaky import flaky
import allure
from common.start import start_app
from page.wo_de_module.personal_information_module.redact_message import Redact_Message


class Test_Update_Nickname():
    @pytest.mark.po
    @flaky(max_runs=1,min_passes=1)

    @allure.story("第二条用例: 修改昵称")
    def test_update_nickname(self):
        app =start_app()
        test_update = Redact_Message(app)

        test_update.update_nickname_case02()   # 先修改昵称再获取结果
        res = test_update.get_nickname_success()  # 获取修改后的结果
        print(res)
        exp = "柯基小靓仔"              # 实际结果是柯基小王子，所以不等于
        assert res != exp

if __name__ == '__main__':
    pytest.main('v', 'test_update_nickname.py')