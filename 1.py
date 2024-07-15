import random

# ANSI color codes for text formatting
class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'
    YELL = '\033[33m'
    MAG = '\033[35m'

# Function to display the game banner
def display_banner():
    banner = f"""
    {Color.HEADER}===============================
    Welcome to {Color.OKBLUE}Rock, Paper, Scissors!{Color.HEADER}
    ================================{Color.ENDC}
    """
    print(banner)

# Function to generate a random choice for the computer
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to get the user's choice and validate it
def get_user_choice():
    print(f"{Color.CYAN}Choose your option:")
    print(f"{Color.OKBLUE}1. Rock")
    print(f"{Color.YELL}2. Paper")
    print(f"{Color.CYAN}3. Scissors{Color.ENDC}")
    
    while True:
        user_choice = input(f"{Color.CYAN}Enter the number of your choice: {Color.ENDC}")
        if user_choice in ['1', '2', '3']:
            break
        else:
            print(f"{Color.FAIL}Invalid choice. Please enter 1, 2, or 3.{Color.ENDC}")
    
    if user_choice == '1':
        return 'rock'
    elif user_choice == '2':
        return 'paper'
    elif user_choice == '3':
        return 'scissors'

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"{Color.WARNING}It's a tie!{Color.ENDC}"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return f"{Color.OKGREEN}You win!{Color.ENDC}"
    else:
        return f"{Color.FAIL}Computer wins!{Color.ENDC}"

# Function to play the game
def play_game():
    display_banner()
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        print(f"\n{Color.MAG}Computer chose: {computer_choice}")
        print(f"You chose: {Color.CYAN}{user_choice.capitalize()}{Color.ENDC}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input(f"{Color.YELL}\nDo you want to play again? (y/n): {Color.ENDC}").lower()
        if play_again != 'y':
            print(f"{Color.HEADER}Thanks for playing! Goodbye!{Color.ENDC}")
            break

# Main entry point of the application
if __name__ == "__main__":
    play_game()
