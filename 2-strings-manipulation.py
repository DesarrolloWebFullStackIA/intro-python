"""
--------------------------- MANIPULACIÓN DE STRINGS ---------------------------
En este taller aprenderás cómo crear manipular cadenas de texto y cómo manejar entradas de datos del usuario.
"""

"""
--- Ejercicio 1 ---
Crea una variable llamada "hobbie". 
Asígnale como valor una string con uno de tus hobbies". 
Crea otra variable llamada "name"
Asígnale como valor una string con tu nombre". 
Crea otra variable llamada "teammate"
Asígnale como valor una string con el nombre de una compañera". 
Crea una variable llamada "teammate-hobbie". 
Asígnale como valor una string con unos de sus hobbies". 
"""
# Escribe tu código aquí
print("================= EJERCICIO 1 =====================")
hobbie = "jugar videojuegos"
name = "Adrian"
teammate = "Sara"
teammate_hobbie = "dibujar"

"""
--- Ejercicio 2 Concatenación ---
Imprime por consola el siguiente mensaje concatenando las variales anteriormente declaradas:
"Soy [name] y en mis tiempos libres me gusta [hobbie]"
"""
# Escribe tu código aquí
print("================= EJERCICIO 2 =====================")
print("Soy " + name + " y en mis tiempos libres me gusta " + hobbie)

"""
--- Ejercicio 3 f-strings ---
Imprime por consola el siguiente mensaje usando f-strings para unir las frases de las variales anteriormente declaradas:
"Ella es [teammate] y en sus tiempos libres le gusta [teammate-hobbie]"
"""
# Escribe tu código aquí
print("================= EJERCICIO 3 =====================")
print(f"Ella es {teammate} y en sus tiempos libres le gusta {teammate_hobbie}")
"""
--- Ejercicio 4 separación por comas ---
Imprime por consola el siguiente mensaje usando separación por comas para unir las frases de las variales anteriormente declaradas:
"Ella se llama [teammate] y yo me llamo [name]"
"""
# Escribe tu código aquí
print("================= EJERCICIO 4 =====================")
print("Ella se llama", teammate, "y yo me llamo", name)

"""
--- Ejercicio 5 separación con operador % ---
Imprime por consola el siguiente mensaje usando separación con el operador % para unir las frases de las variables anteriormente declaradas:
"Además de programar, nos gusta [hobbie] y [teammate-hobbie]"
"""
# Escribe tu código aquí
print("================= EJERCICIO 5 =====================")
print("Además de programar, nos gusta %s y %s" % (hobbie, teammate_hobbie)) # %s = string, %d = entero, %f = float
"""
--- Ejercicio 6 input data ---
Escribe dos variables que reciban por terminal un número cada una
"""
# Escribe tu código aquí
print("================= EJERCICIO 6 =====================")
var1 = input("Introduce un número para var1: ")
var2 = input("Introduce un número para var2: ")

"""
--- Ejercicio 7 ---
Imprime por consola el resultado de la suma de los dos número obtenidos anteriormente y 
en un comentario de línea escribe lo que sucede. ¡Recuerda que puedes usar type() para indagar mas!
"""
# Escribe tu código aquí
print("================= EJERCICIO 7 =====================")
print("La suma de var1 y var2 es:", var1 + var2)
# Escribe tu análisis aquí
# Hemos introducido 2 variables por consola, pero python de forma predeterminada los
# los trata como strings, para ello deben ser transformados en int o float (mejor este
# último por mayor seguridad y no perder decimales) y validar con un try/catch en caso
# de que no se puedan transformar
"""
--- Ejercicio 6 conversión de strings ---
Transforma los valores recibidos en el ejercicio 6 a números
Imprime por consola el resultado de la suma de los dos número obtenidos anteriormente
"""
# Escribe tu código aquí
print("================= EJERCICIO 8 =====================")
y = True
while y == True:
  var1 = input("Introduce un número para var1: ")
  var2 = input("Introduce un número para var2: ")
  try:
    var1 = float(var1);
    var2 = float(var2);
    y = False
  except:
    print("Debes escribir un número")

print("La suma de var1 y var2 es:", var1 + var2)