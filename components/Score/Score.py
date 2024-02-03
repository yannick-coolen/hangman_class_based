class Score:
    _amount_of_turns = 9

    def turns_to_guess(self, answer: bool) -> str | None:
        if not answer:
            self._amount_of_turns -= 1
            if self.get_turns() <= 0:
                return "Game Over"
            else:
                return f"Amount of turns left {self.get_turns()}"
        else:
            return None

    def get_turns(self) -> int:
        return self._amount_of_turns
