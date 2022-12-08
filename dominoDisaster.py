t = int(input())
for j in range(t):

  n = int(input())
  string = input()
  row = ['']*n
  complement = 'L'

  for i in range(n):
    char = string[i]
    if(char == 'U'):
      row[i] = 'D'
    elif(char == 'D'):
      row[i] = 'U'
    else:
      row[i] = complement
      if complement == 'L':
        complement = 'R'
      else:
        complement = 'L'

  print(''.join(row))
