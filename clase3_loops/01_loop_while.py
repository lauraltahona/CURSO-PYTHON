#bucle while
print("\nBucle while:")
contador = 0
while contador < 5:
    print(contador)
    contador += 1 #para que no se vuelva un bucle infinito

# while True:
#     print("Hola") #bucle infinito
# se necesita una condición de salida, una condicion que eventualmente se cumplirá

#a menos que se use BREAK para romper el bucle

print("\nBucle while con break:")

contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break # a veces tiene sentido, no siempre

print("\n")
contador = 0
while contador <= 100: # ya tenemos un limite
    print(contador)
    contador += 1
    if contador % 5 == 0:
        print("Se encontró un multiplo de 5")
        break # pero si solo hay una cosa que nos interesa, se utiliza el break


# CONTINUE
# break es para romper el bucle
# pero continue es para saltar una iteracion en concreto y evitar que se procese esa iteracion
print("\nbucle con continue")
contador = 0
while contador <= 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print(f"número impar: {contador}")

#else, esta condicon cuando se ejecuta?
print("\nBucle while con else")
contador = 0
while contador < 5:
    contador += 1
else: # esta condicion else va a entrar cuando el bucle ha terminado
    print("El bucle ha terminado")

# que diferencia hay sin el else? para qué usarlo?
# el else no se ejecuta cuando  un break rompe el bucle
# se usa para asegurar que la condicion del while es falsa
#pero si utiliza un break, la condicion nunca pasa a ser falsa, por tanto no entra al else

#-----------------------------------------------------------------------------------------
# EJERCICIO PEDIR A UN USUARIO INFO DENTRO DE UN BUCLE

#pedirle al usuario un numero que tiene que ser positivo

print("\nEJERCICIO")
numero = -1
while numero < 0:
    try:
        numero = int(input("Ingresa un numero POSITIVO: "))
        if numero < 0:
            print("El número debe ser positivo. Intente otra vez")
    except:
        print("Lo q introduces debe ser un número")

print(f"El numero introducido es: {numero}")