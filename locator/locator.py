from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GO_BUTTON = (By.ID, 'submit')
    #  Buttons click tests Locators
    title  = 'ToolsQA'
    double_click_element  = "button#doubleClickBtn.btn.btn-primary"
    double_click_btn_text  = "#doubleClickBtn"
    right_click = "#rightClickBtn"
    single_click = "#app .col-12.mt-4.col-md-6 .mt-4:nth-of-type(3) button"
    dynamic_Msg = "#dynamicClickMessage"
    #  Radio buttons click tests Locators
    yes_radio_button_locator = "input#yesRadio.custom-control-input"
    yes_radio_button_text = ".col-12.mt-4.col-md-6:nth-of-type(2) .mt-3 .text-success"
    impresive_radio_button = "input#impressiveRadio"
    impresive_radio_button_text = ".col-12.mt-4.col-md-6:nth-of-type(2) .mt-3 .text-success"
    double_click_btn_text = "#doubleClickBtn"
    right_click = "#rightClickBtn"
    single_click = "#app .col-12.mt-4.col-md-6 .mt-4:nth-of-type(3) button"
    dynamic_Msg = "#dynamicClickMessage"
