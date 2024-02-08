from components.Display.DisplayLogo import DisplayLogo
from components.Game.InitGame import InitGame


def hangman_game():
# After a word has been chosen the game can start
    DisplayLogo().logo()
    print("(Beta)\n")
    print("Choose your dificulty, or if enter 0 to quit the game") 
    print("\n<<Note: the selection is not successfully done yet.")
    print("This is still in pending")
    print("Any selection under zero (0) or above three (3),")
    print("or is not a numeric value will beark this game.>>\n") 
    print("1: Easy\n2: Normal\n3: Hard")
    
    input_difficulty = int(input("Enter a value: "))
    
    print("-"*5)
    if input_difficulty == 0:
        print("Game has stopped")
        return None
    else:
        start_hangman_game(input_difficulty)


def start_hangman_game(input_difficulty: int) -> str | None:
    game = InitGame()
    game.start_game(input_difficulty) # Difficulty is being set trough here


hangman_game()
