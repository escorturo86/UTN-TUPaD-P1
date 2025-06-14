#Trabajo practico de recursividad
#Alumno: ALejandro Pereyra

# Ejercicio 1 - factorial()
# Pide un número al usuario y muestra el factorial de todos los enteros desde 1 hasta ese número.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Ejercicio 2 - mostrar_fibonacci()
# Pide al usuario una cantidad y muestra la serie de Fibonacci hasta esa cantidad de términos.
def mostrar_fibonacci():
    n = int(input("\n2) Ingrese la cantidad de términos de la serie Fibonacci: "))
    def fibonacci(x):
        if x <= 1:
            return x
        return fibonacci(x - 1) + fibonacci(x - 2)
    for i in range(n):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

# Ejercicio 3 - calcular_potencia_recursiva()
# Calcula base^exponente de forma recursiva y muestra el resultado.
def calcular_potencia_recursiva():
    base = int(input("\n3) Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    def potencia(b, e):
        if e == 0:
            return 1
        return b * potencia(b, e - 1)
    print(f"{base}^{exponente} = {potencia(base, exponente)}")

# Ejercicio 4 - convertir_a_binario()
# Convierte un número decimal a su equivalente binario utilizando recursividad.
def convertir_a_binario():
    n = int(input("\n4) Ingrese un número decimal para convertir a binario: "))
    def decimal_a_binario(x):
        if x == 0:
            return ""
        return decimal_a_binario(x // 2) + str(x % 2)
    binario = decimal_a_binario(n)
    print(f"{n} en binario es: {binario if binario else '0'}")

# Ejercicio 5 - verificar_palindromo()
# Verifica si una palabra ingresada es un palíndromo, sin usar funciones de inversión de cadena.
def verificar_palindromo():
    palabra = input("\n5) Ingrese una palabra (sin espacios ni tildes): ").lower()
    def es_palindromo(p):
        if len(p) <= 1:
            return True
        if p[0] != p[-1]:
            return False
        return es_palindromo(p[1:-1])
    print("¿Es palíndromo?", es_palindromo(palabra))

# Ejercicio 6 - sumar_digitos()
# Suma los dígitos de un número ingresado por el usuario sin convertirlo en cadena.
def sumar_digitos():
    n = int(input("\n6) Ingrese un número entero positivo para sumar sus dígitos: "))
    def suma_digitos(x):
        if x < 10:
            return x
        return (x % 10) + suma_digitos(x // 10)
    print(f"Suma de los dígitos: {suma_digitos(n)}")

# Ejercicio 7 - contar_bloques_piramide()
# Calcula cuántos bloques se necesitan para construir una pirámide de n niveles.
def contar_bloques_piramide():
    n = int(input("\n7) Ingrese la cantidad de bloques en el nivel más bajo: "))
    def contar_bloques(x):
        if x == 1:
            return 1
        return x + contar_bloques(x - 1)
    print(f"Total de bloques necesarios: {contar_bloques(n)}")

# Ejercicio 8 - contar_ocurrencias_digito()
# Cuenta cuántas veces aparece un dígito específico dentro de un número.
def contar_ocurrencias_digito():
    numero = int(input("\n8) Ingrese un número: "))
    digito = int(input("Ingrese un dígito a contar (0-9): "))
    def contar_digito(num, dig):
        if num == 0:
            return 0
        return (1 if num % 10 == dig else 0) + contar_digito(num // 10, dig)
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces")



#Llamamos a las funciones desde el programa principal

#Factorial de los números entre 1 y el indicado por el usuario
limite = int(input("Ingrese un número para calcular los factoriales desde 1 hasta ese número: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

mostrar_fibonacci()

calcular_potencia_recursiva()

convertir_a_binario()

verificar_palindromo()

sumar_digitos()

contar_bloques_piramide()

contar_ocurrencias_digito()