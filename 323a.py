d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
inverse_dic = {}
for key, value in d.items():
  inverse_dic[value] = key
print(inverse_dic)