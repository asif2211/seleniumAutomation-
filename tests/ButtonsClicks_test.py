import unittest
from selenium import webdriver
from  pages.ButtonsClicks_page import *
import pytest


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://demoqa.com/buttons")

    def test_search_in_python_org(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""
        main_page = ButtonsHandling(self.driver)
        main_page.double_click()
        main_page.right_click()
        main_page.single_click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()