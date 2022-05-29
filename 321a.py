l = [1, 4, 1 ,6, 'hello', 'a', 5, 'hello']
l_u = []
for i in l:
  if i  not in l_u:
    l_u.append(i)
print(l_u)
# print(list(set(l)))