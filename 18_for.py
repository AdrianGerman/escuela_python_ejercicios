my_list = [23, 54, 76, 98, 90]
for element in my_list:
    print(element)
    
my_tuple = ('adrian', 'german', 'goriago')
for element in my_tuple:
    print(element)
    
    
product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 77
}

print('')


for key in product:
    print(key, '=>',product[key])
    
print('')

for key, value in product.items():
    print(key, '=>',value)
    
    
print('')    

people = [
    {
        'name': 'Adrian',
        'age': 22
    },
    {
        'name': 'Jack',
        'age': 19
    },
    {
        'name': 'John',
        'age': 45
    }
]

for person in people:
    print('name =>', person['name'])