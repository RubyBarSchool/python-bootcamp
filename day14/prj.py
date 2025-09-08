from game_data import data
import random
from art import logo, vs

def show_players(a, b, score):
    print("\n" * 20)
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

def end(score):
    print(f"Sorry, that's wrong. Final score: {score}")

def question():
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    while guess not in ['a', 'b']:
        guess = input("Invalid input. Please type 'A' or 'B': ").lower()
    return guess

def calculate(a, b, guess):
    if a['follower_count'] > b['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'

def random_choice(score):
    data_choice = random.sample(data, 2)
    a = data_choice[0]
    b = data_choice[1]
    show_players(a, b, score)
    return a, b

def play():
    score = 0
    while True:
        a, b = random_choice(score)
        if calculate(a, b, question()) :
            score += 1
        else:
            end(score)
            break
def main():
    play()

if __name__ == "__main__":
    main()







