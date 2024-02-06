print('Imprimiendo un True pero con un not =>',not True) #false
print('Imprimiendo un False pero con un not =>',not False) #True
print('')

# not (and)
print('NOT AND')
print('*' * 25)
print('NOT True and True =>', not (True and True)) #false
print('NOT True and False =>', not (True and False)) #true
print('NOT False and True =>', not (False and True)) #true
print('NOT False and False =>', not (False and False)) #true
# not te retorna el valor contrario de la operación, si originalmente 
# da true al poner un not te retornara false y viceversa

stock = input('Ingresa el numero de stock => ')
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))
# niega la operación dentro de los parentesis