import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from base_page.browser_engine import BrowserEngine
from base_page.base_page import BasePage
from page_object.baidu import BaiduPage

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

'''
class LoginPage(unittest.TestCase):

    url = 'http://h5-saas-dev.myutopa.com/login?redirect=%2Findex'

    def setUp(self):
        self.driver = BrowserEngine().init_driver()
        self.driver.get(url)
        # self.baidupage = BaiduPage(self.driver)
        # self.baidupage._open_url()
'''
url = 'http://h5-saas-dev.myutopa.com/login?redirect=%2Findex'
url1 = 'https://yunduanxin.net/info/8618411631209/'
'''
driver = BrowserEngine(browser='chrome').init_driver()
driver.get(url)
driver.find_element_by_link_text('去注册').click()
'''
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
