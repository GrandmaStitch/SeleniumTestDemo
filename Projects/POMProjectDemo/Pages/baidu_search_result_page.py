class SearchResultPage():

    def __init__(self, driver):
        self.driver = driver
        self.openWebsite_linkText = 'Apple (中国) - 官方网站'

    def click_link(self):
        self.driver.find_element_by_link_text(self.openWebsite_linkText).click()