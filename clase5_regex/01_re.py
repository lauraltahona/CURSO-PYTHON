"""
Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc.

¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente

"""
# 1. importar el modulo de expresiones regulares "re"
import re

# 2. Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola" # patrón
# 3. el texto donde queremos buscar
text = "Hola mundo" # texto
# 4. Usar la funcion de busqueda de "re". Donde está el patrón dentro del texto
result = re.search(pattern, text)

if result:
    print("Encontrado el patrón en el texto")
else:
    print("No he encontrado el patrón en el texto")

print("\n")
# .group() devuelve la cadena que coincide con el pattern
print(f"La cadena que coincide con el patrón: {result.group()}")

# .start() devolver la posición inicial de la coincidencia
print(f"La posición que coincide con el patrón: {result.start()}")

# .end() posición final de la coincidencia, donde estaba terminando # h o l a, a es de indice 4
print(f"La posicion final que coincide con el patrón: {result.end()}")

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.

print("\n")
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"

found_ia = re.search(pattern, text)
if found_ia:
    print(f"Se encontró la coincidencia. La posición inicial de la coincidencia: {found_ia.start()}. La posición final de la coincidencia: {found_ia.end()}")
else:
    print("No se encontró la coincidencia")

#--------------------------
# Encontrar todas las coincidencias de un patrón
# .findall() devuelve una lista con todas las coincidencias
print("\n")
text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.findall(pattern, text)
print(matches)

# No importa si el patron no es exactamente igual

print("\n")
text = "Me gusta Pyhhon. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Py.hon"
matches = re.findall(pattern, text)
print(f"Veces de coincidencias encontradas: {len(matches)}")

# iter() itera en los resultados y los devuelve, saber la informacion de los resultador para poder hacer .group(), .start() etc
print("\n")
text = "Me gusta Pyhhon. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Py.hon"
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())


print("\n")
# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
pattern = "midu"
matches = re.finditer(pattern, text)
matches_counter = re.findall(pattern,text)

print(f"coincidencias encontradaS: {len(matches_counter)}")
for match in matches:
    print(match.group())
    print(f"Posicion inicial: {match.start()}")
    print(f"Posicion inicial: {match.end()}")

### Modificadores

# Los modificadores son opciones que se pueden agregar a un patrón para cambiar su comportamiento

# re.IGNORECASE: Ignora las mayúsculas y minúsculas

print("\n")
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede " \
"cagar con las Regex para ir con cuidado, pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "IA"

found_ia = re.findall(pattern, text, re.IGNORECASE)
if found_ia:
    print(found_ia)
    print(f"cantidad de veces: {len(found_ia)}")
else:
    print("No se encontró la coincidencia")

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
pattern = "python"

found_python = re.findall(pattern, text, re.IGNORECASE)

if found_python:
    print(found_python)
else:
    print("No se encontraron coincidencias")


### Reemplazar el texto

# .sub() reemplaza todas las coincidencias de un patrón en un texto

text = "Hola, mundo! Hola de nuevo. Hola otra vez."
pattern = "Hola"
replacement = "Adiós"

new_text = re.sub(pattern, replacement, text) # count, numero de veces que se quiere reemplazar, por defecto es 0 que es todas las coinicdencias

print(new_text)