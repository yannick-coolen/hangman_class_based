from components.Game.InitGame import InitGame


def start_hangman():
# After a word has been chosen the game can start
    print("----Welcome to Hangman---- (Beta)")
    print("Choose your dificulty") 
    print("\n<<Note: the selection is not successfully done yet.")
    print("This is still in pending")
    print("Any selection under one (1) or above three (3)")
    print("will beark this game.>>\n") 
    print("1: Easy\n2: Normal\n3: Hard")
    
    
    input_difficulty = int(input("Enter a value: "))
    
    print("-"*5)
    hangman_game(input_difficulty)


def hangman_game(input_difficulty: int) -> str | None:
    game = InitGame()
    game.start_game(input_difficulty)

    # while(game.game_is_running()):
    # if (game.get_score().get_turns() > 0):
    test = game.display_word()
    print(test)

    print("Enter a letter")
    input_letter = input()

    game.game_manager.set_letter(input_letter)
    return f"{game.check_input_value()}"


start_hangman()