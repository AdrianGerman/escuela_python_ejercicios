# función 1
def increment(x):
    return x + 1

# lambda de la primer función
increment_v2 = lambda x: x + 1

# función 2
def high_ord_func(x, func):
    return x + func(x)

# lambda de la segunda función
high_ord_func_v2 = lambda x, funct: x + funct(x)

result = high_ord_func(2, increment)
# 2 + (2 + 1)
print(f'resultado de las funciones => {result}')

result = high_ord_func_v2(2, increment_v2)
print(f'resultado de las lambdas => {result}')

# se declara la lambda directamente
result = high_ord_func_v2(2, lambda x: x + 2)
print(result)

# change
result = high_ord_func_v2(2, lambda x: x * 77)
print(result)