# Ejercicio 3
# Solicita los dos valores
inicio = int(input("Ingresá el primer número: "))
fin = int(input("Ingresá el segundo número: "))

# Se ordenan si están al revés
if inicio > fin:
    temp = inicio
    inicio = fin
    fin = temp

suma = 0
numero = inicio + 1

# Se suman todos los valores entre inicio y fin (excluidos)
while numero < fin:
    suma = suma + numero
    numero = numero + 1

print("La suma es:", suma)
