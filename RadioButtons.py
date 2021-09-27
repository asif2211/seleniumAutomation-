# Import the 'modules' that are required for execution for Selenium test automation
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from FireEvents import FireEvents
import sys


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser


# Fixture for browser selection
@pytest.fixture(scope="class")
def driver_init(request, getBrowser):
    if getBrowser == "chrome":
        ff_driver = webdriver.Chrome()
    elif getBrowser == "firefox":
        ff_driver = webdriver.Firefox()

    request.cls.driver = ff_driver


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get('https://demoqa.com/radio-button')
        self.driver.maximize_window()

        self.driver.execute_script(FireEvents.fire_event_script +
                                                          "fireEvent(document.querySelector('input#yesRadio.custom-control-input'),'click');")
        self.driver.close()
