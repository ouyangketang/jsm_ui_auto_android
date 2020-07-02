from page.login_module.pwd_login import Test_Pwd_Login
import pytest
from flaky import flaky
import allure
import conftest
class Test_Pwd_Login_Case():

    @pytest.mark.po
    @flaky(max_runs=1, min_passes=1)
    @allure.story("第一条测试用例:手机号格式错误")
    def test_pwd_login01(self, startapp):
        test_pwd_login = Test_Pwd_Login(startapp)
        test_pwd_login.pwd_login01()

        res = test_pwd_login.is_toast_in("账号不存在")
        exp = "账号不存在"
        assert res != exp

    @allure.story("第二条测试用例:手机号位数错误")
    def test_pwd_login02(self, startapp):
        test_pwd_login = Test_Pwd_Login(startapp)
        test_pwd_login.pwd_login02()
        res = test_pwd_login.is_toast_in("账号不存在")
        exp = "账号不存在"
        assert res != exp

    @allure.story("第三条测试用例:密码错误")
    def test_pwd_login03(self, startapp):
        test_pwd_login = Test_Pwd_Login(startapp)
        test_pwd_login.pwd_login03()

        res = test_pwd_login.is_toast_in("密码错误")
        exp = "密码错误"
        assert res != exp

    @allure.story("第五条用例:密码有空格")
    def test_pwd_login05(self, startapp):
        test_pwd_login = Test_Pwd_Login(startapp)
        test_pwd_login.pwd_login05()

        res = test_pwd_login.is_toast_in("密码格式错误")
        exp = "密码格式错误"
        assert res != exp

    @allure.story("第六条用例:正确的手机号和密码，登录成功")
    def test_pwd_login06(self, startapp):
        test_pwd_login = Test_Pwd_Login(startapp)
        test_pwd_login.pwd_login06()
        res = test_pwd_login.get_success()
        print(res)
        exp = "我是你的谁"
        assert res != exp

if __name__ == '__main__':
    pytest.main(['-v', 'test_pwd_login.py'])

