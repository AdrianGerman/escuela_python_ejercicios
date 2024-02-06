# datos
age = 22

# ejecución
# print(f'Mi edad es: {age}')

# se le pide al usuario que ingrese su edad, en espera del teclado
age = input('Escribe tu edad => ')

# se imprime el tipo de dato de la edad proporcionada por el usuario
print(type(age))

# convertimos el tipo de dato proporcionado a un int para poder hacer las operaciones correspondientes
age = int(age)
print(type(age))

# se hace una suma a la edad para calcular su edad en 10 años
age += 10

# imprime el resultado de la edad proporcionada mas la suma realizada
print(f'Tu edad en 10 años sera: {age}')

# otro metodo para transformar datos directamente desde el input
age = int(input('Escribe tu edad => '))
print(type(age))
age += 10

print(f'Tu edad en 10 años sera: {age}')



