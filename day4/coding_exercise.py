#Ex1
import random


print(random.randint(1,10))
print(random.random())
print(random.uniform(1,2))

if random.randint(1,10) < 5:
    print("Heads")
else:
    print("Tails")

#ex2
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(friends[random.randint(0, len(friends)-1)])
