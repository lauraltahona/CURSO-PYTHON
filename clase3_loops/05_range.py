# range

# permite crear una secuencia de numeros. puede ser util para for, pero no solo para eso

print("\nrange()")

nums = range(5) # range es un tipo de dato, NO CREA UNA LISTA
print(nums) # no se muestra como una lista pero ahí esta guardado el rango para cuando se vaya a utilizar, como en un print
print(type(nums))

# range(1er parametro es el inicio, por defecto es 0, 2do parametro hasta donde)
print("\n")
for num in range(10):
    print(num)
print("\n")

for num in range(5,10):
    print(num)
print("\n")

for num in range(0,10,2):
    print(num)
print("\n")

for num in range(10, 0, -1):
    print(num)
print("\n")

for num in range(-5,0,1):
    print(num)
print("\n")
# range no crea la lista en memoria, crea los numeros sobre la marcha, si son utilizados los crea, si no no

#CREAR UNA LISTA CON RANGE
nums = range(10)
lista = list(nums)
print(lista)
print(type(lista))
print("\n")

# forma sin range
contador = 0
while contador <= 5:
    print("Hacer cinco veces algo")
    contador += 1

# con range
for _ in range(5): print("hacer cinco veces algo") # el guion es para decir q no vamos a utilizar esa variable