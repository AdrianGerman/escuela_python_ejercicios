# and
print('AND')
print('*' * 25)
print('True and True =>',True and True) #true
print('True and False =>',True and False) #false
print('False and True =>',False and True) #false
print('False and False =>',False and False) #false
# para que retorne true las 2 condiciones deben regresar true

print('')
print('AND con valores numericos')
print('*' * 25)
print(10 > 5 and 5 < 10) #true
print(10 > 5 and 5 > 10) #false


print('')
print('*' * 25)
stock = input('Ingresa el numero de stock => ')
stock = int(stock)

print('El valor es =>',stock >= 100 and stock <= 1000)

print('*' * 25)
print('\n')

# or
print('OR')
print('*' * 25)
print('True or True =>',True or True) #true
print('True or False =>',True or False) #true
print('False or True =>',False or True) #true
print('False or False =>',False or False) #false
# para que retorne true por lo menos un valor debe ser true

print('')
print('*' * 25)
role = input('Digita el rol => ')
print("¿Entraste al sistema? =>",role == 'admin' or role == 'seller')


