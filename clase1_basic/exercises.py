###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

nombre = "Laura"
ciudad = "Ciudad"
print(nombre);
print(ciudad);

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print("el tipo de a es: " + str(type(a)));
print("el tipo de b es: "+ str(type(b)));
print("el  tipo de c es: "+ str(type(c)));
print("el tipo de d es: " + str(type(d)));
print("el tipo de e es: " + str(type(e)));

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")


numero = "12345"
entero = int(numero);
flotante = float(numero);

print(f"el numero 12345 como entero es {entero} y como flotante es {flotante}");

numero2 = 3.99
entero2 = int(numero2);

print(f"el numero 3.99 como entero es {entero2}");

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

nombre = "Laura"
edad = 20
altura = 1.67
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros.");

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

#sin asignar variable
resultado = int(round(3.14160) / 2);
print("Valor de PI: 3.1416");
print("Redondeo de pi: ", round(3.1416));
print("resultado de PI / 2: ", resultado);

# PI = 3.1416
# PI_ROUND = round(PI);
# division = int(PI_ROUND / 2)

# print(f"redondeo de PI: {PI_ROUND}");
# print(f"resultado de la division entre 2: {division}")