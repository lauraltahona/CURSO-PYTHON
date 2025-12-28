  # para saber que tipo es algo usamos type()
#numeros
print(type(42))            # int -> integer -> número entero
print(type(3.14))          # float -> número decimal      
print(type(1e3))        # float -> notación científica (1 por 10^3)
#los numeros complejos se representan con una j al final
print(type(2 + 3j))       # complex -> número complejo

#cadenas de texto
print(type("Hola Mundo"))  # str -> string -> cadena de texto
print(type('Hola Mundo'))  # str -> string -> cadena de texto
print(type("""
Multilinea 
"""));

#booleanos
print(type(True))         # bool -> booleano -> True o False
print(type(False))        # bool -> booleano -> True o False
print(type(1 > 2));  # bool -> booleano -> True o False

#ausencia de valor "NoneType"
print(type(None))        # NoneType -> ausencia de valor