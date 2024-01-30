# format
name = "Adrian"
last_name = "German"

#forma no.1
template = "Hola mi nombre es " + name + " y mi apellido es " + last_name
print('dato 1 =>', template)

#forma no.2
template = "Hola mi nombre es {} y mi apellido es {}".format(name, last_name)
print('dato 2 =>', template)


#forma no.3
template = f"Hola mi nombre es {name} y mi apellido es {last_name}"
print('dato 3 =>', template)