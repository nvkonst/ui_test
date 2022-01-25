from selenium import webdriver
from fixture.testpage import TestPage
from fixture.person import PersonHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        self.base_url = base_url
        self.testpage = TestPage(self)
        self.person = PersonHelper(self)
        self.wd.implicitly_wait(20)

    def is_valid(self):
        wd = self.wd
        try:
            wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

    def current_url(self):
        wd = self.wd
        return wd.current_url

    # некоторые методы применимы для работы с любыми страницами, поэтому вынесены из класса TestPage
    def check_unique_element_presence_by_xpath(self, xpath):
        wd = self.wd
        if len(wd.find_elements_by_xpath(xpath)) == 1:
            return True
        else:
            return False

    def scroll_to_element(self, selector):
        wd = self.wd
        element = wd.find_element_by_css_selector(selector)
        element.location_once_scrolled_into_view
