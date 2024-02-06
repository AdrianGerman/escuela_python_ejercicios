# se repite 'col' para que podamos ver que no se permiten datos duplicados y automaticamente los elimuna
set_countries = {'col', 'mex', 'bol', 'col'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 77, 34}
print(set_numbers)

set_types = {1, 'hola', False, 13.77}
print(set_types)

# separa las letas de la palabra y crea el conjunto(set)
set_from_string = set('adrian')
print(set_from_string)

set_from_tuple = set(('abc', 'cvb', 'ase', 'abc'))

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)
print(type(unique_numbers))