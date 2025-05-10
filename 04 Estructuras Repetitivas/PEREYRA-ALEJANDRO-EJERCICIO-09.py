# Ejercicio 9
CANTIDAD = 100
suma = 0
contador = 0

# Pide CANTIDAD de números y los suma
while contador < CANTIDAD:
    numero = int(input("Ingresá un número: "))
    suma = suma + numero
    contador = contador + 1

# Calcula la media
media = suma / CANTIDAD
print("La media es:", media)
