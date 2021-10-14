from selenium import webdriver
from time import sleep
from common.imgCode import getCode


def login(username, password):
    driver = webdriver.Chrome()
    driver.get("http://sqwytst.wt.com:14352/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector('.login_btn').click()
    driver.save_screenshot('../share/1.png')
    for i in range(10):
        currdir = 'D:/Program Files/JetBrains/PyCharm Community Edition 2020.2/pytest_allure/share'
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_name('password').send_keys(password)
        sleep(2)
        driver.find_element_by_name('imgCode').send_keys(getCode(currdir))
        driver.find_element_by_id('login').click()
        sleep(2)
        url = driver.current_url
        if url != 'http://sso.wt.com:3100/loginPage?error':
            # assert page.get_url() == 'http://sqwytst.wt.com:14352/dashboard'
            assert driver.title == '首页 - 智慧网格综合管理平台'
            break
        else:
            driver.save_screenshot(currdir)
            continue


if __name__ == '__main__':
    login('18210001031', 'asdqwe123')
