logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

first_q = "What's the first number?: "
second_q = "What's the next number?: "
operator_q = """
+
-
*
/
Pick an operation: """
first_num = 0.0
second_num = 0.0
operator = ""
result = 0.0


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Error: Division by zero is undefined.")
        return None
    return n1 / n2

def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def input_operator(prompt):
    while True:
        op = input(prompt)
        if op in ['+', '-', '*', '/']:
            return op
        else:
            print("Invalid operator. Please pick one of +, -, *, /.")

def input_continue():
    global result
    while True:
        cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if cont in ['y', 'n']:
            return cont
        else:
            print("Invalid input. Please type 'y' or 'n'.")

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculate():
    global first_num, second_num, operator, result
    print(logo)
    first_num = input_number(first_q)
    while True:
        operator = input_operator(operator_q)
        second_num = input_number(second_q)
        #solution 1
        # if operator == "+":
        #     result = add(first_num, second_num)
        # elif operator == "-":
        #     result = subtract(first_num, second_num)
        # elif operator == "*":
        #     result = multiply(first_num, second_num)
        # elif operator == "/":
        #     result = divide(first_num, second_num)
        #     if result is None:
        #         continue

        #solution 2
        result = operations[operator](first_num, second_num)
        if result is None:
            continue

        print(f"{first_num} {operator} {second_num} = {result}")
        if input_continue() == 'y':
            first_num = result
        else:
            break
    calculate()

def main():
    calculate()

if __name__ == "__main__":
    main()
