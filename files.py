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
        options = webdriver.ChromeOptions()
        preferences = {
            "download.default_directory": "/Users/muhammadasif/PycharmProjects/seleniumAutomation/files/"}
        options.add_experimental_option("prefs", preferences)

        ff_driver = webdriver.Chrome(chrome_options=options)
        # Update Preferences For Download Location

    elif getBrowser == "firefox":
        options = webdriver.FirefoxProfile()
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.download.dir", "/Users/muhammadasif/PycharmProjects/seleniumAutomation/files/")

        ff_driver = webdriver.Firefox(firefox_profile=options)

    request.cls.driver = ff_driver


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get('https://demoqa.com/upload-download')
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 20)
        time.sleep(3)

        # upload file from same directory

        clickFileButton = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ' input[id="uploadFile"]')))

        clickFileButton.send_keys('/Users/muhammadasif/PycharmProjects/seleniumAutomation/files/file.png')

        # download file from same directory

        downloadFile = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ' a#downloadButton')))
        downloadFile.click()
        time.sleep(20)
        time.sleep(2)
        self.driver.close()
