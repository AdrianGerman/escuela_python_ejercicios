text = 'Ella sabe Python' 

# extraemos del texto la letra que se encuentre en la posicion especificada
print(text[0])
print(text[1])
# si no existe la posicion => print(text[999]) nos retorna un error

print('')
size = len(text)
# imprime la longitud de nuestro text
print('size =>',size)
# con size detectamos el ultimo valor
print(text[size -1])
# -1 significa el primer valor del final
print(text[-1])

# slicing
print('')

print('')
print('Pruebas 1')
print('*' * 10)

print(text[0:5])

print('')
print('Pruebas 2')
print('*' * 10)

print(text[10:16])
print(text[:10])

print('')
print('Pruebas 3')
print('*' * 10)

print(text[5:-1])
print(text[5:])

print('')
print('Pruebas 4')
print('*' * 10)

print(text[:])

print('')
print('Pruebas 5')
print('*' * 10)

print(text[10:16:1])
print(text[10:16:2])
print(text[::2])

print('')
print('Pruebas 6')
print('*' * 10)

print(text[::-1])
print(text[16:9:-1])

