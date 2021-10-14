from common.base import BasePage

"""
    baidu_page.py 存储百度搜索页面 
    封装操作到的元素
"""


class BaiduPage(BasePage):
    url = "http://www.baidu.com"

    # 使用继承的父类中的locator方法进行定位
    def search_input(self, search_key):
        self.locator("id", "kw").send_keys(search_key)

    # 定位button
    def search_button(self):
        self.locator("id", "su").click()
