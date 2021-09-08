from selenium import webdriver
import time
# for Chrome driver
# driver = webdriver.Chrome()
driver = webdriver.Firefox(executable_path="/Users/muhammadasif/Downloads/geckodriver")
driver.get("https://stage.edx.org/")
assert "Free Online Courses" in driver.title

elem = driver.find_element_by_css_selector('#home-search[placeholder="Search our 3000+ courses"]')
elem.clear()
elem.send_keys("python")
time.sleep(2)
search = driver.find_element_by_css_selector('.btn-inverse-brand.form-submit')
search.click()
driver.close()