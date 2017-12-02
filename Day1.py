inputNumbers = input()

print(inputNumbers)


sum = 0

for x in range(len(inputNumbers)):
    if x != len(inputNumbers) - 1:
        if inputNumbers[x] == inputNumbers[x+1]:
            sum += int(inputNumbers[x])
    else:
        if inputNumbers[x] == inputNumbers[0]:
            sum += int(inputNumbers[0])

print(sum)

