# Ejercicio 10
# Pide un número
numero = int(input("Ingresá un número: "))
numero = abs(numero)  # Se toma solo la parte positiva
invertido = 0

# Invierte los dígitos uno a uno
while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

print("Número invertido:", invertido)
