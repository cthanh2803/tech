n = int(input())
sumOfString = 0
inputString = input()
splitString = inputString.split()
lenOfArray = len(splitString)
for i in range(0, lenOfArray):
  sumOfString = sumOfString + ord(splitString[i])
print(sumOfString)