# Ejercicio 5
"""El programa realiza lo siguiente paso a paso:

Define una lista llamada numeros con los valores: [8, 15, 3, 22, 7].

Ejecuta la operación max(numeros):

La función max() encuentra el número más grande de la lista.

En este caso, el máximo es 22.

Elimina ese valor máximo con remove():

numeros.remove(22) elimina el primer 22 que encuentra en la lista.

La lista queda modificada como: [8, 15, 3, 7].

Imprime la lista resultante:

El print(numeros) muestra [8, 15, 3, 7]."""

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)