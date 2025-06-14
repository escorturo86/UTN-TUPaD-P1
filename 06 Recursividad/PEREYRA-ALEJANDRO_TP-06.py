#Trabajo practico de recursividad
#Alumno: ALejandro Pereyra

#Función Factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

#Función Serie de Fibonacci hasta una posición
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#Función Potencia (base^exponente)
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

#Función Conversión de decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)


#Llamamos a las funciones desde el programa principal

#Factorial de los números entre 1 y el indicado por el usuario
limite = int(input("Ingrese un número para calcular los factoriales desde 1 hasta ese número: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

#Serie de Fibonacci hasta la posición indicada por el usuario
posicion = int(input("Ingrese hasta qué posición desea mostrar la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(posicion + 1):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

#Potencia recursiva (base y exponente ingresados por el usuario)
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

#Conversión de número decimal a binario (ingresado por el usuario)
numero = int(input("Ingrese un número decimal para convertir a binario: "))
if numero == 0:
    print("0")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")
