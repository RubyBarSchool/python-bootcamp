logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
enc_dec = ['encode', 'decode']
go_again_list = ['yes', 'no']
direction = ''
message = ''
shift = 0
go_again = ''

output = []

def input_direction():
   global direction
   while True:
       direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
       if direction in enc_dec:
           break
       else:
           print("Invalid input, please try again.")

def input_message():
    global message
    while True:
        message = input("Type your message:\n").lower()
        if len(message) != 0:
            break
        else:
            print("Invalid input, please try again.")

def input_shift():
    global shift
    while True:
        value_shift = input("Type the shift number:\n").lower()
        if value_shift.isdigit():
            shift = int(value_shift)
            break
        else:
            print("Invalid input, please try again.")

def input_go_again():
    global go_again
    while True:
        go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if go_again in go_again_list:
            break
        else:
            print("Invalid input, please try again.")

def encrypt():
    global output
    for char in message:
        if char in alphabet:
            index_old = alphabet.index(char)
            index_new = (index_old + shift) % len(alphabet)
            output.append(alphabet[index_new])
        else:
            output.append(char)

def decrypt():
    global output
    for char in message:
        if char in alphabet:
            index_old = alphabet.index(char)
            index_new = (index_old - shift) % len(alphabet)
            output.append(alphabet[index_new])
        else:
            output.append(char)


def program():
    while True:
        input_direction()
        input_message()
        input_shift()
        if direction == 'encode':
            encrypt()
        else:
            decrypt()
        print(f'Here\\\'s the encoded result: {"".join(output)}')
        input_go_again()
        if go_again != 'yes':
            print("Goodbye")
            break
def main():
    print(logo)
    program()

if __name__ == "__main__":
    main()
