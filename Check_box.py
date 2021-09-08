from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox(executable_path="/Users/muhammadasif/Downloads/geckodriver")
driver.get("https://demoqa.com/checkbox")

assert "ToolsQA" in driver.title

wait = WebDriverWait(driver, 20)

Expand_check_box = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '.rct-icon.rct-icon-expand-all')))

Expand_check_box.click()

#  Checked here

Checked = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'span.rct-checkbox')))

Checked.click()

#  Unchecked here

Checked = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'span.rct-checkbox')))

Checked.click()

print('test is finished')
driver.close()
