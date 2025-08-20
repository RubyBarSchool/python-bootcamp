import random

word_list = ["aardvark", "baboon", "camel"]
output = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
"""
count = 6

print(output)
target = random.choice(word_list)
print(target)
guess = ''

for i in target:
    guess += '_'

def assign_question():
    global count
    print("Word to guess: " + guess)
    ip =input("Guess a letter:  ")
    result = calculate_answer(ip)
    if not result:
        count = count - 1
        print("You guessed " + ip +", that's not in the word. You lose a life.")
    else:
        print("You've already guessed "+ip)
        print(guess)

    show_hang_man(count)


def calculate_answer(character):
    global guess
    checkExist = False
    for index in range(len(target)):
        if character == target[index]:
            guess = change_character(target[index], index)
            checkExist = True

    return checkExist

def change_character(character, index):
    global guess
    arr = list(guess)
    arr[index] = character
    return  "".join(arr)


def show_hang_man(count):
    match count:
        case 6:
            print("""
                  +---+
                  |   |
                      |
                      |
                      |
                      |
                =========
                """)
        case 5:
            print("""
                  +---+
                  |   |
                  O   |
                      |
                      |
                      |
                =========
                """)
        case 4:
            print("""
                  +---+
                  |   |
                  O   |
                  |   |
                      |
                      |
                =========
                """)
        case 3:
            print("""
                  +---+
                  |   |
                  O   |
                 /|   |
                      |
                      |
                =========
                """)
        case 2:
            print("""
                  +---+
                  |   |
                  O   |
                 /|\  |
                      |
                      |
                =========
                """)
        case 1:
            print("""
                  +---+
                  |   |
                  O   |
                 /|\  |
                 /    |
                      |
                =========
                """)

while True:
    assign_question()
    if count == 0 or target == guess:
        break
    print("****************************" + str(count) + "/6 LIVES LEFT****************************")

if count == 0:
    print("***********************IT WAS " + target + "! YOU LOSE**********************")
else:
    print("Win")









