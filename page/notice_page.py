from common.base import BasePage
from common import imgCode

"""
    通知公告
"""


class NoticePage(BasePage):
    def notice_management(self):
        self.locator("xpath", "/html/body/div[1]/div/div[1]/div/div[1]/div/ul/div[4]/a/li").click()

    def input_title(self, title):
        self.locator("xpath", "/html/body/div[1]/div/div[2]/section/div/div[1]/div[2]/div/form/div[1]/div/div/input").send_keys(title)

    def search(self):
        self.locator("xpath", "/html/body/div[1]/div/div[2]/section/div/div[1]/div[2]/div/form/div[2]/div/button[1]").click()

    def reload(self):
        self.locator("xpath", "/html/body/div[1]/div/div[2]/section/div/div[1]/div[2]/div/form/div[2]/div/button[2]/span").click()

    def add(self):
        self.locator("xpath", "/html/body/div[1]/div/div[2]/section/div/div[1]/div[1]/button").click()

    def add_title(self, title):
        self.locator("xpath", "/html/body/div[1]/div/div[2]/section/div/div[2]/div/div/div[2]/form/div[1]/div/div[1]/input").send_keys(title)

    def select_iframe(self):
        self.driver.find_elements_by_css_selector('iframe')

    def add_content(self, content):
        self.locator("xpath", "//body").send_keys(content)

    def submit(self):
        self.locator("xpath", "/html/body/div[1]/div/div[2]/section/div/div[2]/div/div/div[3]/div/button[2]").click()




