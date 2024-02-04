# declaramos nuestro diccionario
person = {
    'name': 'gregorio',
    'last_name': 'Robinson',
    'langs': ['python', 'javascript'],
    'age': 67    
}

print(person)

# modificar diccionario
person['name'] = 'german'
# restar a la edad actual 50 y se modifica el campo
person['age'] -= 50
# se agrega un nuevo valor a la lista de lenguajes
person['langs'].append('rust')
print(person)

# eliminacion diccionario
del person['last_name']
person.pop('age')
print(person)

# nos imprime los valores de nuestro diccionario, dividido
print('items')
print(person.items())

# nos imprime solo los atributos o keys de nuestro diccionario
print('keys')
print(person.keys())

# nos imprime solo los valores de nuestro diccionario
print('values')
print(person.values())
