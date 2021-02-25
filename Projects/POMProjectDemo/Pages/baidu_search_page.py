class SearchPage():

    def __init__(self, driver):
        self.driver = driver

        self.searchInput_textbox_name = 'wd'
        self.search_button_id = 'su'

    def enter_search_keyword(self, keyword):
        self.driver.find_element_by_name(self.searchInput_textbox_name).clear()
        self.driver.find_element_by_name(self.searchInput_textbox_name).send_keys(keyword)

    def click_search(self):
        self.driver.find_element_by_id('su').click()