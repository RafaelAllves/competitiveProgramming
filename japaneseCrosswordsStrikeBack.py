n, x = input().split(' ')
n, x = int(n), int(x)
string = input().split(' ')
score = len(string)-1

for char in string:
  score += int(char)


if(score == x):
  print('YES')
else:
  print('NO')
