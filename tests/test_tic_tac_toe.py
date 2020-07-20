"""
These tests cover Tic Tac Toe game.
"""

import pytest

from calendly.pages import InputPage


@pytest.mark.parametrize('phrase', [3])
def create_tic_tac_toe(browser, phrase):
    input_page = InputPage(browser)
    board_page = BoardPagePage(browser)

    # Given the Tic Tac Toe game page is displayed
    input_page.load()

    # When the user enters a 3 in the text box
    board_page.input(phrase)

    # Then the 3 x 3 board game is displayed
    assert phrase == board_page.number_input_value()


