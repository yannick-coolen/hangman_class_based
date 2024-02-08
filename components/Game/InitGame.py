from .GameDifficulty import GameDifficulty
from .GameManager import GameManager


class InitGame:
    _running_status = True

    def start_game(self, difficulty: int):
        self.difficulty = GameDifficulty().select_dificulty(difficulty)

        if self.difficulty is None:
            # If self.difficulty is reached, it will automatically throw an execption
            # This issue is still under research to find a solution
            print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
            print("Game has stopped, check in the start_game() func")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        else:
            self.game_manager = GameManager(self.difficulty)
            self.game_manager.initiate_game_managing()
            self._running()


    def _running(self):
        while self._running_status:
            if "_" in self.game_manager.char_field.list_of_chars(): # <--- this should check if the list has no blank anymore
                if self.game_manager.score.get_turns() > 0:
                    input_letter = input("Enter a letter: ")

                    self.game_manager.set_letter(input_letter)
                    print(f"{self.game_manager.check_input()}")
                else:
                    self._running_status = self.stop_game()
            else:
                self._running_status = self.stop_game()
                print("\nYou won!")


    def stop_game(self) -> None:
        self._game_is_running = False
