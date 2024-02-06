from typing import List

from ..CharsForGame.CharCounter import CharCounter
from ..CharsForGame.CharField import CharField
from ..Score.Score import Score
from ..Word.WordChars import WordChars
from ..Word.WordSelector import WordSelector


class GameManager:
    def __init__(self, difficulty: str | None):
        self.difficulty = difficulty
        self.score = Score()
        self.char_field = CharField()


    def get_word_from_file(self) -> List[str]:
        self._secret_word = WordSelector().get_word_from_file(self.difficulty)
        return WordChars().set_word_in_chars(self._secret_word)


    def initiate_game_managing(self) -> str:
        """
        #### Description:
        Initiate point where the game is being handled

        #### Parameter:
        A series of characters to set up this game

        #### Return:
        Display that the user will see in the terminal
        """
        chars = self.get_word_from_file()  # gets new chars of a chose word
        amount_of_chars = CharCounter(chars).get_length_of_chars() + 1

        self.char_field.field_with_invisible_chars(amount_of_chars)

        return self._secret_word


    # This should be in a class that check the user's input
    def set_letter(self, letter: str) -> None:
        self._letter_to_guess = letter


    def check_input(self) -> str:
        is_position: List[str] = self.char_field.list_of_chars()

        if self._letter_to_guess != "":
            position = self._position_check(is_position)

            if self._letter_to_guess.lower() not in position:
                self.score.turns_to_guess(False, self._secret_word)

        return f"{is_position}"


    # this should be in a class that only check the position
    def _position_check(self, is_position: List[str]):
        for position in range(len(self._secret_word)):
            letter = self._secret_word[position]
            if letter.lower() == self._letter_to_guess.lower():
                is_position = self.char_field.get_hidden_word(position, letter)

        return is_position
