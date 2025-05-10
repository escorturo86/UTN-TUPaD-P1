Ejercicio 10
# Pedimos al usuario que ingrese el hemisferio
hemisferio = input("¿En qué hemisferio estás? (N para norte, S para sur): ").upper()

# Pedimos al usuario que ingrese el número del mes
mes = int(input("¿Qué número de mes es? (1 a 12): "))

# Pedimos el día del mes
dia = int(input("¿Qué día del mes es? (1 a 31): "))

# Ahora determinamos la estación
if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        estacion = "Invierno"
    else:
        estacion = "Verano"
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        estacion = "Primavera"
    else:
        estacion = "Otoño"
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        estacion = "Verano"
    else:
        estacion = "Invierno"
elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
    if hemisferio == "N":
        estacion = "Otoño"
    else:
        estacion = "Primavera"
else:
    estacion = "No se pudo determinar"

# Mostramos el resultado
print("La estación del año es:", estacion)