from enum import Enum


class DifficultyLevel(Enum):
    EASY = ["easy"]
    NORMAL = ["normal"]
    HARD = ["hard"]

# This one need to be checked for optimization to set the difficult level
class GameDifficulty:
    _selected_level: str = ""

    def select_dificulty(self, value_selection: int) -> str | None:
        if value_selection in [1, 2, 3]:
            return self._set_difficulty(value_selection)
        else:
            print("Invalid input, Please enter 1, 2, or 3")

            
    def _set_difficulty(self, value_selection: int) -> str | None:
        match value_selection:
            case 1:
                self._selected_level = DifficultyLevel.EASY.value[0]
            case 2:
                self._selected_level = DifficultyLevel.NORMAL.value[0]
            case 3:
                self._selected_level = DifficultyLevel.HARD.value[0]
            case _:
                return None
        return self._selected_level
