import pytest
from pytest import assume
from page.apply_page import Applypage
from page.login_page import Loginpage
from time import sleep
from selenium import webdriver
import allure
# from common.login import Login


@allure.feature('登录后操作申请管理模块')
class Test_apply:
    # 环境准备 前置条件
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://sqwytst.wt.com:14352/')
        cls.driver.find_element_by_css_selector('.login_btn').click()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

        # cls.driver.save_screenshot("../share/1.png")

    @allure.feature('若验证码错误，登录可循环登录十次')
    def test_login_case01(self):
        page = Loginpage(self.driver)
        for i in range(10):
            currdir = 'D:/Program Files/JetBrains/PyCharm Community Edition 2020.2/pytest_allure/share'
            page.get_picture(currdir)
            page.search_username("13734206025")
            page.search_password("asdqwe123")
            page.sleep(2)
            page.search_code(currdir)
            page.click_login()
            sleep(2)
            url = page.get_url()
            if url != 'http://sso.wt.com:3100/loginPage?error':
                # assert page.get_url() == 'http://sqwytst.wt.com:14352/dashboard'
                assert page.get_title() == '智慧网格综合管理平台'
                break
            else:
                page.get_picture(currdir)
                continue
        page.search_job()
        page.login_job()

    @allure.feature('按姓名查询')
    def test_apply_case01(self):
        applypage = Applypage(self.driver)
        applypage.apply_management()
        applypage.reload()
        applypage.input_name("郭燕")
        applypage.submit_select()
        sleep(2)
        assert applypage.get_name() == '郭燕'

    @allure.feature('按手机号查询')
    def test_apply_case02(self):
        applypage = Applypage(self.driver)
        applypage.apply_management()
        applypage.reload()
        applypage.input_phone("18234230290")
        applypage.submit_select()
        sleep(2)
        assert applypage.get_phone() == '18234230290'

    @allure.feature('查询平城区的岗位申请')
    def test_apply_case03(self):
        applypage = Applypage(self.driver)
        applypage.apply_management()
        applypage.reload()
        applypage.click_organization()
        sleep(1)
        applypage.select_area()
        applypage.submit_select()
        sleep(2)
        with assume: assert applypage.get_organization() == '平城区'

    @allure.feature('查询待审批申请')
    def test_apply_case04(self):
        applypage = Applypage(self.driver)
        applypage.apply_management()
        applypage.reload()
        applypage.click_status()
        sleep(1)
        applypage.select_status_pending()
        applypage.submit_select()
        sleep(2)
        with assume: assert applypage.get_status() == '待审核'

    @allure.feature('查询兼职网格员')
    def test_apply_case05(self):
        applypage = Applypage(self.driver)
        applypage.apply_management()
        applypage.reload()
        applypage.click_jobs_status()
        sleep(1)
        applypage.select_parttime()
        applypage.submit_select()
        sleep(2)
        with assume: assert applypage.get_jod_type() == '兼职网格员'

    # 环境清理
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_apply.py'])
