import random

countries = ['col', 'mex', 'bol', 'pe']

population_v2 = { country: random.randint(1, 100) for country in countries }
print(population_v2)

# imprime los paises que su poblacion es mayor a 20, en cada ejecución 
# es diferente ya que se genera la poblacion de manera aleatoria
result = { country: population for (country, population) in population_v2.items() if population > 20 }
print(result)


# se genera un diccionario solo con las vocales del texto y las pone en mayusculas: 'a': 'A'
text = 'Hola soy German'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)

# ejercicio para modificar la frecuencia ###################################
text = 'Hola soy German'
unique = { c: text.count(c) for c in set(text) if c in 'aeiou' }
print(unique)