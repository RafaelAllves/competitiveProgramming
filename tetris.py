n, m = input().split(' ')
n, m = int(n), int(m)
array = input().split(' ')

top = [0]*n
platform = [[0]*n]*m
score = 0

for i in range(m):
  column = int(array[i])-1
  platform[top[column]][column] = 1
  top[column] = top[column] + 1

print(min(top))