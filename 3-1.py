s = input()
inputArr = s.split()
for i in range(0, len(inputArr)):
  inputArr[i] = int(inputArr[i])
sum = 0
for i in range(0, len(inputArr)):
    if (i % 2 == 0):
      sum = sum + inputArr[i]
print(sum)