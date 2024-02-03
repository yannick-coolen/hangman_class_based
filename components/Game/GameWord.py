# from typing import List

from ..Word.WordSelector import WordSelector


class GameWord:
    _secret_word = ""

    def __init__(self):
        self.word_selector = WordSelector()


    def display_word(self):
        return self._secret_word


    def set_letter(self, letter: str) -> None:
        self._letter_to_guess = letter
