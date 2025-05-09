# Ejercicio 5
# Solicitamos la contraseña al usuario
contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

# Verificamos la longitud usando len()
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")