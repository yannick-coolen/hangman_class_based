

class GameWord:
    _secret_word = ""

    def display_word(self) -> str:
        return self._secret_word


    def set_letter(self, letter: str) -> None:
        self._letter_to_guess = letter
