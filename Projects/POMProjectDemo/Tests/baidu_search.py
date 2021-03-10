from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os, sys, unittest,time, shutil
# run from command line setting
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from Projects.POMProjectDemo.Pages.baidu_search_page import SearchPage
from Projects.POMProjectDemo.Pages.baidu_search_result_page import SearchResultPage
from TestRunner import HTMLTestRunner


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        root_path = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + '..' + os.path.sep + '..')
        driver_type = 'chromedriver89.exe'
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

        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        try:
            cls.driver.quit()
        except Exception as e:
            print(e)
        print('Test completed!')


if __name__ == '__main__':
    # unittest.main()
    # testRunner = HtmlTestRunner.HTMLTestRunner(output='D:/TryTryTry/SeleniumTestDemo/Reports')
    suit = unittest.TestSuite()
    suit.addTest(SearchTest("test_search"))
    now = time.strftime('%Y%m%d%H%M%S')
    with(open(f'Test_Report_{now}.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='测试报告',
            description='测试用例demo'
        )
        runner.run(suit)

    source_path = os.getcwd()
    target_path = os.path.abspath(
        os.path.dirname(os.getcwd()) + os.path.sep + '..' + os.path.sep + '..' + os.path.sep + 'Reports')
    for f in os.listdir(source_path):
        if f.endswith('.html'):
            shutil.move(f, target_path)

