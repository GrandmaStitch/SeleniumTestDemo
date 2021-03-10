from Projects.POMProjectDemo.Locators.locators import Locators

class SearchPage():

    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_name = Locators.search_textbox_name
        self.search_button_id = Locators.search_button_id

    def enter_search_keyword(self, keyword):
        self.driver.find_element_by_name(self.search_textbox_name).clear()
        self.driver.find_element_by_name(self.search_textbox_name).send_keys(keyword)

    def click_search(self):
        self.driver.find_element_by_id('su').click()