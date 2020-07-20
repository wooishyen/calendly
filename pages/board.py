"""
This module contains the game board page.
"""

from selenium.webdriver.common.by import By


class BoardPage:

    # Locators

    RESULT_TABLE = (By.ID, 'table')
    NUMBER_INPUT = (By.ID, 'number')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def result_board(self):
        board = self.browser.find_elements(*self.RESULT_TABLE)
        return board

    def number_input_value(self):
        number_input = self.browser.find_element(*self.NUMBER_INPUT)
        value = number_input.get_attribute('value')
        return value

