import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user = []
computer = []
user_score = 0
computer_score = 0


def scores(score_list):
    """Returns the sum of the cards in the list."""

    if sum(score_list) == 21 and len(score_list) == 2:
        return 0

    if 11 in score_list and sum(score_list) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(score_list)

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)

def info():
    """Displays the current hands and scores of the user and computer."""
    print(f"    Your cards: {user}, current score: {user_score}")
    print(f"    Computer's first card: {computer[0]}")

def final_info():
    """Displays the final hands and scores of the user and computer."""
    print(f"    Your final hand: {user}, final score: {user_score}")
    print(f"    Computer's final hand: {computer}, final score: {computer_score}")


def start():
    """Starts the game by dealing two cards to both the user and computer."""
    for _ in range(2):
        user.append(deal_card())
        computer.append(deal_card())
    global user_score, computer_score
    user_score = scores(user)
    computer_score = scores(computer)

def another_card():
    """Deals another card to the user and updates the score."""
    continue_q = input("Type 'y' to get another card, type 'n' to pass: ")
    while continue_q not in ['y', 'n']:
        continue_q = input("Please type 'y' or 'n': ")
    return continue_q

def continue_blackjack():
    """Handles the computer's turn to draw cards until reaching a score of at least 17."""
    continue_q = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    while continue_q not in ['y', 'n']:
        continue_q = input("Please type 'y' or 'n': ")
    return continue_q

def calculate_winner():
    """Calculates and displays the winner of the game."""
    final_info()
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def blackjack():
    """Main function to play the game of Blackjack."""
    global user_score, computer_score
    start()
    info()
    while another_card() == 'y':
        user.append(deal_card())
        user_score = scores(user)
        info()
        if user_score > 21:
            calculate_winner()
            return

    while user_score > computer_score:
        computer.append(deal_card())
        computer_score = scores(computer)
        if computer_score > 21:
            calculate_winner()
            return
    calculate_winner()

def main():
    """Main loop to start and restart the game."""
    print(logo)
    blackjack()
    while continue_blackjack() == 'y':
        print(logo)
        global user, computer, user_score, computer_score
        user = []
        computer = []
        user_score = 0
        computer_score = 0
        blackjack()


if __name__ == '__main__':
    main()