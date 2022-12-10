x1, y1, x2, y2 = input().split(' ')
x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

x, y= input().split(' ')
x, y= int(x), int(y)

if ((abs(x1 - x2) % x != 0) or (abs(y1 - y2) % y != 0)):
	print('NO')
elif ((abs(x1 - x2) / x) % 2 == abs(y1 - y2) / y % 2):
  print('YES')
else:
  print('NO')