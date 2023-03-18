import os, random

MIN = 1
MAX = 10

def main():
    clear_screen()
    print_intro()

    # start game
    game_loop()

def clear_screen():
    os.system("cls")

def print_intro():
    print("="*50, "MAGIC NUMBER GAME", "="*50)
    print(f"I have a number between {MIN} and {MAX}. Can you guess it?")

def get_magic_number():
    return random.randint(MIN, MAX)

def game_loop():
    magic_number = get_magic_number()
    print(f"MAGIC NUMBER: {magic_number}")

    tries = 3
    print(f"You have {tries} tries.")

    # ask player guess
    player_guess = get_player_guess()
    
    # check player guess
    while player_guess != magic_number:
        clear_screen()

        # remove one tries
        tries -= 1
        if tries == 0:
            break

        print(f"Wrong guess. You have {tries} tries left. Try again!")
        player_guess = get_player_guess()
    
    check_results(magic_number, player_guess)

def check_results(magic_number, player_guess):
    if player_guess == magic_number:
        print(f"You win! {magic_number} was my number! :)))")
    else: 
        print(f"My number was {magic_number}.")

    ask_play_again()

def ask_play_again():
    player_choice = input("Do you want to play again? (y/n)")
    if player_choice == "y":
        clear_screen()
        game_loop()
    else:
        clear_screen()
        print("Maybe next time. Good bye!")
        exit()
    
def get_player_guess():
    player_input = input("Your Guess?")
    
    try:
        result = int(player_input)
        if result < MIN or result > MAX:
            print(f"The number must be between {MIN} and {MAX}")
            get_player_guess()
        
        return result
    except ValueError:
        print("I need a number")
        get_player_guess()

main()