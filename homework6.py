my_dict = {'Gen': 1993, 'Yuka': 1996, 'Kate': 1990, 'Oleg': 1982, 'John': 1965}
print(my_dict)
print(my_dict.get('Yuka'))
print(my_dict.get('Sasha'))
my_dict['Irene'] = 1975
my_dict['Sean'] = 1999
a = my_dict.pop('Kate')
print(a)
print(my_dict)


my_set = {(1, 2, 3), 4, 5, 'Gen', True, 2, 4, 'Gen', True, False}
print(my_set)
my_set.add('Cool')
my_set.add(10.175)
my_set.remove(4)
print(my_set)