
# Los diccionarios son colecciones de pares clave-valor
# sirven para almacenar datos relacionados

persona = {
    "nombre": "Juan",
    "edad": 21,
    "es_estudiante": True,
    "calificaciones": [5,5,4],
    "socials": {
        "twitter": "jperalta",
        "instagram": "jperaltafuentes",
    }
}

# acceder a valores
print(persona["nombre"])
print(persona["calificaciones"][2])
("\n")

# cambiar valores al acceder
persona["nombre"] = "Laura"
persona["calificaciones"][2] = 4.8
print(persona)
("\n")

# eliminar completamente una propiedad, no la devuelve
del persona["edad"]
print(persona)
("\n")

# eliminar y devolver
# le damos el nombre de la clave y nos devuelve su valor pero ELIMINA la propiedad
es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiante}")
print(persona)
("\n")

# sobreescribir un diccionario con otro diccionario
a = {"name": "Laura", "age": 21}
b = {"name": "Juan", "es_Estudiante": True}

a.update(b) # los datos de b "machacan" los datos de a
# pero a tiene una propiedad "age" que b no tiene, por tanto esa queda igual
# y se agrega la propiedad "es_estudiante" en a
print(a)
("\n")

print("es_Estudiante" in a)
("\n")


# obtener todas las claves
print("Keys")
print(persona.keys())
# obtener todos los valores
print("Values")
print(persona.values())
# obtener tanto clave como valor
print("Items")
print(persona.items())

for key, value in persona.items():
    print(f"{key}: {value}")