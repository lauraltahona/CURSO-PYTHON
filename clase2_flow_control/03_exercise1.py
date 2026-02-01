###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# numero = input("Ingrese un numero \n")
# numero2 = input("Ingrese otro número\n")

# if numero > numero2:
#     print(f"El mayor es: {numero}")
# elif numero2 > numero:
#     print(f"El mayor es: {numero2}")
# else:
#     print("Los números son iguales")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# a = int(input("Ingrese un numero \n"))
# b = int(input("Ingrese otro número\n"))

# suma = a + b
# print("Suma: ", suma)
# print("Resta: ", a - b)
# print("Multiplicacion: ", a * b)
# if a > 0 and b > 0:
#     print("Division: ", a / b)
# else:
#     print("No se puede realizar la división porq un digito es cero")

#forma pidiendo la operacion:

# num1 = float(input("Introduce el primer número: "))
# num2 = float(input("Introduce el segundo número: "))
# operacion = input("Introduce la operación (+, -, *, /): ")

# if operacion == "+":
#     resultado = num1 + num2
# elif operacion == "-":
#     resultado = num1 - num2
# elif operacion == "*":
#     resultado = num1 * num2
# elif operacion == "/":
#     if num2 == 0:
#         print("Error: No se puede dividir por cero.")
#     else:
#         resultado = num1 / num2
# else:
#     print("Operación no válida.")

# if 'resultado' in locals(): 
#     print(f"El resultado es: {resultado}")


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# anio = int(input("Introduzca un año por favor: "))

# if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
#     print("Es año bisiesto")
# else:
#     print("No es año bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Introduzca una edad por favor: "))

if 0 <= edad <= 2:
    print("Bebé")
elif 3 <= edad <= 12:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 64:
    print("Adulto")
elif edad >= 65: 
    print ("Adulto mayor")
else:
    print("Edad no válida")