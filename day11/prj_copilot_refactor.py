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

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(deck):
    """Returns a random card from the deck."""
    return random.choice(deck)


def calculate_score(hand):
    """Calculate the score of a hand. Returns 0 for Blackjack."""
    score = sum(hand)
    if score == 21 and len(hand) == 2:
        return 0  # Blackjack
    # Handle Ace (11) as 1 if over 21
    while 11 in hand and score > 21:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score


def print_info(user_hand, computer_hand, user_score):
    print(f"    Your cards: {user_hand}, current score: {user_score}")
    print(f"    Computer's first card: {computer_hand[0]}")


def print_final_info(user_hand, computer_hand, user_score, computer_score):
    print(f"    Your final hand: {user_hand}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_hand}, final score: {computer_score}")


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def user_turn(user_hand, deck):
    while True:
        user_score = calculate_score(user_hand)
        if user_score > 21:
            break
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
        while choice not in ['y', 'n']:
            choice = input("Please type 'y' or 'n': ")
        if choice == 'y':
            user_hand.append(deal_card(deck))
        else:
            break
    return user_hand


def computer_turn(computer_hand, deck, user_score):
    while calculate_score(computer_hand) < 17 and calculate_score(computer_hand) < user_score <= 21:
        computer_hand.append(deal_card(deck))
    return computer_hand


def play_game():
    deck = CARDS[:]
    user_hand = [deal_card(deck), deal_card(deck)]
    computer_hand = [deal_card(deck), deal_card(deck)]
    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)
    print_info(user_hand, computer_hand, user_score)
    user_hand = user_turn(user_hand, deck)
    user_score = calculate_score(user_hand)
    # Computer's turn only if user hasn't busted or got blackjack
    if user_score <= 21:
        computer_hand = computer_turn(computer_hand, deck, user_score)
    computer_score = calculate_score(computer_hand)
    print_final_info(user_hand, computer_hand, user_score, computer_score)
    print(compare(user_score, computer_score))


def main():
    print(logo)
    while True:
        play_game()
        again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        while again not in ['y', 'n']:
            again = input("Please type 'y' or 'n': ")
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == '__main__':
    main()