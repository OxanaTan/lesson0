my_dict = {'Olga': 1996,
           'Maxim': 1992,
           'Masha': 2004}
print(my_dict)
print(my_dict['Olga'])
print(my_dict.get('Anna'))
my_dict.update({'Oxana': 1994,
                'Nikita': 1999})
print(my_dict)
my_dict.pop('Maxim')
print(my_dict)

my_set = {1, 1, 2, 2, 3, 'a', 'b', 'a', 'b', 'c'}
print(my_set)
print(my_set.add('good')); print(my_set.add(27))
print(my_set)
print(my_set.discard(1))
print(my_set)

