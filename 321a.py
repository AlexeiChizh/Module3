l = [1, 4, 1 ,6, 'hello', 'a', 5, 'hello']
l_u = []
for i in range(0, len(l)):
  for j in range(i + 1, len(l)):
    if (l[i] == l[j]):
      print(l[j])
      l_u.append(l[j])
print(l_u)
