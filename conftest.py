import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="C:/Users/Anna_Poimenova/PycharmProjects/pytest/chromedriver_win32/chromedriver.exe")
    yield driver
    driver.quit()