
from locator.locator import MainPageLocators
from pages.base_page import BaseMethods


class ButtonsHandling(BaseMethods):
    def __init__(self,driver):
        self.driver = driver;

    def double_click(self):
        objbase = BaseMethods(self.driver)
        objbase.is_title_matches(MainPageLocators.title)
        print(MainPageLocators.title)
        objbase.click(MainPageLocators.double_click_element)
        get_text  = objbase.get_text(MainPageLocators.double_click_btn_text)
        print(get_text)

    def right_click(self):
        objbase = BaseMethods(self.driver)
        #  right click
        objbase.click(MainPageLocators.right_click)
        get_text  = objbase.get_text(MainPageLocators.right_click)
        print(get_text)

    def single_click(self):
        objbase = BaseMethods(self.driver)
        # single click
        objbase.click(MainPageLocators.single_click)
        get_text  = objbase.get_text(MainPageLocators.single_click)
        print(get_text)
        get_text  = objbase.get_text(MainPageLocators.dynamic_Msg)
        print(get_text)


