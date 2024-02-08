import random
from io import TextIOWrapper
from typing import List


class WordSelector:
    def get_word_from_file(self, difficulty: str | None) -> str:
        """
        #### Description:
          Takes a word from a text file
        """

        file: TextIOWrapper = open("wordlist.txt", "r")

        lines = self._check_length_for_word(file, difficulty)

        word = random.choice(lines)
        file.close()
        return word


    def _check_length_for_word(self, file: TextIOWrapper, difficulty: str | None):
        lines: List[str] = []

        if difficulty == "easy":
            lines = [
                line.strip() for line in file.readlines() 
                if len(line.strip()) >= 13
            ]
        elif difficulty == "normal":
            lines = [
                line.strip() for line in file.readlines() 
                if len(line.strip()) <= 12
            ]
        elif difficulty == "hard":
            lines = [
                line.strip() for line in file.readlines() 
                if len(line.strip()) <= 6
            ]

        return lines
