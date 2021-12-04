import pytest
from time import sleep
from selenium import webdriver
from page.baidu_page import BaiduPage


class Test_baidu:
    # 环境准备 前置条件
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_baidu_case01(self):
        page = BaiduPage(self.driver)
        page.open()
        page.search_input("啦啦啦")
        page.search_button()
        sleep(2)
        assert page.get_title() == "啦啦啦_百度搜索"

    def test_baidu_case02(self):
        page = BaiduPage(self.driver)
        page.open()
        page.search_input("勺子")
        page.search_button()
        sleep(2)
        assert page.get_title() == "勺子_百度搜索"

    # 环境清理
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'tes_baidu.py'])
