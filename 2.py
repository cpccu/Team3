import random

class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'

# Sample quiz questions and answers
questions = [
    {
        "question": "What is the capital of Bangladesh?",
        "options": ["Chittagong", "Khulna", "Rajshahi", "Dhaka"],
        "correct_answer": 3  # Dhaka
    },
    {
        "question": "Which river is known as the lifeline of Bangladesh?",
        "options": ["Brahmaputra", "Padma", "Meghna", "Jamuna"],
        "correct_answer": 1  # Padma
    },
    {
        "question": "Who is the national poet of Bangladesh?",
        "options": ["Rabindranath Tagore", "Kazi Nazrul Islam", "Jibanananda Das", "Lalon Shah"],
        "correct_answer": 1  # Kazi Nazrul
    },
    {
        "question": "What is the national flower of Bangladesh?",
        "options": ["Rose", "Water Lily", "Marigold", "Sunflower"],
        "correct_answer": 1  # water lily
    },
    {
        "question": "In which year did Bangladesh gain independence?",
        "options": ["1947", "1952", "1971", "1990"],
        "correct_answer": 2  # 1971
    }
]

def display_banner():
    banner = f"""
    {Color.HEADER}====================================
             {Color.OKBLUE}Welcome to Quiz Time!{Color.HEADER}
    ===================================={Color.ENDC}
    """
    print(banner)

def display_question(question):
    print(f"{Color.CYAN}{question['question']}{Color.ENDC}")
    for idx, option in enumerate(question['options'], start=1):
        print(f"{Color.OKBLUE}{idx}. {option}{Color.ENDC}")

def get_user_answer():
    while True:
        try:
            user_answer = int(input(f"{Color.OKGREEN}Enter your answer (1-{len(questions[0]['options'])}): {Color.ENDC}"))
            if 1 <= user_answer <= len(questions[0]['options']):
                return user_answer - 1  # Adjusting to zero-based index
            else:
                print(f"{Color.FAIL}Invalid choice. Please enter a number between 1 and {len(questions[0]['options'])}.{Color.ENDC}")
        except ValueError:
            print(f"{Color.FAIL}Invalid input. Please enter a number.{Color.ENDC}")

def check_answer(question, user_answer):
    correct_answer_index = question['correct_answer']
    correct_answer = question['options'][correct_answer_index]
    user_answer_text = question['options'][user_answer]
    
    if user_answer == correct_answer_index:
        return True, correct_answer
    else:
        return False, correct_answer

def play_quiz():
    display_banner()
    score = 0

    for question in questions:
        display_question(question)
        user_answer = get_user_answer()
        is_correct, correct_answer = check_answer(question, user_answer)
        if is_correct:
            score += 1
            print(f"{Color.OKGREEN}Correct!{Color.ENDC}")
        else:
            print(f"{Color.FAIL}Incorrect. The correct answer is: {correct_answer}{Color.ENDC}")

    print(f"\n{Color.WARNING}Quiz completed! Your score is: {score}/{len(questions)}{Color.ENDC}")

if __name__ == "__main__":
    play_quiz()
