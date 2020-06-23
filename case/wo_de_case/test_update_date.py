from page.wo_de_module.redact_message import Redact_Message
import pytest
from flaky import flaky
from common.start import start_app
import allure

class Test_Update_Date():

    @pytest.mark.po
    @flaky(max_runs=1,min_passes=1)

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
    pytest.main(['-v','test_update_date.py'])