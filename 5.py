number = int(input())
inputNumber = input().split()
for i in range(0, len(inputNumber)):
  inputNumber[i] = int(inputNumber[i])
minNumber = inputNumber[0]
minNumberIndex = 0
findNumber = 0
for i in range(0, len(inputNumber)):
  if(minNumber > inputNumber[i]):
    minNumber = inputNumber[i]
if (minNumber > 0):
  findNumber = minNumber - 1
else:
  findNumber = 1 - (minNumber)
for i in range(0, len(inputNumber)):
  if(inputNumber[i] > 0):
    inputNumber[i] = inputNumber[i] - findNumber
  else:
    inputNumber[i] = inputNumber[i]  + findNumber
for i in range(0, len(inputNumber)):
  print(inputNumber[i], end=' ')

