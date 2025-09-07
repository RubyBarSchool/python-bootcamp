import random
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

WELLCOME = "Welcome to the Number Guessing Game!"
NUMBER_PROMPT = "I'm thinking of a number between 1 and 100."

def choose_difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if difficulty == 'easy':
            return 10
        elif difficulty == 'hard':
            return 5
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")

def make_guess():
    while True:
        try:
            guess = int(input("Make a guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_guess(guess, answer):
    if guess < answer:
        print("Too low.")
        return False
    elif guess > answer:
        print("Too high.")
        return False
    else:
        print(f"You got it! The answer was {answer}.")
        return True

def start_game():
    print(logo)
    print(WELLCOME)
    print(NUMBER_PROMPT)

    answer = random.randint(1, 100)
    attempts = choose_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = make_guess()
        if check_guess(guess, answer):
            break
        attempts -= 1
        if attempts == 0:
            print(f"You've run out of guesses. The number was {answer}.")
        else:
            print("Guess again.")

def main():
    while True:
        start_game()
        if input("Do you want to play again? Type 'y' or 'n': ").strip().lower() != 'y':
            break
        print("\n" * 100)  # Clear the screen

if __name__ == '__main__':
    main()