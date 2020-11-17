from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from BaseApp import BasePage
from selenium.webdriver.common.by import By

class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_LOUPE = (By.ID, "search-form-btn")
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "search-form-field")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".searched-item")

class SearchHelper(BasePage):

    def click_search_loupe(self):
        search_loupe = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_LOUPE)
        search_loupe.click()

    def enter_search_request(self, request):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.send_keys(request)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        return search_field

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR,time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu