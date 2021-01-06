inputString = input()
arrBlack = []
arrWhite = []
for i in range(0,len(inputString)):
  if (inputString[i] == 'B'):
    arrBlack.append(i + 1)
  if (inputString[i] == 'W'):
    arrWhite.append(i + 1)
sumBlack = 0
sumWhite = 0
for i in range(len(arrBlack) - 1, -1, -1):
  for j in range(i - 1, -1, -1):
    sumBlack = sumBlack + arrBlack[i] - arrBlack[j] + 1
for i in range(len(arrWhite) - 1, -1, -1):
  for j in range(i - 1, -1, -1):
    sumWhite = sumWhite + arrWhite[i] - arrWhite[j] + 1
print(sumBlack, sumWhite)