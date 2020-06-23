from common.start import start_app
from page.login_module.one_key_login import One_Key_login
from flaky import flaky
import pytest
import allure
class Test_One_Key_Login():

    @pytest.mark.po()
    @flaky(max_runs=1,min_passes=1)
    @allure.story("第一条一键登录用例")
    def test_login01(self):
        app = start_app()
        test_login = One_Key_login(app)     # 调用登录的类
        test_login.one_key_login01()        # 调用第一个登录函数

        res = test_login.get_login_sucess()
        print(res)
        exp = "用户352"
        assert res in exp

    @allure.story("第二条一键登录用例")
    def test_login02(self):
        app = start_app()
        test_login = One_Key_login(app)     # 调用登录的类
        test_login.one_key_login02()        # 调用第二个登录函数

        res = test_login.get_login_sucess()
        print(res)
        exp = "用户352"
        assert res in exp

if __name__ == '__main__':
    pytest.main(['-v','test_one_key_login.py'])

