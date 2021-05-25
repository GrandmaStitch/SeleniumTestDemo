import time
import unittest

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
driver = BrowserEngine(browser='chrome').init_driver()
driver.get(url1)
for i in range(26):
    ll = driver.find_elements_by_xpath('//*[@class="col-xs-12 col-md-8"]')[i].get_attribute('outerHTML')
    # ll = driver.find_elements_by_xpath('//*[@class="col-xs-12 col-md-8"]')[i].get_attribute('currentSrc')
    if '【新航道】您的验证码是' in ll:
        print(ll)


# print(driver.find_element_by_link_text('【U智零售】您的验证码是'))

# inputContext1 = driver.find_element_by_xpath('//input[@class="ivu-input"]').get_attribute('value')

# driver.quit()
# driver.close()
