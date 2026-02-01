#pueden contener elementos de diferentes tipos

print("crear listas")
lista1 = [1, 2, 3, 4] #enteros
lista2 = ["manzana", "pera", "banano"]
lista3: list[int | str | float | bool] = [1, "hola", 3.14, True] #opcional lo del principio
lista_vacia = []
matriz = [[1, 2], ["calcetin", 2]] # lista de listas 

#acceso a elementos por indice
print(lista1[0])
print(lista2[1])
print(lista2[-1]) # esto nos devuelve el ultimo q seria banano
print(lista2[-2]) # pera

print(matriz[1][0]) #seria la fila 1 (segunda) en la posicion 0: 

#slicing (rebanado) de listas
        
lista1 = [1, 2, 3, 4]

# lista[desde:hasta]
print(lista1[1:3]) # quiero que la lista1 vaya desde el indice 1 hasta el tope que es el 3 pero la posicion 3 NO la incorpora
print(lista1[:3]) # quiero todos los numeros hasta el indice 3
print(lista1[2:]) # desde el indice 2 hasta el final
print(lista1[:]) # hace copia de la lista 

# lista[desde:hasta:paso], si no le decimos el paso, va a ser de uno en uno

lista5 = [1,2,3,4,5,6,7,8]
print(lista5[::2]) #[1, 3, 5, 7] va de dos en dos
print(lista5[::-1]) #para devolver indices inversos(descendente)


# MODIFICAR UNA LISTA

lista1 = [1, 2,3]
lista1 += [5,6,7]
print(lista1)