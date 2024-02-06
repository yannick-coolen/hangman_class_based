from typing import List


class CharField():
    _list_of_chars: List[str] = []
        

    def list_of_chars(self) -> List[str]:
        return self._list_of_chars


    def field_with_invisible_chars(self, amount_of_chars: int) -> None:
        while amount_of_chars > 1:
            self._list_of_chars.append("_")
            amount_of_chars -= 1


    def get_hidden_word(self, position: int, letter: str) -> List[str]:
        self._list_of_chars[position] = letter
        return self._list_of_chars
    