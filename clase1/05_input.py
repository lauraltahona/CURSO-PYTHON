nombre = input("Hola, ¿cuál es tu nombre? \n");
print(f"Hola {nombre}, encantado de conocerte.");
 
age = input("Cuántos años tienes?\n");
print(type(age));
# Todo lo que se recibe por input es de tipo string
# print(f"Dentro de 20 años tendrás {age + 20} años.")
print(f"Dentro de 20 años tendrás {int(age) + 20} años.");

#age = int(input("¿Cuántos años tienes?"))