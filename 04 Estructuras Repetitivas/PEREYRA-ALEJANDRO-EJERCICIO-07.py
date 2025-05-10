# Ejercicio 7
# Pide un número positivo
fin = int(input("Ingresá un número positivo: "))
suma = 0
numero = 0

# Bucle suma todos los números desde 0 hasta fin
while numero <= fin:
    suma = suma + numero
    numero = numero + 1

print("La suma es:", suma)
