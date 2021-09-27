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
def driver_init(request,getBrowser):
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
        self.driver.get('https://demoqa.com/buttons')
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 20)
        # double click
        doubleClick  = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'button#doubleClickBtn.btn.btn-primary')))

        doubleClick.click()
        print('double click has done')

        # right click
        rightClick = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'button#rightClickBtn.btn.btn-primary')))

        rightClick.click()
        print('right click has done')
        time.sleep(1)
        # simple click

        simpleClick = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.col-12.mt-4.col-md-6 .mt-4:nth-of-type(3) > button')))

        simpleClick.click()

        print('simple click has done')

        print('test is finished')
        self.driver.close()

