# Ejercicio 8
# Solicitar el nombre al usuario
nombre = input("Ingrese su nombre: ")

# Solicitar la opción de formato
print("Elija una opción:")
print("1. Mostrar el nombre en MAYÚSCULAS")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la primera letra en mayúscula")
opcion = input("Ingrese 1, 2 o 3: ")

# Aplicar la transformación según la opción elegida
if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida. Por favor, elija 1, 2 o 3.")
