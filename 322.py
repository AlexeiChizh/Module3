from random import randint
n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
print(m)
maximum = m[0][0]
for i in range(n):
  for j in range(n):
    if m[i][j] > maximum:
      maximum = m[i][j]
print(maximum)