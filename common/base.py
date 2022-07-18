from selenium import webdriver
import time


class BasePage:
    """
    基础page层，封装常用方法
    """

    def __init__(self, driver):
        # 导入webdriver包
        self.driver = driver
        # self.driver = webdriver.Chrome()

    # 打开页面
    def open(self, url=None):
        if url is None:
            self.driver.get(url)
        else:
            self.driver.get(url)

    # 元素定位
    def locator(self, name, value):
        return self.driver.find_element(name, value)

    # 获取title
    def get_title(self):
        return self.driver.title

    # 获取页面文本，使用xpath定位
    def get_text(self, name, path):
        return self.locator(name, path).text

    # 获取当前url
    def get_url(self):
        return self.driver.current_url

    # 执行js脚本
    def js(self, script):
        self.driver.execute_script(script)

    # 休眠事件
    def sleep(self, sec):
        time.sleep(sec)

    # 获取iframe
    def get_iframe(self):
        iframe = self.driver.find_element_by_css_selector('iframe')
        return iframe
