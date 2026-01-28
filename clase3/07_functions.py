# funciones
# bloques de codigo reutilizables y parametrizables para hacer tareas especificas

""" Definición de una función

def nombre_de_la_funcion(par1, par2, ...):
   #docstring
   # cuerpo de la funcion
   return valor_de_retorno #opcional

"""
def saludar():
    print("Hola")
saludar()

# con parametros

def saludar_a(nombre): # parametro
    print(f"Hola {nombre}")
# reutilizable
saludar_a("Laura") # argumento
saludar_a("Juan")

# el parametro es lo que acepta la funcion
# el argumento es lo que se le pasa a la función

# con más parametros

def sumar(a,b):
    return a+b

result = sumar(2,3)
print(f"resultado de la suma: {result}")

#documentar las funciones con docstring
def restar(a,b):
    """
    Resta dos numeros y devuelve el resultado
    """
    return a - b

print(f"resultado de la resta: {restar(5,4)}")
print(restar.__doc__)

#parametro por defecto

def multiplicar(a, b=2):
    return a * b

print(f"resultado de multiplicacion: {multiplicar(3)}")
print(f"resultado de multiplicacion: {multiplicar(3,4)}") # si no se pasa el parametro por defecto es 2, pero si se pasa, si cambia

# ARGUMENTOS POR CLAVE

def describir_persona(nombre,edad,sexo):
    print(f"\nsoy {nombre}, tengo {edad} años y me identifico como {sexo}")

#parametros posicionales
describir_persona("Laura", 21, "femenina")
describir_persona(21, "laura", "femenina") 

# argumentos por clave

describir_persona(sexo="masculino", nombre="Juan", edad=22) # aqui no importa el orden porque ya le especificas que parametro estas usando

# argumentos de longitud de variable (*args)
def sumar_numeros(*args): # argumentos de forma iterable, no se sabe cuantos argumentos van a haber
    suma=0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(1,2,3,4,5))
print(sumar_numeros(1,2))
print(sumar_numeros(1,2,5,4,6,7,8,9))

# argumentos de clave-valor variable (**kwargs) 
"""
    Sirven para que una función reciba muchos parámetros con nombre,
    sin saber de antemano cuántos van a llegar.
"""
def mostrar_datos(**kwargs):
    print(kwargs)

mostrar_datos(nombre="Lau", edad=21, carrera="Ingeniería") # lo que paso con el formato clave=valor entra a kwargs

print("\n")

def mostrar_datos(**kwargs):
    print("Nombre:", kwargs["nombre"]) #pero falla si no llega la clave llamada nombre
    print("Edad:", kwargs["edad"])

mostrar_datos(nombre="Lau", edad=21)
mostrar_datos(nombre="Juan", edad=21)

print("\n")

def mostrar_información_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}") #No le importa cuáles claves lleguen, no falla por claves faltantes, muestra todo lo que llegue

mostrar_información_de(nombre="Lau", edad=21, carrera="Ingeniería")
mostrar_información_de(nombre="Lau", edad=21, country="Colombia")
