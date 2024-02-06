my_dict = {}
print(type(my_dict))

my_dict = {
    'name': 'Adrian',
    'last_name': 'German Becerra',
    'age': 22
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
# este es un mejor modo de llamar un valor del diccionario
print(my_dict.get('age'))

# true si el valor si existe en el diccionario
print('name' in my_dict)
# false si el valor no existe en el diccionario
print('estevalornoexiste' in my_dict)