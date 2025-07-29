
#Ex2
number = int(input("What is the number you want to check? "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Ex4
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

money = 0

if size.lower() == "S".lower():
    money += 15
elif size.lower() == "M".lower():
    money += 20
else:
    money += 25

if pepperoni.lower() == "y".lower():
    if size.lower() == "S".lower():
        money += 2
    else:
        money += 3

if extra_cheese.lower() == "y".lower():
    money += 1

print("Your final bill is: $"+ str(money)+".")