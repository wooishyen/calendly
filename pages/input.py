"""
This module contains input for the Tic Tac Toe Page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InputPage:

  # URL

  URL = 'https://codepen.io/CalendlyQA/full/KKPQLmV'

  # Locators

  NUMBER_INPUT = (By.ID, 'number')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def input(self, phrase):
    number_input = self.browser.find_element(*self.NUMBER_INPUT)
    number_input.send_keys(phrase + Keys.RETURN)