class DisplayHangman:
    _index_hangman = [
        """
    +
    |
    |
    |
    |
    |
    """,
        """
    +-----+
    |
    |
    |
    |
    |
    """,
        """
    +-----+
    |/
    |
    |
    |
    |
    """,
        """
    +-----+
    |/    |
    |
    |
    |
    |
    """,
        """
    +-----+
    |/    |
    |     O
    |
    |
    |
    """,
    """
    +-----+
    |/    |
    |     O
    |     |
    |
    |
    """,
        """
    +-----+
    |/    |
    |     O
    |    -|
    |
    |
    """,
        """
    +-----+
    |/    |
    |     O
    |    -|-
    |
    |
    """,
        """
    +-----+
    |/    |
    |     O
    |    -|-
    |    /
    |
    """,
        """
    +-----+
    |/    |
    |     O
    |    -|-
    |    / \\
    |
    """,
    ]

    def get_display(self, amount_turns: int) -> str:
        length_index = len(self._index_hangman) - amount_turns
        return self._index_hangman[length_index - 1] if length_index > 0 else ""
