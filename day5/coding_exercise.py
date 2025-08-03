#Ex1
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))


total = 0
maxValue = student_scores[0]

for score in student_scores:
    total += score
    if score > maxValue:
        maxValue = score

print("Sum: ", total)
print("Max: ", maxValue)


print("Function sum: ",sum(student_scores))

print("Function max: ", max(student_scores))

#Ex2
sum = 0

for number in range(1, 101):
    sum += number

print("Sum: ", sum)



