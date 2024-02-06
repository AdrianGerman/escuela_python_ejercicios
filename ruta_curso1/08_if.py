pet = input('¿Cuál es tu mascota favorita? => ')

if pet == 'perro':
    print('Genial, eso es muy bueno')
elif pet == 'gato':
    print('Espero tengas suerte')
elif pet == 'pez':
    print('Eres un tremendo genio')
else:
    print('Mascota bastante aburrida')
    

stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
    print('El stock es correcto')
else:
    print('El stock es incorrecto')