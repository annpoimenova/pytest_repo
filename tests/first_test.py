from YandexPages import SearchHelper
import pytest

#if you want run tests parallel using command: pytest -n 2
#if you want run marking test using command: pytest -m run_these_please
#if you want run tests contains in method specific word using command: pytest -k "first"
#if you want see fail steps using command: pytest -x
#short test summary info: pytest --tb=no
#run last fail test: pytest --lf



# @pytest.mark.parametrize("x", ["pytest", "BDD"])
def test_first(browser, x):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.click_search_loupe()
    yandex_main_page.enter_search_request(x)
    elements = yandex_main_page.check_navigation_bar()
    assert "pytest" in elements


# @pytest.mark.run_these_please
def test_second(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.click_search_loupe()
    yandex_main_page.enter_search_request("selenium")
    elements = yandex_main_page.check_navigation_bar()
    assert "selenium" in elements