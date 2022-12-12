symmetricalLetters = "AHIMOTUVWXY"
name = input()

for letter in name:
  if letter not in symmetricalLetters:
    print("NO")
    exit(0)

if (name == name[::-1]):
  print("YES")
else:
  print("NO")