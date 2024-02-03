from typing import List

from .CharCounter import CharCounter
from .CharField import CharField


class CharManager:
    _list_of_chars: List[str] = []

    def __init__(self, chars: List[str]):
        self.chars = chars
        self.char_counter = CharCounter(self.chars)
        self.char_field = CharField(self._list_of_chars)
       