from selenium import webdriver
from FireEvents import FireEvents
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#  Explicit wait for certain condition until not get exception of NotElementVisible

# for Chrome driver
# driver = webdriver.Chrome()
driver = webdriver.Firefox(executable_path="/Users/muhammadasif/Downloads/geckodriver")
driver.get("https://demoqa.com/checkbox")

assert "ToolsQA" in driver.title
wait = WebDriverWait(driver, 20)

# Check
driver.execute_script(FireEvents.fire_event_script + "fireEvent(document.querySelector('#tree-node-home'), 'click');")
time.sleep(1)

# for unCheck
driver.execute_script(FireEvents.fire_event_script + "fireEvent(document.querySelector('#tree-node-home'), 'click');")
time.sleep(1)
driver.close()