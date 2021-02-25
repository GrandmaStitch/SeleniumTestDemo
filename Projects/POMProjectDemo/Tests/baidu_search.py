from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os, unittest,time
from Projects.POMProjectDemo.Pages.baidu_search_page import SearchPage
from Projects.POMProjectDemo.Pages.baidu_search_result_page import SearchResultPage


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        root_path = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + '..' + os.path.sep + '..')
        driver_type = 'chromedriver88.exe'
        driver_path = os.path.abspath(root_path + os.path.sep + 'drivers' + os.path.sep + driver_type)

        cls.driver = webdriver.Chrome(driver_path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search(self):
        # 百度地址
        url = 'https://www.baidu.com'
        keyword = '苹果官网'

        driver = self.driver
        driver.get(url)
        self.driver.implicitly_wait(10)

        search = SearchPage(driver)
        search.enter_search_keyword(keyword)
        search.click_search()
        self.driver.implicitly_wait(10)

        time.sleep(5)

        search_result_page = SearchResultPage(driver)
        search_result_page.click_link()
        self.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        # cls.driver.quit()
        print('Test completed!')

if __name__ == '__main__':
    unittest.main()




'''
# 搜索页
try:
    driver.get(url)

    driver.implicitly_wait(10)

    if driver.find_element_by_link_text('百度热榜'):

        driver.find_element_by_name('wd').send_keys(keyword)

        driver.find_element_by_id('su').click()

        driver.implicitly_wait(10)

        # 搜索结果页
        driver.find_element_by_link_text('Apple (中国) - 官方网站').click()

        driver.implicitly_wait(10)

        print('Test completed!')

except:
    print("Can't open page!")
    driver.close()
    driver.quit()
'''