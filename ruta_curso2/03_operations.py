set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# unir los conjuntos
set_c = set_a.union(set_b)
print(set_c)

# otra manera de unir los conjuntos
print(set_a | set_b)

# nos da los valores er comun de los conjuntos
set_c = set_a.intersection(set_b)
print(set_c)

# otra manera de obtener los valores en comun de los conjuntos
print(set_a & set_b)

# se resta al primer conjunto el segundo conjunto
# se quitan los elementos de b en a
set_c = set_a.difference(set_b)
print(set_c)

# otra manera de hacar la diferencia entre los conjuntos
print(set_a - set_b)


# diferencia simetrica
# unir los conjuntos pero elimina los que son en comun de ambos conjuntos
set_c = set_a.symmetric_difference(set_b)
print(set_c)

# otra manera de hacer la diferencia simetrica
print(set_a ^ set_b)