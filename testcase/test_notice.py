import pytest
from page.login_page import Loginpage
from page.notice_page import NoticePage
from selenium import webdriver
from time import sleep
import allure


@allure.feature('通知公告')
class Test_notice:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://sqwytst.wt.com:14352/')
        cls.driver.find_element_by_css_selector('.login_btn').click()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

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

    def test_add_notice01(self):
        notice = NoticePage(self.driver)
        notice.notice_management()
        notice.add()
        notice.add_title('测试')
        notice.select_iframe()
        notice.add_content()
        notice.submit()

    # 环境清理
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_notice.py'])
