from ..Display.DisplayHangman import DisplayHangman


class Score:
    _amount_of_turns = 9

    def turns_to_guess(self, answer: bool) -> str | None:
        if not answer:
            self._amount_of_turns -= 1
            if self.get_turns() <= 0:
                print(
                    f"""\nGame Over
                      {DisplayHangman().get_display(self._amount_of_turns)}"""
                )
            else:
                print(
                    f"""Amount of turns left {self.get_turns()}
                      {DisplayHangman().get_display(self._amount_of_turns)}
                      """
                )
        else:
            return None

    def get_turns(self) -> int:
        return self._amount_of_turns
