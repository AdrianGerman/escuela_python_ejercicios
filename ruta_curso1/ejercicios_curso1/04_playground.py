person = {
    'name': 'Adrian',
    'lastName': 'Lopez',
    'age': 29
}

# Escribe tu solución 👇

# Agregar un nuevo elemento al dicc con la llave 'twitter' y el valor '@usertwitter'
person['twitter'] = ('@usertwitter')

# Actualiza el valor del elemento con la llave "name" con el valor "Felipe"
person['name'] = 'Felipe'

# Elimina el elemento del diccionario con la llave 'age'
del person['age']

# Imprime una lista con las llaves del diccionario
print(list(person.keys()))

# Imprime una lista con los valores del diccionario
print(list(person.values()))