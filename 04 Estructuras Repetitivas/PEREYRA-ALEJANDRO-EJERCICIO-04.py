# Ejercicio 4
suma = 0

# Pide el primer número
numero = int(input("Ingresá un número (0 para salir): "))

# Suma mientras el número no sea 0
while numero != 0:
    suma = suma + numero
    numero = int(input("Ingresá otro número (0 para salir): "))

print("Suma total:", suma)
