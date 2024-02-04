from typing import List

from ..CharsForGame.CharField import CharField
from ..CharsForGame.CharManager import CharManager
from ..Score.Score import Score
from ..Word.WordChars import WordChars
from ..Word.WordSelector import WordSelector


class GameManager:
    _score = Score()

    def __init__(self, difficulty: str | None):
        self.difficulty = difficulty
        

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
        chars = self.get_word_from_file()
        self.char_managing = CharManager(chars)
        amount_of_chars = self.char_managing.char_counter.count_chars() + 1

        self.char_managing.char_field.field_with_invisible_chars(amount_of_chars)

        return self._secret_word


    # GameWord
    def display_word(self) -> str:
        return self._secret_word


    def set_letter(self, letter: str) -> None:
        self._letter_to_guess = letter
    # End GameWord

    # This should be in a class that check the user's input
    def check_input(self) -> str:
        char_position: CharField = self.char_managing.char_field
        is_position = self.char_managing.char_field.list_of_chars
        position = self.position_check(char_position, is_position)

        if self._letter_to_guess.lower() not in position:
            self._score.turns_to_guess(False)

        amount_turns = self.check_score()
        return f"{amount_turns}\n{is_position}"
        
    
    def check_score(self) -> int:
        return self._score.get_turns()

    # this should be in a class that only check the position
    def position_check(self, char_index: CharField, is_position: List[str]):
        for position in range(len(self._secret_word)):
            letter = self._secret_word[position]
            if letter.lower() == self._letter_to_guess.lower():
                letters_position = char_index.get_hidden_word(position, letter)
                is_position = letters_position
        return is_position
