items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'shorts',
        'price': 200
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

# se modifica la lista para agregar el nuevo campo de 'taxes'
def add_taxes(item):
    # para no modificar la lista original, se hace una copia de los datos de la lista original a 
    # new_item y ahora se trabaja sobre ella
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_items = list(map(add_taxes, items))
print('new list')
print(new_items)
print('old list')
print(items)