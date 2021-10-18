import unittest
from selenium import webdriver
from  pages.Radiobuttons_page import *
import pytest


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://demoqa.com/radio-button")

    def test_search_in_python_org(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        main_page = RadioButtonHandling(self.driver)
        # for yes button
        main_page.radio_yes_button()
        # for impress button
        main_page.radio_impress_button()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()