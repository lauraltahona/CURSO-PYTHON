
lista = [1, 2, 3, 4, 5]

# AÑADIR O INSERTAR

lista.append(6) # añade un elemento al final de la lista
print(lista)

lista.insert(1, 1.5) # inserta un elemento en la posicion que le indiquemos en el primer argumento
print(lista)

lista.extend([5,6,7,8]) #agrega varios elementos al final de la lista
print(lista)

# ELIMINAR

lista.remove(1) # elimina el primer '1' que encuentre, si hay varios '1' no los va a borrar todos, solo el primero q aparezca
print(lista)

ultimo_borrado = lista.pop() #elimina el ultimo elemento de la lista y ademas te lo devuelve, asi que se puede guardar
print(f"la lista quedo: {lista}")
print(f"elemento elimninado: {ultimo_borrado}")

lista.pop(1) # eliimin< el segundo elemento de la lista o el indice que le pases
print(lista)

del lista[-1]
print(lista)

lista.clear() # elimina todos los de la lista
print(lista)

# elimina un rango de elementos
lista = ['a', 'b', 'c', 'd', 'e']
del lista[1:3]
print(lista)

# ORDENAR

numbers = [50,70,3,4,8,100,1]
numbers.sort() # modifica la lista original, no devuelve nada
print(numbers)

sorted_numbers = sorted(numbers) #ordena la lista creando una copia de la original, por tanto si la devuelve
print(sorted_numbers)

#cadena de texto minusculas
cadenas = ['manzana', 'pera', 'limón', 'manzana']
sorted_cadenas = sorted(cadenas)
print(sorted_cadenas)

#cadenas con mayusuclas
frutas = ['Manzana', 'pera', 'Limón', 'manzana']

frutas.sort(key=str.lower) # compara las cadenas transformadas con el lowerCase

# MAS METODOS
 
animals = ['león', 'gato', 'perro']
print(len(animals)) # devuelve el tamaño de la lista: 3

print(animals.count('león')) #cuantas veces aparece leon en la lista

print('gato' in animals) # comprueba si esta 'gato' en la lista -> True

