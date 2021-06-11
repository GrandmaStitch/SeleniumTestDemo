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