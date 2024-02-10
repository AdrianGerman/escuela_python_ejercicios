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
    item['taxes'] = item['price'] * .19
    return item

new_items = list(map(add_taxes, items))
print(new_items)