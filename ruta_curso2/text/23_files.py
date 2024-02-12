file = open("ruta_curso2/text/text.txt")
# lee todo el archivo
# print(file.read())

# lee solo una linea, cada uno es la siguierte linea
# print(file.readline())
# print(file.readline())
# print(file.readline())

# cierra el archivo 
# (auque no hace ningún cambio visual, el close se debe hacer siempre)
# file.close()


for line in file:
    print(line)

file.close()


with open('ruta_curso2/text/text.txt') as file:
    for line in file:
        print(line)



