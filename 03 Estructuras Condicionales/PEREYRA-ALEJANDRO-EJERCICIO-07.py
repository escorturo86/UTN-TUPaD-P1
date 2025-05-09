# Ejercicio 7
# Solicitamos una frase o palabra al usuario
texto = input("Ingrese una frase o palabra: ")

# Verificamos si termina en vocal (mayúscula o minúscula)
if texto[-1].lower() in 'aeiou':
    texto += "!"
    
# Imprimir el resultado
print("Resultado:", texto)