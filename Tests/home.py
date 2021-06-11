import time
import unittest
import sys
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Commons.browser_engine import BrowserEngine

class HomePage(unittest.TestCase):

    def setUp(self):
        self.driver = BrowserEngine().init_driver()

    def test_home_page(self):
        url = 'http://45.79.141.239:8080/en-gb/catalogue/'
        url1 = 'http://45.79.141.239:8080'
        self.driver.get(url)
        self.assertIn('All products', self.driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



