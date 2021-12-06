import pytest
from time import sleep
from selenium import webdriver
from page.login_page import Loginpage
import allure


@allure.feature('登录')
class Test_login:
    # 环境准备 前置条件
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.pingcheng.gov.cn/page/admin_zyq/')
        cls.driver.find_element_by_css_selector('.login_btn').click()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        # cls.driver.save_screenshot("../share/1.png")

    @allure.feature('若验证码错误，可循环登录十次')
    def test_login(self):
        for i in range(10):
            currdir = 'D:/Program Files/JetBrains/PyCharm Community Edition 2020.2/pytest_allure/share'
            page = Loginpage(self.driver)
            page.get_picture(currdir)
            page.search_username("18710001032")
            page.search_password("bgfg1000lbfwlXP#")
            page.sleep(2)
            page.search_code(currdir)
            page.click_login()
            sleep(2)
            url = page.get_url()
            if url != 'http://111.53.13.251:3100/loginPage?error':
                # assert page.get_url() == 'http://sqwytst.wt.com:14352/dashboard'
                assert page.get_title() == '大同市“普惠、转型、绿色”政银企融资对接平台'
                break
            else:
                page.get_picture(currdir)
                continue
        page.search_job('/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[3]/table/tbody/tr/td[2]/div/label/span[1]/span')
        page.login_job('/html/body/div[1]/div/div[2]/div/div/div[3]/div/button[2]')

    # 环境清理
    # @classmethod
    # def teardown_class(cls):
    #     sleep(2)
    #     cls.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_zyq_login.py'])
