from Projects.POMProjectDemo.Locators.locators import Locators

class SearchResultPage():

    def __init__(self, driver):
        self.driver = driver
        self.openWebsite_linkText = Locators.openWebsite_linkText

    def click_link(self):
        self.driver.find_element_by_link_text(self.openWebsite_linkText).click()