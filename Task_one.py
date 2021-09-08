from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SelenumTest:

    # for Chrome driver
    # chrome_flag = 'chrome'
    # firefox_flag = 'firefox'
    #
    # if chrome_flag == ""
    # driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    def tests(self):
        # chromeFlag = "Chrome"
        # fireFoxFlag = "fireFox"
        # if

        driver = webdriver.Firefox(executable_path="/Users/muhammadasif/Downloads/geckodriver")
        wait = WebDriverWait(driver, 10)
        driver.get("https://stage.edx.org/")
        assert "Free Online Courses" in driver.title
        print(driver.title)

        elem = driver.find_element_by_css_selector('#home-search[placeholder="Search our 3000+ courses"]')
        elem.clear()
        elem.send_keys("python")
        time.sleep(2)
        search = driver.find_element_by_css_selector('.btn-inverse-brand.form-submit')
        search.click()

        time.sleep(2)

        # Full Name
        search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span > span:nth-child(1) > span:nth-child(1)')))
        assert "Introduction to Python" in search.text
        print(search.text)
        time.sleep(2)
        results_display = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.d-card-wrapper:nth-child(1)')))
        results_display.click()
        driver.close()


TestObject = SelenumTest()

TestObject.tests()