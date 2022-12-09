n=int(input())
s=list(input())

keys=[0]*26
count=0
for i in range(0, (len(s)//2)):
  key = s[i*2]
  door = s[i*2+1]
  keys[ord(key)-97] += 1
  if (keys[ord(door)-65] > 0):
    keys[ord(door)-65] -= 1
  else:
    count+=1
print(count)