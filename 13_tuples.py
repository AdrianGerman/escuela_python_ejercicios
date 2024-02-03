numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'adri')
print(numbers)
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# las tuplas son inmutables y por ende no se pueden modificar

print(strings)
print(strings.index('zule'))
print(strings.count ('nico'))

# se deben de convertir a listas o strings para que se puedan modificar
my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'juli'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)