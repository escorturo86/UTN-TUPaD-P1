# TP N°7 Datos complejos
# Alumno: Alejandro Pereyra

# EJERCICIO 1
# Creamos un diccionario con precios iniciales de frutas
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Agregamos nuevas frutas con sus precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# EJERCICIO 2
# Actualizamos el precio de algunas frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# EJERCICIO 3
# Creamos una lista con solo los nombres de las frutas, sin precios
solo_frutas = []

# Recorremos el diccionario y agregamos las claves (nombres) a la lista
for fruta in precios_frutas:
    solo_frutas.append(fruta)

# Mostramos la lista
print("Lista de frutas:")
print(solo_frutas)

# EJERCICIO 4
# Creamos un diccionario vacío para almacenar la agenda telefónica
agenda = {}

# Pedimos al usuario que cargue 5 contactos
print("Cargue 5 contactos en la agenda:")
contador = 0
while contador < 5:
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    agenda[nombre] = numero
    contador = contador + 1

# Permitimos consultar un número ingresando un nombre
consulta = input("Ingrese el nombre de un contacto para consultar su número: ")

# Verificamos si el nombre está en la agenda
if consulta in agenda:
    print("El número es:", agenda[consulta])
else:
    print("El contacto no se encuentra en la agenda.")

# EJERCICIO 5
# Pedimos al usuario una frase
frase = input("Ingrese una frase: ")

# Pasamos la frase a minúsculas
frase = frase.lower()

# Dividimos la frase en palabras usando split
palabras = frase.split()

# Usamos un set para obtener las palabras únicas
palabras_unicas = set(palabras)

# Creamos un diccionario para contar la frecuencia de cada palabra
frecuencia = {}

# Recorremos la lista de palabras
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] = frecuencia[palabra] + 1
    else:
        frecuencia[palabra] = 1

# Mostramos las palabras únicas y la frecuencia
print("Palabras únicas:", palabras_unicas)
print("Frecuencia de cada palabra:", frecuencia)

# EJERCICIO 6
# Vamos a guardar los nombres y las notas de 3 alumnos
alumnos = {}

# Repetimos el ingreso de datos 3 veces
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    print("Ingrese 3 notas para", nombre)
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    # Guardamos las notas en una tupla
    notas = (nota1, nota2, nota3)
    # Guardamos la tupla en el diccionario
    alumnos[nombre] = notas

# Calculamos y mostramos el promedio de cada alumno
for alumno in alumnos:
    notas = alumnos[alumno]
    suma = notas[0] + notas[1] + notas[2]
    promedio = suma / 3
    print("El promedio de", alumno, "es", promedio)

# EJERCICIO 7
# Pedimos dos listas de estudiantes que aprobaron parciales y las convertimos en sets
print("Ingrese los IDs de los estudiantes que aprobaron el Parcial 1 (separados por espacio):")
entrada1 = input()
lista1 = entrada1.split()
parcial1 = set()

for id in lista1:
    parcial1.add(int(id))

print("Ingrese los IDs de los estudiantes que aprobaron el Parcial 2 (separados por espacio):")
entrada2 = input()
lista2 = entrada2.split()
parcial2 = set()

for id in lista2:
    parcial2.add(int(id))

# Mostramos resultados
ambos = parcial1.intersection(parcial2)
solo_uno = parcial1.symmetric_difference(parcial2)
al_menos_uno = parcial1.union(parcial2)

print("Estudiantes que aprobaron ambos parciales:", ambos)
print("Estudiantes que aprobaron solo uno:", solo_uno)
print("Estudiantes que aprobaron al menos uno:", al_menos_uno)

# EJERCICIO 8
# Creamos un diccionario con stock inicial
stock = {
    "Arroz": 10,
    "Fideos": 5
}

# Pedimos el nombre del producto
producto = input("Ingrese un producto para consultar o agregar al stock: ")

# Verificamos si ya existe
if producto in stock:
    print("El stock actual de", producto, "es", stock[producto])
    agregar = int(input("¿Cuántas unidades desea agregar?: "))
    stock[producto] = stock[producto] + agregar
else:
    nuevo_stock = int(input("Producto no registrado. ¿Cuántas unidades tiene?: "))
    stock[producto] = nuevo_stock

# Mostramos el stock actualizado
print("Stock actual:", stock)

# EJERCICIO 9
# Creamos una agenda de eventos donde la clave es una tupla (día, hora)
agenda_eventos = {
    ("Lunes", "10:00"): "Reunión",
    ("Martes", "14:00"): "Clase de Python"
}

# Pedimos día y hora al usuario
dia = input("Ingrese un día: ")
hora = input("Ingrese una hora (formato HH:MM): ")

# Buscamos en la agenda
clave = (dia, hora)

if clave in agenda_eventos:
    print("Actividad programada:", agenda_eventos[clave])
else:
    print("No hay actividad registrada para ese horario.")

# EJERCICIO 10
# Creamos un diccionario de países y capitales
paises = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Japón": "Tokio"
}

# Creamos un nuevo diccionario con las capitales como claves y los países como valores
capitales = {}

# Recorremos el diccionario original
for pais in paises:
    capital = paises[pais]
    capitales[capital] = pais

# Mostramos el nuevo diccionario
print("Diccionario invertido (capital -> país):", capitales)