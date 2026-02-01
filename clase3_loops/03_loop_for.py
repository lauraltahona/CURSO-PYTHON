frutas = ["manzana", "pera", "mandarina"]
#iterar una lista
for fruta in frutas:
    print(fruta)
print("\n")
#iterar sobre cualquier cosa que sea iterable
cadena = "laura"
for caracter in cadena:
    print(caracter) # imprime l a u r a
print("\n")
# enumerate():  enumerar las propiedades que tiene la lista, en este caso son dos, el indice y el valor

frutas = ["manzana", "pera", "mandarina"]

#para enumerar los elementos de una lista primero devuelve el indice y despues el valor
for index, fruta in enumerate(frutas):
    print(f"el indice es {index} y la fruta es {fruta}")
print("\n")
# bucles anidados
letras = ['A', 'B', 'C']
numeros = [1, 2, 3]

for letra in letras: # itera A
    for numero in numeros: # itera cada numero hasta terminar (hasta el 3)
        print(f"{letra}{numero}")
# termina la primera iteracion de las letras y empieza la siguiente letra q es B
print("\n")
# BREAK
animales = ["perro", "gato", "leon", "raton", "loro", "pez", "canario"]

for animal in animales:
    print(animal)
    if animal == "loro":
        break; # imprime loro pero no continua con pez y canario

animales = ["perro", "gato", "leon", "raton", "loro", "pez", "canario"]
print("\n")

for idx, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"el loro esta escondido en el indice {idx}")
        break; # si el objetivo era encontrar el loro, ya para qué sigue buscando, sin el break sigue "buscando"

print("\n")

# CONTINUE

for id, animal in enumerate(animales):
    if animal == "loro":
        continue; # printar todos los animales pero si es un loro, continua, ignoralo 
        # que no siga ejecutando lo que esta en el for, si no que se salte a la siguiente iteración (pez)

    print(animal) 

print("\n")

# Comprensión de Listas (list comprehension)
animales = ["perro", "gato", "leon", "raton", "loro", "pez", "canario"]
# que cada uno de los elementos de la lista animales se transformen en mayusculas
animales_mayus = [animal.upper() for animal in animales] # comprension de listas
                 # lo q queremos hacer para cada animal o elemento
print(animales_mayus)
print("\n")

# con condicional
# el primer num solo devuelve el numero que cumple con la condicion
     #    ↓
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]

