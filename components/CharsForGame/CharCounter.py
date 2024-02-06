from typing import List


class CharCounter:
    """
    #### Description:
     
    This class its role runs as a DTO, to retrieve the data, 
    holds it, until it's needed again.
    
    #### Returns: 
    None in default..
    """

    def __init__(self, chars: List[str]) -> None:
        self.chars = chars


    def get_length_of_chars(self) -> int:
        """
        #### Description:
            retrieve the chars as the total length.
            
         NOTE: 
            the length might diverge as expected, 
            and should be increased by one outside this
            scope.
            
        #### Returns:
            A length of chars in a int value
        """
        return len(self.chars)
