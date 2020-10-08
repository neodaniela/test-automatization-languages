import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru, es or fr")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    user_language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
