set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

# buscamos en nuestro conjunto de "set_countries" si existe la palabra que proporcionamos
print('col' in set_countries)
print('pe' in set_countries)

# add
set_countries.add('pe')
print(set_countries)

# update
set_countries.update({'ar', 'ecu', 'pe'})
print(set_countries)

# remove
set_countries.remove('ar')
print(set_countries)

# discard no error si no encuentra la key "arg" hecho que si sucederia en la propiedad "remove"
set_countries.discard('arg')
print(set_countries)

set_countries.add('arg')
print(set_countries)

# eliminamos todo el conjunto
set_countries.clear()
print(set_countries)
print(len(set_countries))



