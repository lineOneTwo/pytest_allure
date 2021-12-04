from common.base import BasePage
from common.imgCode import getCode

"""
    登录页面
"""


class Loginpage(BasePage):

    # 使用继承的父类中的locator方法进行定位
    def search_login(self):
        self.locator("xpath", '//*[@id="app"]/div/div[1]/div/span').click()

    def mix_windows(self):
        self.driver.maximize_window()

    def get_picture(self, currdir):
        self.driver.save_screenshot(currdir+"/1.png")
        # self.driver.save_screenshot('\share\screeshots\screenshot')

    def search_username(self, search_key):
        self.locator("name", "username").send_keys(search_key)

    def search_password(self, search_key):
        self.locator("name", "password").send_keys(search_key)

    def search_code(self, currdir):
        self.locator("name", "imgCode").send_keys(getCode(currdir))

    # 定位button
    def click_login(self):
        self.locator("id", "login").click()

    def search_job(self):
        self.locator("xpath", "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div/label/span[1]/span").click()

    def login_job(self):
        self.locator("xpath", "/html/body/div[1]/div/div[2]/div/div/div[3]/div/button[2]/span").click()
