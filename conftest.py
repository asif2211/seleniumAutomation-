import time

import pytest
from selenium import webdriver

# browser = "chrome"


def pytest_addoption(parser):
    # parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--browser", action="store", default="chrome")



@pytest.fixture
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture
def getDriver(request, getBrowser):
    _driver = None
    print("browser from getBrowser method - " + getBrowser)
    if getBrowser == "chrome":
        _driver = webdriver.Chrome()
    elif getBrowser == "firefox":
        _driver = webdriver.Firefox()
    # env = request.config.getoption("--env")
    # _driver.get("https://www." + env + ".saucedemo.com/index.html")
    _driver.get("https://www.saucedemo.com/index.html")
    _driver.implicitly_wait(20)
    request.cls.driver = _driver
    yield request.cls.driver
    time.sleep(2)
    request.cls.driver.quit()


