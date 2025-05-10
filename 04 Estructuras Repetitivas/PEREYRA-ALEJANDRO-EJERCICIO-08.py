# Ejercicio 8
CANTIDAD = 100
contador = 0
pares = 0
impares = 0
positivos = 0
negativos = 0

# Pide números y cuenta sus características
while contador < CANTIDAD:
    numero = int(input("Ingresá un número: "))

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1

    contador = contador + 1

# Muestra los resultados
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)
