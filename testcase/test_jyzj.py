import pytest
from time import sleep
from selenium import webdriver
from page.login_page import Loginpage
import allure

# 截图文件夹
img_dir_path = '../Result_jyzj_Image_Orig/'

@allure.feature('登录')
class Test_login:
    # 环境准备 前置条件
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:\Project\pytest_allure\chromedriver.exe')
        cls.driver.get('http://111.53.13.252/admin_jyzj/')
        cls.driver.find_element_by_css_selector('.login_btn').click()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        # cls.driver.save_screenshot("../share/1.png")

    @allure.feature('若验证码错误，可循环登录十次')
    def test_login(self):
        for i in range(10):
            currdir = 'D:/Project/pytest_allure/share'
            page = Loginpage(self.driver)
            page.get_picture(currdir)
            page.search_username("18511067360")
            page.search_password("F&iijuq1vX&PR")
            page.sleep(2)
            page.search_code(currdir)
            page.click_login()
            sleep(2)
            url = page.get_url()
            if url != 'http://111.53.13.251:3100/loginPage?error':
                # assert page.get_url() == 'http://sqwytst.wt.com:14352/dashboard'
                if page.get_title() == '用户授权':
                    self.driver.find_element_by_xpath('//*[@id="login"]').click()
                    assert page.get_title() == '教育之家'
                    break
                else:
                    assert page.get_title() == '教育之家'
                    break
            else:
                page.get_picture(currdir)
                continue

    # 跳过
    # @pytest.mark.skip
    @allure.feature('测试学校管理')
    def test_school(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/span/a').click()
        sleep(1)

        # 添加学校
        school_add_img = img_dir_path + 'school_add.png'
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/section/main/div[2]/button/span').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/div[1]/div/div/div[2]/form/div[1]/div/div[1]/input').send_keys('school')
        # 略去 选择类型 简介 上传图片
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/div[1]/div/div/div[3]/div/button[2]').click()
        self.driver.save_screenshot(school_add_img)
        sleep(1)

        # 查询学校
        school_inquire_img = img_dir_path + 'school_inquire.png'
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/section/div/section/main/div[1]/div/form/div[1]/div/div/input').send_keys('school')
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/section/div/section/main/div[1]/div/form/div[2]/div/button[1]').click()
        self.driver.save_screenshot(school_inquire_img)
        sleep(1)

        # 编辑学校
        school_edit_img = img_dir_path + 'school_edit.png'
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/section/main/div[3]/div[3]/table/tbody/tr[1]/td[3]/div/button[1]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/div[2]/div/div/div[3]/div/button[1]/span').click()
        self.driver.save_screenshot(school_edit_img)
        sleep(1)

        # 删除学校
        school_delete_img = img_dir_path + 'school_delete.png'
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/section/main/div[3]/div[3]/table/tbody/tr[1]/td[3]/div/button[2]/span').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]/span').click()
        self.driver.save_screenshot(school_delete_img)
        sleep(1)

























    # 环境清理
    @classmethod
    def teardown_class(cls):
        sleep(2)
        cls.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_jyzj.py'])
