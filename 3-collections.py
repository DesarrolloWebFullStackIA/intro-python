"""
--------------------------- COLECCIONES ---------------------------
En este taller aprenderás a manipular coleccciones de datos: Listas, diccionarios, tuplas y sets.
"""

"""
 --- LISTAS ---
Las listas son ordenadas y mutables.
Pueden contener elementos duplicados.
Puedes modificar, añadir y eliminar elementos.
"""
"""
--- Ejercicio 1 Listas ---
Crea una variable "mascotas" que almacene una lista con los siguientes elementos: 'perro', 'gato', 'loro'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
print(" ================== Mascotas/Listas ================== ")
# Escribe tu código aquí
mascotas = ["perro", "gato", "loro"]

# Escribe el código para saber la cantidad de elementos que tiene la lista, imprimir por consola
print("Longitud de la lista:", len(mascotas))

# Escribe el código para acceder al valor de la posición 2, imprimir por consola
print("Valor de la pos 2:", mascotas[1])

# Escribe el código para agregar una elemento a la lista, imprimir por consola la lista
mascotas.append("velociraptor")
print("Lista append:", mascotas)

# Escribe el código para modificar un elemento de la lista, imprimir por consola la lista
mascotas[1] = "T-rex"
print("Lista modificar:", mascotas)

# Escribe el código para eliminar un elemento de la lista, imprimir por consola la lista
mascotas.pop(3)
print("Lista pop:", mascotas)

"""
 --- TUPLAS ---
Las tuplas son ordenadas e inmutables.
Pueden contener elementos duplicados.
No puedes modificar, añadir o eliminar elementos después de la creación.
"""

"""
--- Ejercicio 2 Tuplas ---
Crea una variable "plantas" que almacene una tupla con los siguientes elementos: 'cactus', 'orquidea', 'rosas'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
# Escribe tu código aquí
print(" ================== Plantas/Tuplas ================== ")
plantas = ("cactus", "orquidea", "rosas")

# Escribe el código para saber la cantidad de elementos que tiene la tupla, imprimir por consola
print("Longitud de tupla:", len(plantas))
# Escribe el código para acceder al valor de la posición 2, imprimir por consola
print("Valor de la pos 2:", plantas[1])
# Intentar modificar una tupla
# plantas[1] = 'hoja rota'  # Descomenta esta línea para ver qué sucede
# TypeError: 'tuple' object does not support item assignment
# Escribe tu análisís acá acerca de qué sucede
# Como bien indica, la tupla no admite asignaciones nuevas a sus objetos

"""
 --- SETS ---
Los sets son desordenados y mutables.
No pueden contener elementos duplicados.
Puedes añadir y eliminar elementos, pero no puedes modificar los elementos existentes.
"""

"""
--- Ejercicio 3 Sets ---
Crea una variable "nombres" que almacene un set con los siguientes elementos: 'María', 'Cris', 'Cris', 'Alex'
Imprime por la terminal dicha variable
Haz los pasos pedidos
"""
print(" ================== Nombres/Sets ================== ")
# Escribe el código aqui
nombres = {'María', 'Cris', 'Cris', 'Alex'}
# Explica qué sucede cuándo imprimes el valor que almacena "nombres"
print("Set:", nombres)
# El resultado que nos da python es por culpa de que los SETS no admiten
# objetos repetidos, internamente python hashea los objetos y si dos son 
# iguales, eliminara las copias. A parte, tampoco son ordenadas, con distintas
# ejecuciones del programa pueden cambiar el orden de forma aleatoria

# Escribe el código para saber la cantidad de elementos que tiene el set, imprimir por consola
print("Longitud set:", len(nombres))

# Escribe el código para acceder al valor de la posición 3, imprimir por consola
try: # No funciona, ya que al no tener orden, no podemos sacar la posicion 3
    print("Set pos 3:", nombres[2])
except:
    print("TypeError: 'set' object is not subscriptable")

# Escribe el código para agregar una elemento al set, imprimir por consola el set
nombres.add("Julian")
print("Set:", nombres)

# Escribe el código para eliminar un elemento del set, imprimir por consola el set
nombres.remove("Alex")
print("Set:", nombres)
"""
 --- DICCIONARIOS ---
Los diccionarios son desordenados y mutables.
Contienen pares clave-valor.
Puedes añadir, modificar y eliminar pares clave-valor.
"""

"""
--- Ejercicio 4 Diccionarios ---
Crea un diccionario llamado "ciudad" con las claves 'nombre' y 'pais' y los valores 'Barcelona' y 'España' respectivamente.
Imprime el diccionario 
"""
print(" ================== Ciudades/Diccionario ================== ")
# Escribe el código aqui para acceder y ver por consola el valor de 'nombre'
ciudad = {
    "nombre": "Barcelona",
    "pais": "España"
}
print(ciudad)
# Escribe el código aqui para añadir un nuevo par clave-valor y ver por consola el valor de 'ciudad'
ciudad["habitantes"] = 3000000
print(ciudad)
# Escribe el código aqui para modificar el valor de un par clave-valor de 'ciudad' y verlo por consola
ciudad.update({"nombre": "Soria"})
print(ciudad)
# Escribe el código aqui para eliminar un par clave-valor de 'ciudad' y verlo por consola
ciudad.pop("pais")
print(ciudad)