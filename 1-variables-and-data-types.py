"""
--------------------------- VARIABLES / TIPOS DE DATOS ---------------------------
En este taller aprenderás cómo crear variables, trabajar con diferentes tipos de datos.
"""

"""
--- Ejercicio 1 Variables---
Crea una variable llamada "mensaje". 
Asígnale el valor "¡Hola, Mundo!". 
Imprime el valor de la variable en la consola.
"""
mensaje = "¡Hola, Mundo!"
print(mensaje)

"""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""
mensaje = "Hello world!"
print(mensaje)
# La variable mensaje se sobreescribe con el nuevo dato proporcionado

"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""
cadena = "Hola"
print(cadena)
entero = 12
print(entero)
decimal = 0.33
print(decimal)
booleano = True
print(booleano)
lista = ["Hola", "Adios", "Bien"] 
print(lista)
tupla = (44, 22, 33) # A tuple is a collection which is ordered and unchangeable but allow copies.
print(tupla)
diccionario = { # A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} # As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
print(diccionario)
serie = {"Platano", "Manazana", "Kiwi"} # A set is a collection which is unordered, unchangeable*, and unindexed.
print(serie) # * Note: Set items are unchangeable, but you can remove items and add new items.
