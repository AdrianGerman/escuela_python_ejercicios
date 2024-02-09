# creación de listas 
numbers = [1, 2, 3, 4]
numbers_v2 = []

# llenamos la lista de numbers_v2 con los valores de la lista 
# original pero multiplicados * 2
for i in numbers:
    numbers_v2.append(i * 2)
    
print(numbers)
print(numbers_v2)

# hacemos lo mismo que numebers_v2 pero usando map y lambda
numbers_v3 = list(map(lambda i: i * 2, numbers))
print(numbers_v3)


print('')
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]
print(numbers_1)
print(numbers_2)

# suma de manera vertical los valores de las listas
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)
