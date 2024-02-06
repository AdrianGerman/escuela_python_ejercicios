x = 3.3
print(f"Valor de x => {x}")
y = 1.1 + 2.2
print(f"Valor de y => {y}")

print(f"Comparacion => {x == y}") #false
# es falso ya que los decimales no coinciden

# primer metodo para ajustar la validación con los decimales
# str
print("")
print("Conviertiendo flotantes a str para poder compararlos")
# se convierte con format a str y se agregan solamenrte 2 decimales
y_str = format(y, ".2g")
print("str y => ", y_str)
print("float x =>", x)
# se convierte x a str para la comparación
print(f"Ambos valores en srt => {y_str == str(x)}") # true
print("¿Que valor es x? => ",type(x)) #float
# solo se convierte en la comparación pero no afecta el valor original

# segundo metodo para ajustar la validación con los decimales
# float
print("")
print("Se agrega una tolerancia de decimales para las validaciones")
print(f"Valor de y => {y} \nValor de x => {x}")

tolerance = 0.00001 # se asigna una tolerancia
print("Despues de agregar la tolerancia se comparan los 2 valores =>",abs(x - y) < tolerance)