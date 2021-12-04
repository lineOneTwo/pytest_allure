from common.base import BasePage

# from common.login import Login

"""
    申请管理页面
"""


class Applypage(BasePage):

    # 使用继承的父类中的locator方法进行定位
    def apply_management(self):
        self.locator("xpath", "/html/body/div/div/div[1]/div/div[1]/div/ul/div[3]/a/li").click()

    def input_name(self, search_key):
        self.locator("xpath",
                     "/html/body/div/div/div[2]/section/div/div[1]/div/main/div/div[1]/div/form/div[1]/div/div/input").send_keys(
            search_key)

    def input_phone(self, search_key):
        self.locator("xpath",
                     "/html/body/div/div/div[2]/section/div/div[1]/div/main/div/div[1]/div/form/div[2]/div/div/input").send_keys(
            search_key)

    # 选择审批状态
    def click_status(self):
        self.locator("xpath",
                     "/html/body/div[1]/div/div[2]/section/div/div[1]/div/main/div/div[1]/div/form/div[3]/div/div/div/input").click()

    def select_status_all(self):
        self.locator("xpath", "/html/body/div[2]/div[1]/div[1]/ul/li[1]").click()

    def select_status_pending(self):
        self.locator("xpath", "/html/body/div[3]/div[1]/div[1]/ul/li[2]").click()

    def select_status_pass(self):
        self.locator("xpath", "/html/body/div[2]/div[1]/div[1]/ul/li[3]").click()

    def select_status_fail(self):
        self.locator("xpath", "/html/body/div[2]/div[1]/div[1]/ul/li[4]").click()

    # 选择机构
    def click_organization(self):
        self.locator("xpath",
                     "/html/body/div[1]/div/div[2]/section/div/div[1]/div/main/div/div[1]/div/form/div[4]/div/div/div/input").click()

    def click_area(self):
        self.locator("xpath", "/html/body/div[3]/div[1]/div[1]/div[1]/ul/li/span").click()

    def select_area(self):
        self.locator("xpath", "/html/body/div[2]/div[1]/div[1]/div[1]/ul/li/label/span[1]/span").click()

    def click_row(self):
        self.locator("xpath", "/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[1]/span").click()

    def select_row(self):
        self.locator("xpath", "/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[1]/label/span[1]/span").click()

    def click_community(self):
        self.locator("xpath", "/html/body/div[3]/div[1]/div[3]/div[1]/ul/li[1]/span").click()

    def select_community(self):
        self.locator("xpath", "/html/body/div[3]/div[1]/div[3]/div[1]/ul/li[1]/label/span[1]/span").click()

    def select_grid(self):
        self.locator("xpath", "/html/body/div[3]/div[1]/div[4]/div[1]/ul/li[1]/label/span[1]/span").click()

    # 选择是否兼职
    def click_jobs_status(self):
        self.locator("xpath",
                     "/html/body/div[1]/div/div[2]/section/div/div[1]/div/main/div/div[1]/div/form/div[5]/div/div/div/input").click()

    def select_all(self):
        self.locator("xpath", "/html/body/div[4]/div[1]/div[1]/ul/li[1]/span").click()

    def select_fulltime(self):
        self.locator("xpath", "/html/body/div[4]/div[1]/div[1]/ul/li[2]/span").click()

    def select_parttime(self):
        self.locator("xpath", "/html/body/div[4]/div[1]/div[1]/ul/li[3]/span").click()

    def submit_select(self):
        self.locator("xpath",
                     "/html/body/div/div/div[2]/section/div/div[1]/div/main/div/div[1]/div/form/div[6]/div/button[1]/span").click()

    def reload(self):
        self.locator("xpath",
                     "/html/body/div/div/div[2]/section/div/div[1]/div/main/div/div[1]/div/form/div[6]/div/button[2]/span").click()

    def get_name(self):
        return self.locator("xpath",
                            "/html/body/div/div/div[2]/section/div/div[1]/div/main/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div").text

    def get_phone(self):
        return self.locator("xpath",
                            "/html/body/div/div/div[2]/section/div/div[1]/div/main/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div").text

    def get_organization(self):
        return self.locator("xpath",
                            "/html/body/div/div/div[2]/section/div/div[1]/div/main/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div").text

    def get_status(self):
        return self.locator("xpath",
                            "/html/body/div[1]/div/div[2]/section/div/div[1]/div/main/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/span").text

    def get_jod_type(self):
        return self.locator("xpath",
                            "/html/body/div/div/div[2]/section/div/div[1]/div/main/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div").text

    def audit(self):
        self.locator("xpath",
                     "/html/body/div[1]/div/div[2]/section/div/div[1]/div/main/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/button[1]/span").click()

    def delete(self):
        self.locator("xpath",
                     "/html/body/div[1]/div/div[2]/section/div/div[1]/div/main/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/button[2]/span").click()
