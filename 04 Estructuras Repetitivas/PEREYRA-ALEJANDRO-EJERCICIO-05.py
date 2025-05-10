# Ejercicio 5
import random

# Se elige un número al azar entre 0 y 9
SECRETO = random.randint(0, 9)

# Primer intento del usuario
intento = int(input("Adiviná el número entre 0 y 9: "))
intentos_realizados = 1

# Bucle que se repite hasta que adivine
while intento != SECRETO:
    intento = int(input("Incorrecto. Probá otra vez: "))
    intentos_realizados = intentos_realizados + 1

print("¡Correcto! Adivinaste en", intentos_realizados, "intentos.")
