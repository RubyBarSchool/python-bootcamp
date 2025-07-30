import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_shape = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper,  2 for Scissors or 3 End.")
inputChoice = 0
first = True
while True :
    if not first:
        print("Do you want more times? Type 0 for Rock, 1 for Paper,  2 for Scissors or 3 End.")

    inputChoice = int(input())
    computerChoice = random.randint(0, 2)
    first = False
    if inputChoice < 0 or inputChoice > 3:
        print("Invalid input. Try again.")
        continue
    elif inputChoice == 3:
        print("Have a nice day!")
        break

    print("You chose:", game_shape[inputChoice])
    print("Computer chose:", game_shape[computerChoice])

    if inputChoice == computerChoice:
        print("It's a draw!")
    elif inputChoice < computerChoice:
        if inputChoice + 1 == computerChoice:
            print("You lose!")
        else:
            print("You win!")
    else:
        if computerChoice + 1 == inputChoice:
            print("You win!")
        else:
            print("You lose!")