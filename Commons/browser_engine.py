import configparser
import os

from selenium import webdriver


class BrowserEngine(object):
    def __init__(self):
        config_path = os.path.abspath(os.path.dirname(
            os.path.dirname(__file__))) + '/config.ini'
        config = configparser.ConfigParser()
        try:
            config.read(config_path, encoding='utf-8')
        except:
            config.read(config_path, encoding='utf-8-sig')
        self._driver_type = config.get('driverName', 'driverVersion')
        self._driver = None
        self.driver_path = os.path.abspath(os.path.dirname(
            os.path.dirname(__file__))) + os.path.sep + 'drivers'+ os.path.sep + self._driver_type

    def init_driver(self):
        if 'chrome' in self._driver_type.lower():
            self._driver = webdriver.Chrome(self.driver_path)
        elif 'firefox' in self._driver_type.lower():
            self._driver = webdriver.Firefox(self.driver_path)
        elif 'ie' in self._driver_type.lower():
            self._driver = webdriver.Ie(self.driver_path)
        elif 'edge' in self._driver_type.lower():
            self._driver = webdriver.Edge(self.driver_path)
        else:
            ValueError('传入的浏览器类型有误，目前仅支持Chrome/Firefox/IE/Edge浏览器')
        self._driver.maximize_window()
        return self._driver

