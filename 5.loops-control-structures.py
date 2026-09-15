"""
--------------------------- CICLOS Y ESTRUCTURAS DE CONTROL ---------------------------
En este taller aprenderás usar los métodos más típicos para dirigir el flujo de ejecuón y la lógica de un algoritmo
"""

"""
--- Ejercicio 1 condicionales  ---
Escribe un programa que pida al usuario una letra y luego imprima un mensaje indicando si es una vocal o una consonante.
"""
# Escribe tu código aquí
letra = input("Introduce una letra: ").lower()

if len(letra) == 1 and letra.isalpha():
    if letra in "aeiou":
        print(f"'{letra}' es una vocal.")
    else:
        print(f"'{letra}' es una consonante.")
else:
    print("Entrada no válida. Debes ingresar solo una letra.")

"""
--- Ejercicio 2  condicionales anidados  ---
Escribe un programa que pida al usuario una nota (entre 0 y 100) y determine si 
es una calificación de "A", "B", "C", "D" o "F".
"""
# Escribe tu código aquí
nota = float(input("Introduce una nota (entre 0 y 100): "))

if 0 <= nota <= 100:
    if nota >= 90:
        calificacion = "A"
    elif nota >= 80:
        calificacion = "B"
    elif nota >= 70:
        calificacion = "C"
    elif nota >= 50:
        calificacion = "D"
    else:
        calificacion = "F"
    print(f"Tu calificación es: {calificacion}")
else:
    print("Error: La nota debe estar en el rango de 0 a 100.")

"""
--- Ejercicio 3  bucle while  ---
Escribe un programa que pida al usuario un número entero positivo y 
luego imprima la cuenta regresiva desde ese número hasta 1.
"""
# Escribe tu código aquí
numero = int(input("Introduce un número entero positivo: "))

while numero >= 1:
    print(numero)
    numero -= 1

"""
--- Ejercicio 4  bucle for  ---
Escribe un programa que imprima todos los caracteres de una cadena de texto ingresada por el usuario.
"""
# Escribe tu código aquí
texto = input("Introduce un texto: ")

for caracter in texto:
    print(caracter)

"""
--- Ejercicio 5  bucle for con range ---
Escribe un programa que imprima la tabla de multiplicar del 5 (del 1 al 10).
"""
# Escribe tu código aquí
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

"""
--- Ejercicio 6  bucle for con listas ---
Escribe un programa que pida al usuario 5 palabras, las guarde en una lista y 
luego en una nueva lista guarde todas las palabras en mayúsculas.
"""
# Escribe tu código aquí
palabras = []
for i in range(5):
    palabra = input(f"Introduce la palabra {i + 1} de 5: ")
    palabras.append(palabra)

palabras_mayusculas = []
for palabra in palabras:
    palabras_mayusculas.append(palabra.upper())

print("Lista original:", palabras)
print("Lista en mayúsculas:", palabras_mayusculas)

"""
--- Ejercicio 7  break and continue ---
Escribe un programa que le pida al usuario una mascota y 
si es un perro, que imprima en la consola "Tengo un perro", 
si es un gato, que imprima en la consola "Tengo un gato", 
si es un pájaro, que imprima en la consola "Tengo un pájaro" y 
si no es ninguno de los 3 que imprima "No tengo una mascota convencional"
"""
# Escribe tu código aquí
while True:
    mascota = input("Introduce una mascota (o escribe 'salir' para terminar): ").lower().strip()

    if mascota == "salir":
        break
    elif mascota == "perro":
        print("Tengo un perro")
        break
    elif mascota == "gato":
        print("Tengo un gato")
        break
    elif mascota in ("pájaro", "pajaro"):
        print("Tengo un pájaro")
        break
    else:
        print("No tengo una mascota convencional")
        continue
