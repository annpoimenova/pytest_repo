from YandexPages import SearchHelper

def test_first_one(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.click_search_loupe()
    yandex_main_page.enter_search_request("java")
    elements = yandex_main_page.check_navigation_bar()
    assert "pytest" in elements

def test_second_two(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.click_search_loupe()
    yandex_main_page.enter_search_request("python")
    elements = yandex_main_page.check_navigation_bar()
    assert "selenium" in elements