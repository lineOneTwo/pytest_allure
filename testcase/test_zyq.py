import time

import pytest
from time import sleep
from selenium import webdriver
from common.winauto import WinAuto
import datetime
from page.login_page import Loginpage
import allure

# 截图文件夹
img_dir_path = '../Result_zyq_Image_Orig/'


@allure.feature('登录')
class Test_login:

    # 环境准备 前置条件
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:/Project/pytest_allure/chromedriver.exe')
        cls.driver.get('http://111.53.13.252/admin_zyq/')
        cls.driver.find_element_by_css_selector('.login_btn').click()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @allure.feature('若验证码错误，可循环登录十次')
    def test_login(self):
        currdir = r'D:/Project/pytest_allure/share'
        page = Loginpage(self.driver)

        for i in range(10):
            page = Loginpage(self.driver)
            page.get_picture(currdir)
            page.search_username("18710001032")
            page.search_password("F&iijuq1vX&PR")
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


    # 跳过
    # @pytest.mark.skip
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
        sleep(1)
        # 添加栏目
        articlecolumn_add_img = img_dir_path + 'articlecolumn_add.png'
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]/span').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div/div[2]/form/div/div/div/input').send_keys('栏目')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div/div[3]/div/button[1]/span').click()
        driver.save_screenshot(articlecolumn_add_img)
        sleep(1)


        # # 截图
        # driver.save_screenshot(
        #     '../Result_zyq_Image_Orig/roleList{0}.png'.format(time.strftime('%Y-%m-%d', time.localtime(time.time()))))



        # 编辑栏目
        articlecolumn_edit_img = img_dir_path + 'articlecolumn_edit.png'
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[5]/div/button[1]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div/div[3]/div/button[2]/span').click()
        driver.save_screenshot(articlecolumn_edit_img)
        sleep(1)


        # 下级栏目
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[4]/div/button/span').click()
        sleep(1)
        # 返回上级
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]/span').click()
        sleep(1)

    # @pytest.mark.skip
    @allure.feature('测试文章管理')
    def test_articleList(self):
        driver = self.driver
        # 打开文章列表
        driver.get('http://111.53.13.252/admin_zyq/?code=Hst0Ng#/articleList')
        sleep(1)
        # 点击机构列表
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/section/aside/div/div[1]/div/span[2]').click()

        # 点击添加文章按钮
        articleList_add_img = img_dir_path + 'articleList_add.png'
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/section/main/div[3]/button/span').click()
        # 输入内容
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div[2]/form/div[1]/div/div[1]/input').send_keys('文章标题')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div[2]/form/div[2]/div/div/input').send_keys('from')

        # 上传附件按钮
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div[2]/form/div[3]/div/div/div/button').click()
        # 上传附件
        window = WinAuto("#32770", "打开")
        window.file_input(r"C:\Users\Administrator\2021.jpg")
        window.open_button_click()


        #切换到富文本
        iframe = driver.find_element_by_id('ueditor_0')
        driver.switch_to_frame(iframe)
        driver.find_element_by_xpath('/html/body/p').send_keys('测试内容输入')
        sleep(1)

        # 跳转回到主框架页
        driver.switch_to.default_content()

        # 滚动至元素可见
        ele = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div[3]/div/button[1]/span')
        driver.execute_script("arguments[0].scrollIntoView();", ele)
        sleep(2)

        # 取消
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div[3]/div/button[1]/span').click()
        sleep(2)
        driver.save_screenshot(articleList_add_img)


        # 切换到已终审文章
        driver.find_element_by_xpath('//*[@id="tab-2"]').click()
        sleep(1)
        # 查询功能
        articleList_select_img = img_dir_path + 'articleList_select.png'
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/section/main/div[2]/div/form/div[1]/div/div/input').send_keys('人民银行')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/section/main/div[2]/div/form/div[3]/div/button[1]').click()
        driver.save_screenshot(articleList_select_img)
        sleep(2)

        # 切换拒审文章
        driver.find_element_by_xpath('//*[@id="tab-3"]').click()
        sleep(1)

    # @pytest.mark.skip
    @allure.feature('测试企业审核')
    def test_pbcFirmInformation(self):
        driver = self.driver
        driver.get('http://111.53.13.252/admin_zyq/?code=Hst0Ng#/pbcFirmInformation')
        sleep(1)

        # 企业名称、规模查询
        pbcFirmInformation_inquire_img = img_dir_path + 'pbcFirmInformation_inquire.png'
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/form/div[1]/div/div/input').send_keys('name')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/form/div[2]/div/div/div/input').click()
        sleep(2)
        # 先确定ui，再确定li
        a = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul')
        a.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[3]').click()
        sleep(1)
        # 查询按钮
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/form/div[3]/div/button[1]').click()
        driver.save_screenshot(pbcFirmInformation_inquire_img)

        # 切换到已审企业
        driver.find_element_by_xpath('//*[@id="tab-2"]').click()
        # 查询后重置
        pbcFirmInformation_reset_img = img_dir_path + 'pbcFirmInformation_reset.png'
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/form/div[1]/div/div/input').send_keys('name')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/form/div[3]/div/button[1]/span').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/form/div[3]/div/button[2]/span').click()
        driver.save_screenshot(pbcFirmInformation_reset_img)
        # 查看详情
        pbcFirmInformation_detail_img = img_dir_path + 'pbcFirmInformation_detail.png'
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[8]/div/button/span').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[3]/div/button[2]/span').click()
        sleep(1)
        driver.save_screenshot(pbcFirmInformation_detail_img)

        # 切换到拒审企业
        driver.find_element_by_xpath('//*[@id="tab-3"]').click()

    # @pytest.mark.skip
    @allure.feature('测试文章审核')
    def test_pbcArticleList(self):
        driver = self.driver
        driver.get('http://111.53.13.252/admin_zyq/?code=Hst0Ng#/pbcArticleList')
        sleep(1)

        # 查询
        pbcArticleList_inquire_img = img_dir_path + 'pbcArticleList_inquire.png'
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/form/div[1]/div/div/input').send_keys('标题')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/form/div[2]/div/label[2]/span[1]/span').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/form/div[3]/div/button[1]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/form/div[3]/div/button[2]/span').click()
        driver.save_screenshot(pbcArticleList_inquire_img)
        sleep(1)

        # 切换到已审核列表
        driver.find_element_by_xpath('//*[@id="tab-2"]').click()
        sleep(1)

        # 切换到拒审列表
        driver.find_element_by_xpath('//*[@id="tab-3"]').click()
        sleep(1)

    # @pytest.mark.skip
    @allure.feature('测试资金审核')
    def test_moneyPedestrianManagementProjectDocking(self):
        driver = self.driver
        driver.get('http://111.53.13.252/admin_zyq/?code=6UHGIE#/moneyPedestrianManagementProjectDocking')

        # 查询
        moneyPedestrianManagementProjectDocking_inquire_img = img_dir_path + 'moneyPedestrianManagementProjectDocking_inquire.png'
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/form/div[1]/div/div/input').send_keys('name')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/form/div[2]/div/button[1]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/form/div[2]/div/button[2]').click()
        driver.save_screenshot(moneyPedestrianManagementProjectDocking_inquire_img)
        sleep(1)


        # 切换到待银行对接项目
        driver.find_element_by_xpath('//*[@id="tab-2"]').click()
        sleep(1)
        # 详情
        moneyPedestrianManagementProjectDocking_detail_img = img_dir_path + 'moneyPedestrianManagementProjectDocking_detail.png'
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[9]/div/button/span').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[3]/div/button/span').click()
        driver.save_screenshot(moneyPedestrianManagementProjectDocking_detail_img)
        sleep(1)

        # 切换到被拒审项目
        driver.find_element_by_xpath('//*[@id="tab-4"]').click()
        # 查询
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/form/div[1]/div/div/input').send_keys('name')
        sleep(1)
        # # 截图
        # driver.save_screenshot('../Result_zyq_Image_Orig/jushen{0}.png'.format(time.strftime('%Y-%m-%d',time.localtime(time.time()))))

    # @pytest.mark.skip
    @allure.feature('测试法律法规')
    def test_porTallist(self):
        driver = self.driver
        driver.get('http://111.53.13.252/admin_zyq/?code=6UHGIE#/porTallist')
        iframe = driver.find_element_by_class_name('iframe_content')
        driver.switch_to_frame(iframe)

        a = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/ul')
        a.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/ul/li[3]/span').click()

        # 跳转回到主框架页
        driver.switch_to.default_content()

        # 截图
        driver.save_screenshot('../Result_zyq_Image_Orig/porTallist{0}.png'.format(time.strftime('%Y-%m-%d',time.localtime(time.time()))))

    # @pytest.mark.skip
    @allure.feature('测试消息管理')
    def test_message(self):
        driver = self.driver
        driver.get('http://111.53.13.252/admin_zyq/?code=6UHGIE#/messageManage')

        # 翻页
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/button[2]/i').click()
        sleep(1)
        # 截图
        driver.save_screenshot('../Result_zyq_Image_Orig/message{0}.png'.format(time.strftime('%Y-%m-%d',time.localtime(time.time()))))

    # @pytest.mark.skip
    @allure.feature('资源管理')
    def test_resourceList(self):
        driver =self.driver
        driver.get('http://111.53.13.252/admin_zyq/?code=6UHGIE#/resourceList')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/div[1]/i').click()
        sleep(1)
        # 截图
        driver.save_screenshot('../Result_zyq_Image_Orig/resourceList{0}.png'.format(time.strftime('%Y-%m-%d',time.localtime(time.time()))))

    # @pytest.mark.skip
    @allure.feature('角色管理')
    def test_roleList(self):
        driver = self.driver
        driver.get('http://111.53.13.252/admin_zyq/?code=6UHGIE#/roleList')
        sleep(3)
        # 添加角色
        rolelist_add_img = img_dir_path + 'rolelist_add.png'
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div[2]/button/span').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[1]/div/div[1]/input').send_keys('test')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[2]/div/div[1]/input').send_keys('tese')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[3]/div/button[2]/span').click()
        driver.save_screenshot('../Result_zyq_Image_Orig/resourceList{0}.png'.format(time.strftime('%Y-%m-%d',time.localtime(time.time()))))
        driver.save_screenshot(rolelist_add_img)
        sleep(3)

        # 查询角色
        rolelist_inquire_img = img_dir_path + 'rolelist_inquire.png'
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div/div/input').send_keys('test')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div/button[1]/span').click()
        driver.save_screenshot(rolelist_inquire_img)
        sleep(3)


        # 删除角色
        rolelist_delete_img = img_dir_path + 'rolelist_delete.png'
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[4]/div/button[2]/span').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
        driver.save_screenshot(rolelist_delete_img)
        sleep(3)


    # @pytest.mark.skip
    @allure.feature('用户管理')
    def test_userList(self):
        driver = self.driver
        driver.get('http://111.53.13.252/admin_zyq/?code=6UHGIE#/userList')

        # 查询用户
        userlist_inquire_img = img_dir_path + 'userlist_inquire.png'
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div/div/input').send_keys('人行')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div/div/div/input').click()
        sleep(1)

        # 下拉列表
        a = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul')
        a.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()

        # 查询按钮
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[3]/div/button[1]/span').click()
        driver.save_screenshot(userlist_inquire_img)
        sleep(1)


    # 环境清理
    @classmethod
    def teardown_class(cls):
        sleep(2)
        cls.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_zyq.py'])
