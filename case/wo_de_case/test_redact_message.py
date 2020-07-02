from page.wo_de_module.personal_information_module.redact_message import Redact_Message
from flaky import flaky
import pytest
import allure
import conftest
class Test_Redact_Message():

    @pytest.mark.po
    @flaky(max_runs=1, min_passes=1)
    @allure.feature("第一条测试用例: 修改头像")
    def test_update_case01(self, startapp):

        test_update = Redact_Message(startapp)
        test_update.update_photo_case01()
        res = test_update.is_toast_in("保存成功")
        print(res)
        exp = "保存成功"
        assert res != exp

    @allure.story("第二条用例: 修改昵称")
    def test_update_case02(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_nickname_case02()  # 先修改昵称再获取结果

        res = test_update.get_nickname_success()  # 获取修改后的结果
        print(res)
        exp = "柯基小王子"
        assert res == exp

    @allure.story("第三条测试用例: 修改性别")
    def test_update_case03(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_sex_case03()

        res = test_update.get_sex_success()
        print(res)
        exp = "男"
        assert res == exp

    @allure.story("第四条测试用例: 修改地址")
    def test_update_case04(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_adress_case04()

        res = test_update.get_address_success()
        print(res)
        exp = "四川省乐山市"
        assert res == exp

    @allure.story("第五条用例: 修改日期")
    def test_update_case05(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_date_case05()

        res = test_update.is_toast_in("保存成功")
        print(res)
        exp = "保存成功"
        assert res != exp

    @allure.story("第六条测试用例: 修改头像、昵称、性别、地址、日期")
    def test_update_case06(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case06()
        res = []
        res.append(test_update.get_nickname_success())
        res.append(test_update.get_sex_success())
        res.append(test_update.get_address_success())
        print(res)

        exp = ['魔力转圈圈', '男', '广东省韶关市']
        for x, y in zip(res, exp):
            print(x, y)
            assert x == y

    @allure.story("第七条测试用例: 修改头像、昵称、性别、地址")
    def test_update_case07(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case07()

        res = []
        res.append(test_update.get_nickname_success())
        res.append(test_update.get_sex_success())
        res.append(test_update.get_address_success())
        print(res)

        exp =['测试账号5', '其它', '云南省丽江市']
        for x, y in zip(res, exp):
            print(x, y)
            assert x in y

    @allure.story("第八条测试用例: 修改昵称、性别、地区、日期")
    def test_update_case08(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case08()

        res = []
        res.append(test_update.get_nickname_success())
        res.append(test_update.get_sex_success())
        res.append(test_update.get_address_success())
        print(res)

        exp = ['测试账号4', '其它', '西藏自治区那曲市']
        for x, y in zip(res, exp):
            print(x, y)
            assert x == y

    @allure.story("第九条测试用例: 修改头像、性别、地区、日期")
    def test_update_case09(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case09()

        res = []
        res.append(test_update.get_sex_success())
        res.append(test_update.get_address_success())
        print(res)

        exp = ['男', '广东省深圳市']
        for x, y in zip(res, exp):
            print(x, y)
            assert x == y

    @allure.story("第十条测试用例: 修改头像、昵称、地区、日期")
    def test_update_case10(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case10()

        res = []
        res.append(test_update.get_nickname_success())
        res.append(test_update.get_address_success())
        print(res)

        exp = ['测试账号3', '甘肃省陇南市']
        for x, y in zip(res, exp):
            print(x, y)
            assert x == y

    @allure.story("第十一条测试用例: 修改头像、昵称、性别、日期")
    def test_update_case11(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case11()

        res = []
        res.append(test_update.get_nickname_success())
        res.append(test_update.get_sex_success())
        print(res)

        exp = ['测试账号2', '男']
        for x, y in zip(res, exp):
            print(x, y)
            assert x == y

    @allure.story("第十二条测试用例: 修改头像、昵称、性别")
    def test_update_case12(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case12()

        res =[]
        res.append(test_update.get_nickname_success())
        res.append(test_update.get_sex_success())

        exp =['测试账号1', '其它']
        for x, y in zip(res, exp):
            print(x, y)
            assert x == y

    @allure.story("第十三条测试用例: 修改头像、昵称、地区")
    def test_update_case13(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case13()

        res = []
        res.append(test_update.get_nickname_success())
        res.append(test_update.get_address_success())

        exp =['测试账号哟', '山西省大同市']
        for x, y in zip(res, exp):
            print(x, y)
            assert x == y

    @allure.story("第十四条用例: 修改头像、昵称、日期")
    def test_update_case14(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case14()

        res = test_update.get_nickname_success()
        print(res)
        exp = '新的昵称'
        assert res == exp

    @allure.story("第十五条用例: 修改昵称、性别、地区")
    def test_update_case15(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case15()

        res = []
        res.append(test_update.get_nickname_success())
        res.append(test_update.get_sex_success())
        res.append(test_update.get_address_success())
        exp = ['qwer', '其它', '北京市市辖区']
        for x, y in zip(res, exp):
            print(x, y)
            assert x == y

    @allure.story("第十六条用例: 修改昵称、性别、日期")
    def test_update_case16(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case16()

        res = []
        res.append(test_update.get_nickname_success())
        res.append(test_update.get_sex_success())
        print(res)

        exp =['点歌货我', '男']
        for x, y in zip(res, exp):
            print(x, y)
            assert x == y

    @allure.story("第十七条用例: 修改性别、地区、日期")
    def test_update_case17(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case17()

        res = []
        res.append(test_update.get_sex_success())
        res.append(test_update.get_address_success())
        print(res)

        exp = ['女', '湖南省邵阳市']
        for x, y in zip(res, exp):
            print(x, y)
            assert x == y

    @allure.story("第十八条用例：修改性别、日期")
    def test_update_case18(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case18()

        res = test_update.get_sex_success()
        print(res)
        exp = '男'
        assert res == exp

    @allure.story("第十九条用例: 修改地区、日期")
    def test_update_case19(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case19()

        res = test_update.get_address_success()
        exp ='湖南省长沙市'
        print(res)
        assert res == exp

    @allure.story("第二十条用例: 修改头像、地区、日期")
    def test_update_case20(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case20()

        res = test_update.get_address_success()
        print(res)
        exp = '湖南省衡阳市'
        assert res == exp

    @allure.story("第二十一条用例: 修改头像、日期")
    def test_update_case21(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case21()

        res = test_update.is_toast_in("保存成功")
        exp = '保存成功'
        assert res != exp

    @allure.story("第二十二条用例: 修改头像、昵称")
    def test_update_case22(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case22()

        res = test_update.get_nickname_success()
        exp = '修改我以后'
        assert res == exp

    @allure.story("第二十三条用例: 修改头像、性别")
    def test_update_case23(self, startapp):

        test_update = Redact_Message(startapp)
        test_update.update_case23()

        res = test_update.get_sex_success()
        exp = '女'
        assert res == exp

    @allure.story("第二十四条用例: 修改头像、地区")
    def test_update_case24(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case24()

        res = test_update.get_sex_success()
        exp = '内蒙古自治区包头市'
        assert res == exp

    @allure.story("第二十五条用例: 修改昵称、性别")
    def test_update_case25(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case25()

        res = []
        res.append(test_update.get_nickname_success())
        res.append(test_update.get_sex_success())
        exp = ['修改的昵称', '其它']
        assert res == exp

    @allure.story("第二十六条用例: 修改昵称、地区")
    def test_update_case26(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case26()

        res = []
        res.append(test_update.get_nickname_success())
        res.append(test_update.get_address_success())
        exp = ['啦啦啦啦', '新疆维吾尔自治区克孜勒苏柯尔克孜自治州']
        for x,y in zip(res,exp):
            print(x, y)
            assert res == exp

    @allure.story("第二十七条用例: 修改昵称、日期")
    def test_update_case27(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case27()

        res = []
        res.append(test_update.get_nickname_success())
        res.append(test_update.is_toast_in("保存成功"))
        exp = ['assassin', '保存成功']
        for x,y in zip(res, exp):
            print(x, y)
            assert res == exp

    @allure.story("第二十八条用例: 修改性别、地区")
    def test_update_case28(self, startapp):
        test_update = Redact_Message(startapp)
        test_update.update_case28()

        res = []
        res.append(test_update.get_sex_success())
        res.append(test_update.get_address_success())

        exp = ['男', '安徽省合肥市']
        for x, y in zip(res, exp):
            print(x, y)
            assert res == exp

if __name__ == '__main__':
    pytest.main('-v', 'test_redact_message.py')
    xx = Test_Redact_Message()
    xx.test_update_case01()
