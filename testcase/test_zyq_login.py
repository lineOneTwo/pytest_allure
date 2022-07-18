import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

from page.login_page import Loginpage
import allure


@allure.feature('登录')
class Test_login:
    # 环境准备 前置条件
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:\Project\pytest_allure\chromedriver.exe')
        cls.driver.get('http://111.53.13.252/admin_zyq/')
        cls.driver.find_element_by_css_selector('.login_btn').click()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @allure.feature('若验证码错误，可循环登录十次')
    def test_login(self):
        currdir = 'D:\Project\pytest_allure\share'
        page = Loginpage(self.driver)

        for i in range(10):
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



    @allure.feature('测试文章栏目管理')
    def test_articlecolumn(self):
        driver = self.driver
        # element1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[1]/span/li/i')
        # # 鼠标悬停
        # ActionChains(driver).move_to_element(element1).perform()
        # sleep(2)
        # driver.find_element_by_css_selector('#el-popover-3443 > a:nth-child(1) > li > div').click()

        # 打开文章栏目
        driver.get('http://111.53.13.252/admin_zyq/?code=Hst0Ng#/articleColumn')
        # 添加栏目
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]/span').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div/div[2]/form/div/div/div/input').send_keys('栏目')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div/div[3]/div/button[1]/span').click()

        # 编辑栏目
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[5]/div/button[1]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div/div[3]/div/button[2]/span').click()


        # 下级栏目
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[4]/div/button/span').click()
        sleep(1)
        # 返回上级
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]/span').click()


    @allure.feature('测试文章管理')
    def test_articleList(self):
        driver = self.driver
        # 打开文章列表
        driver.get('http://111.53.13.252/admin_zyq/?code=Hst0Ng#/articleList')
        # 点击机构列表
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/section/aside/div/div[1]/div/span[2]').click()
        # 点击添加文章按钮
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/section/main/div[3]/button/span').click()
        # 输入内容
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div[2]/form/div[1]/div/div[1]/input').send_keys('文章标题')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div[2]/form/div[2]/div/div/input').send_keys('from')

        #切换到富文本
        iframe = driver.find_element_by_id('ueditor_0')
        driver.switch_to_frame(iframe)
        driver.find_element_by_xpath('/html/body/p').send_keys('测试内容输入')
        sleep(1)
        # 跳转回到主框架页
        driver.switch_to.default_content()

        # 取消
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div[3]/div/button[1]/span')
        sleep(2)

        # 切换到已终审文章
        driver.find_element_by_xpath('//*[@id="tab-2"]')
        # 查询功能
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/section/main/div[2]/div/form/div[1]/div/div/input').send_keys('人民银行')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/section/main/div[2]/div/form/div[3]/div/button[1]').click()
        sleep(1)

        # 切换拒审文章
        driver.find_element_by_xpath('//*[@id="tab-3"]')




    # 环境清理
    # @classmethod
    # def teardown_class(cls):
    #     sleep(2)
    #     cls.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_zyq_login.py'])
