# r+ agrega el nuevo contenido sin afectar el original, w+ sobrescribe el archivo original y
# unicamente queda el texto que nosotros escribimos
with open('ruta_curso2/text/text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('hola de nuevo\n')
    file.write('mi nombre es\n')
    file.write('san judas apostol\n') 
