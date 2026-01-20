###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

numero = 10
contador = 0
while contador < 10:
    print(numero)
    numero -= 1
    contador += 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

numero = 0
suma_pares = 0
while numero <= 20:
    numero += 1
    if numero % 2 == 0:
        print(f"numero par: {numero}")
        suma_pares += numero
print(f"Suma de pares: {suma_pares}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

numero = int(input("Ingrese un numero entero positivo: "))
contador = 1
factorial = 1
while contador <= numero:
    factorial *= contador
    contador += 1

print(f"El factorial del numero es {factorial}")


#asi lo habia hecho yo

# numero = int(input("Ingrese un numero entero positivo: "))
# contador = 0 # da 720 porque hace una iteración más, ya que comienza desde el 0, hace 6 iteraciones cuando deben haber 5 iteraciones
               # me da el factorial de 6
# factorial = 1
# while contador <= numero: # 5 = 5: entra de nuevo al bucle
#     contador += 1 # pero aqui incrementa a 6 y multiplica lo q hay en factorial por 6, entonces el incremento es despues de multiplicar
#     factorial *= contador
# print(f"El factorial del numero es {factorial}")


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
# len permite saber la longitud de una cadena
valida = False
while valida == False:
    password = input("Digite su contraseña: ")
    if len(password) >= 8:
        print("Contraseña válida")
        valida = True
    else:
        print("Contraseña invalida")
        valida = False

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
numero = int(input("Digite un numero entero positivo: "))

multiplicado = 1

while multiplicado <= 10:
    print(f"{numero} * {multiplicado} = {numero * multiplicado}")
    multiplicado += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

n = int(input("Introduce un número entero positivo N: "))

numero = 2
while numero <= n:
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor += 1
  if es_primo:
    print(numero)

  numero += 1