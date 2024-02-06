from components.Game.InitGame import InitGame


def hangman_game():
# After a word has been chosen the game can start
    print("----Welcome to Hangman---- (Beta)")
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
    running_status = True
    game = InitGame()
    game.set_running_status(running_status)
    game.start_game(input_difficulty) # Difficulty is being set trough here


    while(running_status):
        if (game.game_manager.check_score() > 0):
            test = game.game_manager.display_word()
            print(test)
            
            
            print()
            input_letter = input("Enter a letter: ")


            game.game_manager.set_letter(input_letter)
            print(f"{game.game_manager.check_input()}")
        elif "_" not in game.game_manager.get_char().list_of_chars():
            print("You won!")
            running_status = game.stop_game()
        else:
            running_status = game.stop_game()


hangman_game()
