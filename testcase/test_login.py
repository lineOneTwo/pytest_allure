import ddt as ddt
import pytest
from time import sleep
from selenium import webdriver
from page.login_page import Loginpage
import allure
import yaml

f = open('D:/Program Files/JetBrains/PyCharm Community Edition 2020.2/pytest_allure/data/' + 'login_data.yaml',
         encoding='utf-8')
testData = yaml.safe_load(f)


# @ddt.ddt
@allure.feature('登录')
class test_Login:
    # 环境准备 前置条件
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        # cls.driver.save_screenshot("../share/1.png")

    @ddt.data(*testData)
    def test_login_case01(self, datayaml):
        # self.driver.get('http://www.pingcheng.gov.cn/page/admin_zwfw/')
        self.driver.get(datayaml['url'])
        self.driver.find_element_by_css_selector('.login_btn').click()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        for i in range(10):
            currdir = 'D:/Program Files/JetBrains/PyCharm Community Edition 2020.2/pytest_allure/share'
            page = Loginpage(self.driver)
            page.get_picture(currdir)
            # page.search_username("18511067360")
            # page.search_password("bgfg1000lbfwlXP#")
            page.search_username(datayaml['data']['username'])
            page.search_password(datayaml['data']['password'])
            page.sleep(2)
            page.search_code(currdir)
            page.click_login()
            sleep(2)
            url = page.get_url()
            if url != 'http://111.53.13.251:3100/loginPage?error':
                # assert page.get_url() == 'http://sqwytst.wt.com:14352/dashboard'
                # assert page.get_title() == '政务服务'
                assert page.get_title() == datayaml['data']['check']
                break
            else:
                page.get_picture(currdir)
                continue

    # 环境清理
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_login.py'])
