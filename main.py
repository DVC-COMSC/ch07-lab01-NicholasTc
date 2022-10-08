
# ******************************
# Make your Code
# ******************************
numbers = []
total = 0

# taking user input
for i in range(5):
    num = int(input())
    numList.append(num)

# processing the list
minNum = min(numList)
maxNum = max(numList)

for n in numList:
    total += n

total = total - (minNum + maxNum)

print(total)
