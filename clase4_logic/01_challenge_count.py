"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. 
En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la 
letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""

# text = "RRRRJJJjjjrr"

text = "fhgugugugugu"
contador_j = 0
contador_r = 0

def checked_is_balanced(text):
    text = text.upper()

    contador_j = text.count("J")
    print(f"Contador de J: {contador_j}")

    contador_r = text.count("R")
    print(f"Contador de R: {contador_r}")


    # if contador_j == contador_r:
    #     print("la alianza entre la mente y el fuego está en equilibrio")
    #     return True
    # else:
    #     return False

    return contador_j == contador_r



hay_equilibrio = checked_is_balanced(text)
print(f"¿Hay equilibrio para enfrentar el desafío?: {hay_equilibrio}")

print("\n")
# como lo estaba haciendo antes de recordar count

"""Toda variable que se modifica dentro de una función debe inicializarse dentro de esa función, 
   a menos que uses global (que casi nunca es buena idea).
"""

text = "HFHDHSHSj"
def checked_is_balanced2(text):

    contador_r=0
    contador_j=0
    text = text.upper()

    for letra in text:
        if letra == "J":
            contador_j += 1
            print(f"contador de J: {contador_j}")
        elif letra == 'R':
            contador_r += 1
            print(f"contador de R: {contador_r}")
        else:
            continue;

    if contador_j == contador_r:
        print("la alianza entre la mente y el fuego está en equilibrio")
        return True
    else:
        return False


hay_equilibrio = checked_is_balanced2(text)
print(f"¿Hay equilibrio para enfrentar el desafío?: {hay_equilibrio}")