import os
os.system("clear") 


print("\nSentencia simple condicional");

edad = 18

#se ponen dos puntos simulando un "entonces"
if edad >= 18:
    #python en vez de llaves, funciona a través de tabulaciones
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#------------------------------------------
#elif

nota = 7

if nota >= 9:
    print("sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >=5:
    print("aprobado")
else:
    print("no fue suficiente para aprobar")

#----------------------------------------
print("condiciones multiples")
edad = 25
tiene_Carnet= True

#en js es && ||, en python se escribe como and, or
if edad >= 18 and tiene_Carnet:
    print("Puedes conducir")
else:
    print("POLICIA!!!!!!")


#en js es !, en python es not

es_fin_de_semana = False
if not es_fin_de_semana:
    print("hay que trabajar")

#--------------------------------------------
print("Anidar condiciones") #mejor evitar

edad = 28
tiene_dinero = True
if edad >= 18:
   if tiene_dinero:
       print("puedes ir a la discoteca")
   else:
       print("Quedate en casa")
else:
    print("No puedes entrar a la disco")

#simplificar siempre q se pueda

if edad < 18:
    print("No puedes entrar a la disco")
elif tiene_dinero:
    print("puedes ir a la discoteca")
else:
    print("Quedate en casa")

#-------------------------------
print("-----------------------------")
print("\nLa condición terniaria")
#[codigo si cumple la condicion] if [condicion] else [codigo si no cumple]
edad = 17
mensaje = "Es mayor de edad" if edad > 18 else "Es menor de edad"
print(mensaje)