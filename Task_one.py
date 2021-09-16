import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from FireEvents import  FireEvents
import time


def pytest_addoption(parser):
    # parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--browser", action="store", default="chrome")
    # parser.addoption("--env", action="store", default=settings.env)


@pytest.fixture
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture
def driver_init(request,getBrowser):
    print("browser from getBrowser method - " + getBrowser)
    if getBrowser == "chrome":
        _driver = webdriver.Chrome()
    elif getBrowser == "firefox":
        _driver = webdriver.Firefox()

    request.cls.driver = _driver
    # yield
    # _driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get("https://demoqa.com/text-box")
        print(self.driver.title)
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
        time.sleep(1)
        self.driver.close()

# obj = Task_One()
# obj_two = obj.Test_URL()
# obj_two.test_open_url()