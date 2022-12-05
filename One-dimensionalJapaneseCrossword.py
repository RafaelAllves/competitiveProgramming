n = int(input())
array = input()
cryptography = []
numberOfBlocks = 0
count = 0
for i in range(len(array)):
  square = array[i]

  if (square == 'B'):
    count += 1

  if (((square == 'W' and i != 0) or (i == (len(array) - 1))) and count != 0):
    cryptography.append(count)
    count = 0
    numberOfBlocks += 1

print(numberOfBlocks)
for j in cryptography:
  print(j, end = ' ')
print()

