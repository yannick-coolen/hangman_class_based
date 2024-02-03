class WordChars:
    def set_word_in_chars(self, word: str) -> list[str]:
        """
        #### Description:\n
          Based on the given string value through the parameter,\n
          it will take all the character and append this separately\n
          into a list

        #### Args:
          word (str): The word value that has been taken\n
          from the txt.file

        #### Returns:
          list[str]: List of characters
        """
        word_chars: list[str] = []
        for x in range(len(word)):
            word_chars.append(word[x])
        return word_chars
