from page.wo_de_module.redact_message import Redact_Message
import pytest
from flaky import flaky
from common.start import start_app
import allure

class Test_Update_Sex():
    @pytest.mark.po
    @flaky(max_runs=1,min_passes=1)

    @allure.story("第三条用例:修改性别")
    def test_update_sex(self):
        app =start_app()
        test_update = Redact_Message(app)

        test_update.update_sex()
        res = test_update.is_toast_in("保存成功")
        print(res)
        exp = "保存成功"
        assert res!=exp

if __name__ == '__main__':
    pytest.main(['-v','test_update_sex.py'])