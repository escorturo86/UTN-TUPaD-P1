# Ejercicio 2
# Solicita un número al usuario
numero = int(input("Ingresá un número entero: "))

# Se usa el valor absoluto para ignorar el signo
temporal = abs(numero)
cantidad_digitos = 0

# Si el número es 0, tiene un dígito
if temporal == 0:
    cantidad_digitos = 1
else:
    # Se cuentan los dígitos dividiendo por 10 hasta que quede 0
    while temporal > 0:
        cantidad_digitos = cantidad_digitos + 1
        temporal = temporal // 10

print("Cantidad de dígitos:", cantidad_digitos)
