import math
infinite = math.inf
min = infinite

n, m = input().split(' ')
n, m = int(n), int(m)
array = input().split(' ')

intArray = [int(numericString) for numericString in array]
intArray.sort()

for i in range(len(intArray)-(n-1)):

  diff = intArray[i+n-1] - intArray[i]

  if(diff < min):
    min = diff
print(min)