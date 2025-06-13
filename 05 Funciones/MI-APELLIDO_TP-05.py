import math

# 1. Imprimir "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Saludar usuario
def saludar_usuario():
    nombre = input("Ingresá tu nombre: ")
    print(f"Hola {nombre}!")

# 3. Información personal
def informacion_personal():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4. Área y perímetro del círculo
def calcular_area_y_perimetro_circulo():
    radio = float(input("Ingresá el radio del círculo: "))
    area = math.pi * (radio ** 2)
    perimetro = 2 * math.pi * radio
    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")

# 5. Segundos a horas
def segundos_a_horas():
    segundos = int(input("Ingresá la cantidad de segundos: "))
    horas = segundos / 3600
    print(f"Equivale a {horas} horas")

# 6. Tabla de multiplicar
def tabla_multiplicar():
    numero = int(input("Ingresá un número: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones básicas
def operaciones_basicas():
    a = float(input("Ingresá el primer número: "))
    b = float(input("Ingresá el segundo número: "))
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

# 8. Calcular IMC
def calcular_imc():
    peso = float(input("Ingresá tu peso en kg: "))
    altura = float(input("Ingresá tu altura en metros: "))
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc:.2f}")

# 9. Celsius a Fahrenheit
def celsius_a_fahrenheit():
    celsius = float(input("Ingresá la temperatura en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivalen a {fahrenheit}°F")

# 10. Calcular promedio
def calcular_promedio():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    c = float(input("Tercer número: "))
    promedio = (a + b + c) / 3
    print(f"El promedio es: {promedio}")

# Programa principal
# Llamamos a las funciones
imprimir_hola_mundo()
saludar_usuario()
informacion_personal()
calcular_area_y_perimetro_circulo()
segundos_a_horas()
tabla_multiplicar()
operaciones_basicas()
calcular_imc()
celsius_a_fahrenheit()
calcular_promedio()
