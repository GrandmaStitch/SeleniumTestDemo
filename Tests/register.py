import time
import unittest
import sys
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Locators.browser_engine import BrowserEngine
# from base_page.base_page import BasePage
# from page_object.baidu import BaiduPage

from Commons.fetch_verify_code import FetchVerifyCode


class LoginPage():

    def __init__(self, url):
        self.open_url = url

    def setUp(self):
        self.driver = BrowserEngine().init_driver()

    def signUp(self):
        # self.driver.maximize_window()
        self.driver.get(self.open_url)
        # time.sleep(10)
        self.driver.find_element_by_link_text('去注册').click()

def main():
    login_url = 'http://h5-saas-dev.myutopa.com/login?redirect=%2Findex'
    verify_code_url = 'https://yunduanxin.net/info/8618411631209/'
    virtual_mobile_num = '18411631209'

    driver_path = os.path.abspath(os.path.dirname(
        os.path.dirname(__file__))) + os.path.sep + 'drivers' + os.path.sep + 'chromedriver_win_90'

    driver = webdriver.Chrome(driver_path)
    driver.maximize_window()
    driver.get(login_url)
    time.sleep(5)
    # driver.find_element_by_link_text('去注册').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/span/a').click()


login_url = 'http://h5-saas-dev.myutopa.com/login?redirect=%2Findex'
verify_code_url = 'https://yunduanxin.net/info/8618411631209/'
virtual_mobile_num = '18411631209'

driver_path = os.path.abspath(os.path.dirname(
    os.path.dirname(__file__))) + os.path.sep + 'drivers' + os.path.sep + 'chromedriver_win_90'

driver = webdriver.Chrome(driver_path)
driver.maximize_window()
driver.get(login_url)
time.sleep(5)
# driver.find_element_by_link_text('去注册').click()
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/span/a').click()
'''
# url = 'http://h5-saas-dev.myutopa.com/login?redirect=%2Findex'
# url1 = 'https://yunduanxin.net/info/8618411631209/'

driver = BrowserEngine(browser='chrome').init_driver()
driver.get(url)
driver.find_element_by_link_text('去注册').click()

driver = BrowserEngine().init_driver()
driver.get(url1)
for i in range(26):
    fetch_text = driver.find_elements_by_xpath('//*[@class="col-xs-12 col-md-8"]')[i].get_attribute('outerHTML')
    if '【网易】您的验证码为' in fetch_text:
        break

print(fetch_text)
res = fetch_text.split('"')
print(res[5])


# print(driver.find_element_by_link_text('【U智零售】您的验证码是'))


driver.quit()
# driver.close()
'''

# if __name__ == '__main__':
#     main()
