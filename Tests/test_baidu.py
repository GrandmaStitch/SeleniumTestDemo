import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from base_page.base_page import BasePage
from base_page.browser_engine import BrowserEngine
from page_object.baidu import BaiduPage


class TestBaiduPage(unittest.TestCase):
    def setUp(self):
        # return webdriver.Chrome()
        self.driver = BrowserEngine().init_driver()
        # BaiduPage(webdriver.Chrome())
        self.baidupage = BaiduPage(self.driver)
        # return webdriver.Chrome().get(url)
        self.baidupage._open_url()

    def test_数字(self):
        try:
            self.baidupage.search_content('123')
            time.sleep(10)
            self.assertEqual(self.baidupage.get_title(), '123_百度搜索')
        except Exception as e:
            self.baidupage.get_img(self)
            raise e

    def test_汉字(self):
        try:
            self.baidupage.search_content('河北神玥软件')
            time.sleep(10)
            self.assertEqual(self.baidupage.get_title(), '河北神玥软件_百度搜索')
        except Exception as e:
            self.baidupage.get_img(self)
            raise e

    def test_英文字母(self):
        try:
            self.baidupage.search_content('shineyue')
            time.sleep(10)
            self.assertEqual(self.baidupage.get_title(), 'shineyue_百度搜索')
        except Exception as e:
            self.baidupage.get_img(self)
            raise e

    def tearDown(self):
        self.baidupage.quit()
