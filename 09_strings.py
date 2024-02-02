# busca un palabra dentro del texto, si la encuentra retorna true y si no, false
print('*' * 50)
text = 'El sabe programar en Python'
print('Texto para analizar =>',text)
print('*' * 50)
print('')
print(f'¿Econtramos la palabra "JavaScript" en el texto? => {"JavaScript" in text}')
print('¿Econtramos la palabra "Python" en el texto? =>','Python' in text)

# sirve para saber cuantos caracteres tiene nuestro texto
print('')
size = len(text)
print(f'El texto tiene => {size} caracteres')

print('')
# pasar nuestro texto a mayusculas
print('Texto transformado a mayusculas =>',text.upper())
# pasar nuestro texto a minuculas
print('Texto transformado a minusculas =>',text.lower())
# contar cuantas veces se repite una letra en el texto
print('La letra "a" se repite =>',text.count('a'),'veces')
# invierte las mayusculas y minusculas del texto
print('Texto con las mayusculas y minusculas invertidas =>',text.swapcase())
# para verificar si el texto inicia con una palabra especifica
print('¿El texto comienza con "El"? =>',text.startswith('El'))
# para verificar si el texto termina con una palabra especifica
print('¿El texto termina con "JavaScript"? =>',text.endswith('JavaScript'))

# remplaza la cadena de texto por otra especificada
print('Texto modificado con "replace":\n  ',text.replace('Python','Rust'))

# ejemplo #2
print('\n')
print('Ejemplo #2')
print('*' * 50)
text_2 = 'este es un titulo'
print(text_2)
print('*' * 50)

# convierte la primer letra en mayuscula
print('')
print(text_2.capitalize())

# convierte la primera letra en mayuscula de cada palabra
print('')
print(text_2.title())

# analiza si el texto puede convertirse en un int
print('')
print('El texto puede ser un int =>',text_2.isdigit())

print('"777" puede ser un int =>','777'.isdigit())


