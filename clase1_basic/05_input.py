nombre = input("Hola, ¿cuál es tu nombre? \n");
print(f"Hola {nombre}, encantado de conocerte.");
 
age = input("Cuántos años tienes?\n");
print(type(age));
# Todo lo que se recibe por input es de tipo string
# print(f"Dentro de 20 años tendrás {age + 20} años.")
print(f"Dentro de 20 años tendrás {int(age) + 20} años.");
#age = int(input("¿Cuántos años tienes?"))

#multiples valores a la vez
country, city = input("En qué país y ciudad vives?\n").split() #por defecto va a separar por espacios o puede ser .split(",")
print(f"Vives en {city}, que está en {country}. Que lindo lugar!");