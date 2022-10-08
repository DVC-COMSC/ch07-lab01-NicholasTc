
# ******************************
# Make your Code
# ******************************
numbers = []
total = 0

# taking user input
for i in range(5):
    num = int(input())
    numbers.append(num)

# processing the list
minNum = min(numbers)
maxNum = max(numbers)

for n in numbers:
    total += n

total = total - (minNum + maxNum)

print(total)
