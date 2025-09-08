import os

LOGO = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

NAME_PROMPT = "What is your name?: "
BID_PROMPT = "What's your bid?: $"
CONTINUE_PROMPT = "Are there any other bidders? Type 'yes' or 'no'.\n"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_bid():
    name = input(NAME_PROMPT)
    while True:
        try:
            price = int(input(BID_PROMPT))
            break
        except ValueError:
            print("Please enter a valid number for the bid.")
    return name, price


def ask_continue():
    return input(CONTINUE_PROMPT).strip().lower() == 'yes'


def find_highest_bidder(bidders):
    winner, highest_bid = max(bidders.items(), key=lambda item: item[1])
    print(f"The winner is {winner} with a bid of ${highest_bid}")


def main():
    print(LOGO)
    bidders = {}
    while True:
        name, price = get_bid()
        bidders[name] = price
        if not ask_continue():
            break
        clear_screen()
    clear_screen()
    find_highest_bidder(bidders)


if __name__ == '__main__':
    main()
