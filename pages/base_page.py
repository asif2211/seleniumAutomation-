from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# import csv
# from datetime import datetime
# from os import write


class BaseMethods:
    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self,locator):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return locator in self.driver.title

    def click(self,locator):
            try:
                WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located(By.CSS_SELECTOR,locator)).click()
                time.sleep(2)
            except:
                self.driver.find_element_by_css_selector(locator).click()
            # finally:
            #     self.driver.find_element_by_css_selector(locator).click()

    def send_values(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        try:
            return self.driver.find_element_by_css_selector(locator).text
        except (ValueError, TimeoutError, Exception):
            return None

    def get_inter_text(self, locator):
        try:
            return self.driver.find_element_by_css_selector(locator).get_attribute('value')
        except (ValueError, TimeoutError, Exception):
            return None

    def wait_for_ele_invisible(self, locator):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element(locator))
        except (ValueError, TimeoutError, Exception):
            return None

    def get_all_elements(self, locator):
        try:
            return self.driver.find_elements_by_class_name(locator)
        except:
            return self.driver.find_elements_by_css_selector(locator)

    def get_element_property(self, locator):
        ele = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator))
        return ele

    def clean_text(self, original, expected):
        result = original.replace(original, expected)
        return result

    def is_ele_clickable(self, locator):
        ele = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator))
        return ele

    def wait_for_ele_visible(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(locator))
        except (ValueError, TimeoutError, Exception):
            return None

    def send_form_values(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator))).send_keys(text)

    def check_the_check_box(self, locator):
        ele = self.driver.find_element_by_css_selector(locator).is_selected()
        return ele
