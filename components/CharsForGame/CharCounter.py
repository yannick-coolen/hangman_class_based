from typing import List


class CharCounter:
    def __init__(self, chars: List[str]):
        self.chars = chars


    def count_chars(self) -> int:
        return len(self.chars)
