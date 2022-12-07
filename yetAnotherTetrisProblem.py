t = int(input())

for j in range(t):
  n = int(input())
  array = input().split(' ')
  intArray = [int(numericString) for numericString in array]

  first = intArray[0] % 2

  isPossible=True

  for i in intArray:
    if(i%2 == first):
      continue
    else:
      isPossible=False
      break

  if(isPossible):
    print("YES")
  else:
    print("NO")
