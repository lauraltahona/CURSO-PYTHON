#transformar el tipo de un valor a otro tipo

print("conversion de tipos");
print(type(int("100")));
print(int(2.5)); #convierte el float a 2
print(round(2.8)); #en casos de .5 para abajo redondea al PAR mas cercano

print(2 + int("3")); #convierte el string "3" a entero y luego realiza la suma
print("100" + str(50)); #convierte el entero 50 a string y luego realiza la concatenacion

print(bool("")); #false porq es cadena de texto vacia
print(bool("Hola")); #true porq es cadena de texto no vacia
 