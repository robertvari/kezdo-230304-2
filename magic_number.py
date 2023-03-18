import os, random

MIN = 1
MAX = 10

def main():
    clear_screen()
    print_intro()

def clear_screen():
    os.system("cls")

def print_intro():
    print("="*50, "MAGIC NUMBER GAME", "="*50)
    print(f"I have a number between {MIN} and {MAX}. Can you guess it?")

main()