# Ejercicio 4
# Solicitamos la edad al usuario
edad = int(input("Por favor, ingresa tu edad: "))

# Verificamos y mostramos la categoría correspondiente
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
