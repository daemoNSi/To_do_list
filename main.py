my_dict = {'apple': [5,'peps', 'chook'], 'banana': [3,'pook', 'look'], 'orange': [2, 'kek', 'nook']}
my_dict2 = {'peps': [5,'peps', 'chook'], 'cook': [3,'pook', 'look'], 'took': [2, 'kek', 'nook']}

one = 3
two = 'pook'

final_dict = dict(zip(range(len(my_dict)), list(my_dict.values())))
my_dict2.clear()
my_dict2.update(final_dict)
print(final_dict)
print(my_dict2)
