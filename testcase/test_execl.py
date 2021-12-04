# -*- coding:utf-8 -*-
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pytest
import allure
from common import login
from common.ReadTabDataUtils import read_test_data
import json

@pytest.mark.run(order=3)
@allure.feature("登录模块")
class Test_Login:


    @allure.story("登录模块测试")
    @allure.title("登录测试用例")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("登录功能：用户名和密码校验")
    @allure.step("登录模块")
    @pytest.mark.parametrize("req_data,exc_data",read_test_data("../test_data/接口自动化用例设计.xls","登录",None,7,9))
    def test_login(self,req_data,exc_data):
        res_text = login.login(json.loads(req_data))
        assert res_text == json.loads(exc_data)
