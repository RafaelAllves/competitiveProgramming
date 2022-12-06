board=[['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]

for i in range(4):
  row = input()
  seqH = 0
  haveSpace = False
  
  for j in range(4):
    board[i][j] = row[j]

    if(row[j] == 'x'):
      seqH+=1
      if(seqH >= 3):
        print('YES')
        exit(0)
    elif(row[j] == '.'):
      if(haveSpace):
        if(board[i][j-1] == '.'):
          seqH = 1
      else:
        seqH+=1
        haveSpace = True
        if(seqH >= 3):
          print('YES')
          exit(0)
    else:
      seqH = 0
      haveSpace = False



for i in range(4):
  seqV = 0
  haveSpace = False
  for j in range(4):
    if(board[j][i] == 'x'):
      seqV+=1
      if(seqV >= 3):
        print('YES')
        exit(0)
    elif (board[j][i] == '.'):
      if(haveSpace):
        if(board[j-1][i] == '.'):
          seqV = 1
      else:
        seqV+=1
        haveSpace = True
        if(seqV >= 3):
          print('YES')
          exit(0)
    else:
      seqV = 0
      haveSpace = False


seqD = 0
haveSpace = False
for i in range(4):
  if(board[i][i] == 'x'):
    seqD+=1
    if(seqD >= 3):
      print('YES')
      exit(0)
  elif(board[i][i] == '.'):
    if(haveSpace):
      if(board[i-1][i-1] == '.'):
        seqD = 1
    else:
      seqD+=1
      haveSpace = True
      if(seqD >= 3):
        print('YES')
        exit(0)
  else:
      seqD = 0
      haveSpace = False


seqD = 0
haveSpace = False
for i in range(4):
  if(board[i][3-i] == 'x'):
    seqD+=1
    if(seqD >= 3):
      print('YES')
      exit(0)
  elif(board[i][3-i] == '.'):
    if(haveSpace):
      if(board[i-1][j-i+1] == '.'):
        seqD = 1
    else:
      haveSpace = True
      seqD+=1
    if(seqD >= 3):
      print('YES')
      exit(0)
  else:
    seqD = 0
    haveSpace = False




aux = [
  [board[0][2], board[1][1], board[2][0]],
  [board[0][1], board[1][2], board[2][3]],
  [board[1][0], board[2][1], board[3][2]],
  [board[1][3], board[2][2], board[3][1]]
]


for i in range(4):
  seqD = 0
  haveSpace = False
  for j in range(3):
    if(aux[i][j] == 'x'):
      seqD+=1
      if(seqD >= 3):
        print('YES')
        exit(0)
    elif(aux[i][j] == '.'):
      if(haveSpace):
        seqD = 1
      else:
        seqD+=1
        haveSpace = True
      if(seqD >= 3):
        print('YES')
        exit(0)
    else:
      seqD = 0
      haveSpace = False

print('NO')