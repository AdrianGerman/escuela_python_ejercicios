# Para resolver este desafío, tu reto es usar la función filter 
# de Python y una función lambda para filtrar una lista de palabras, 
# retornando una lista solo con las que cumplan con la condición de tener 4 o más letras.

def filter_by_length(words):
   # Escribe tu solución 👇
   return list(filter(lambda i: len(i) >= 4, words))

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)