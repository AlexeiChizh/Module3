dict_list = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
inverse_dict=dict([val,key] for key,val in dict_list.items())
print(inverse_dict)