from selenium import webdriver
import time
from FireEvents import FireEvents
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#  Explicit wait for certain condition until not get exception of NotElementVisible

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import os


class SeleniumTestTask2 :

    def chromeTest(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get("https://demoqa.com/text-box")

        assert "ToolsQA" in driver.title
        wait = WebDriverWait(driver, 10)
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

        driver.execute_script(
            FireEvents.fire_event_script + "fireEvent(document.querySelector('button#submit'), 'click');")
        time.sleep(2)
        driver.close()

    def fireFoxTest(self):

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://demoqa.com/text-box")
        assert "ToolsQA" in driver.title
        wait = WebDriverWait(driver, 10)
        # Full Name
        full_name = wait.until(EC.presence_of_element_located  ((By.CSS_SELECTOR, 'input[placeholder="Full Name"]')))
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

        driver.execute_script(FireEvents.fire_event_script + "fireEvent(document.querySelector('button#submit'), 'click');")
        time.sleep(2)
        driver.close()


testObject = SeleniumTestTask2()
testObject.chromeTest()
# testObject.fireFoxTest()