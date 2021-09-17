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
        self.driver.get('https://demoqa.com/text-box')
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 20)
        # Full Name
        full_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Full Name"]')))
        full_name.clear()
        full_name.send_keys("MuhammadAsif")

        # Email
        email = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="name@example.com"]')))
        email.clear()
        email.send_keys("abc@xyz.com")

        # Addresss
        address = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea#currentAddress')))
        address.clear()
        address.send_keys("asif from lahroe")

        # Permanent Address
        per_address = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea#permanentAddress')))
        per_address.clear()
        per_address.send_keys("Asif From khanpur")

        self.driver.execute_script(
            FireEvents.fire_event_script + "fireEvent(document.querySelector('button#submit'), 'click');")
        time.sleep(5)
        self.driver.close()
