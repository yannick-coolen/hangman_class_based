from .GameDifficulty import GameDifficulty
from .GameManager import GameManager


class InitGame:   
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
            return self.game_manager.initiate_game_managing()
       
       
    def set_running_status(self, game_is_running: bool) -> None:
        self.game_is_running = game_is_running


    def stop_game(self) -> None:
        self._game_is_running = False
