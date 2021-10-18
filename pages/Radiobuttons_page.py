
from locator.locator import MainPageLocators
from pages.base_page import BaseMethods
from FireEvents import FireEvents


class RadioButtonHandling(BaseMethods):
    def __init__(self,driver):
        self.driver = driver;

    def radio_yes_button(self):
        objbase = BaseMethods(self.driver)
        objbase.is_title_matches(MainPageLocators.title)
        print(MainPageLocators.title)
        objbase.wait_for_ele_visible(MainPageLocators.yes_radio_button_locator)
        self.driver.execute_script(FireEvents.fire_event_script +
                                   "fireEvent(document.querySelector('input#yesRadio.custom-control-input'),'click');")
        get_text  = objbase.get_text(MainPageLocators.yes_radio_button_text)
        print(get_text)

    def radio_impress_button(self):
        objbase = BaseMethods(self.driver)
        self.driver.execute_script(FireEvents.fire_event_script +
                                   "fireEvent(document.querySelector('input#impressiveRadio'),'click');")

        get_text = objbase.get_text(MainPageLocators.impresive_radio_button_text)
        print(get_text)



