print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15: $"))
people = int(input("How many people to split the bill? "))
if people == 0 : people = 1
print("Each person should pay: $" + str(format(round((bill+bill*tip/100)/people,2),".2f")))