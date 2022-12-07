board=[['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]


totalX = 0
total0 = 0
next='first'
theFirstPlayerWon = False
theSecondPlayerWon = False


for i in range(3):
  row = input()
  for j in range(3):
    board[i][j] = row[j]
    if(row[j] == 'X'):
      totalX += 1
    elif (row[j] == '0'):
      total0 += 1

if((totalX - total0) == 1):
  next='second'
elif((totalX - total0) == 0):
  next='first'
else:
  print('illegal')
  exit(0)


for i in range(3):
  seqXH = 0
  seq0H = 0
  
  for j in range(3):

    if(board[i][j] == 'X'):
      seqXH += 1
      seq0H = 0
      if(seqXH >= 3):
        theFirstPlayerWon=True
    elif(board[i][j] == '0'):
      seq0H += 1
      seqXH = 0
      if(seq0H >= 3):
        theSecondPlayerWon=True
    else:
      seqXH = 0
      seq0H = 0
      break




for i in range(3):
  seqXV = 0
  seq0V = 0
  
  for j in range(3):

    if(board[j][i] == 'X'):
      seqXV += 1
      seq0V = 0
      if(seqXV >= 3):
        theFirstPlayerWon=True
    elif(board[j][i] == '0'):
      seq0V += 1
      seqXV = 0
      if(seq0V >= 3):
        theSecondPlayerWon=True
    else:
      seqXV = 0
      seq0V = 0
      break






seqXD = 0
seq0D = 0
for i in range(3):
  if(board[i][i] == 'X'):
    seqXD += 1
    seq0H = 0
    if(seqXD >= 3):
      theFirstPlayerWon=True
  elif (board[i][i] == '0'):
    seq0D += 1
    seqXD = 0
    if(seq0D >= 3):
      theSecondPlayerWon=True
  else:
    seqXD = 0
    seq0D = 0
    break



seqXD = 0
seq0D = 0
for i in range(3):
  if(board[i][2-i] == 'X'):
    seqXD += 1
    seq0D = 0
    if(seqXD >= 3):
      theFirstPlayerWon=True
  elif (board[i][2-i] == '0'):
    seq0D += 1
    seqXD = 0
    if(seq0D >= 3):
      theSecondPlayerWon=True
  else:
    seqXD = 0
    seq0D = 0
    break


if(theFirstPlayerWon and theSecondPlayerWon):
  print('illegal')
  exit(0)

if(theFirstPlayerWon):
  if((total0 + 1) == totalX):
    print('the first player won')
  else:
    print('illegal')
  exit(0)

if(theSecondPlayerWon):
  if(total0 == totalX):
    print('the second player won')
  else:
    print('illegal')
  exit(0)

if((totalX + total0) == 9):
  print('draw')
else:
  print(next)