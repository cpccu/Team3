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

def display_banner():
    banner = f"""
    {Color.HEADER}===============================
    Welcome to {Color.OKBLUE}Rock, Paper, Scissors!{Color.HEADER}
    ================================{Color.ENDC}
    """
    print(banner)

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    user_choice = input(f"{Color.CYAN}Enter your choice ({Color.OKBLUE}rock, paper, {Color.YELL}or {Color.CYAN}scissors): {Color.ENDC}").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input(f"{Color.FAIL}Invalid choice. Please enter rock, paper, or scissors: {Color.ENDC}").lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"{Color.WARNING}It's a tie!{Color.ENDC}"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return f"{Color.OKGREEN}You win!{Color.ENDC}"
    else:
        return f"{Color.FAIL}Computer wins!{Color.ENDC}"

def play_game():
    display_banner()
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        print(f"\n{Color.MAG}Computer chose: {computer_choice}")
        print(f"You chose: {Color.CYAN}{user_choice}{Color.ENDC}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input(f"{Color.YELL}\nDo you want to play again? (yes/no): {Color.ENDC}").lower()
        if play_again != 'yes':
            print(f"{Color.HEADER}Thanks for playing! Goodbye!{Color.ENDC}")
            break

if __name__ == "__main__":
    play_game()
