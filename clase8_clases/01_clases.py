
# Las clases son plantillas para crear un objeto
# un objeto es una instancia de una clase
# la clase es una plantilla o un molde y que al utilizar el molde sale el objeto
# cada vez que utilizamos ese molde sale un objeto 


class Coche:
    tipo = "Vehiculo de cuatro ruedas" # este tipo todos lo van a tener igual

    # método especial que es el que construye el objeto
    # se llama automaticamente este método cuando creas la instancia
    # como el constructor

    def __init__(self, marca, modelo, color): # el self se refiere a si mismo
        # pero estos atributos de la instancia que se ponen aqui es porque cada coche 
        # lo va a tener diferente
        self.marca = marca,
        self.modelo = modelo,
        self.color = color
    
    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} arrancó!🚗")



mi_coche = Coche("Toyota", "Corolla", "rojo")
mi_coche.arrancar()
print(mi_coche.tipo)
print("\n")
otro_coche = Coche("Nissan", "4X4", "blanco")
otro_coche.arrancar( )
print(otro_coche.tipo)


# encapsulacion: es ocultar los detalles internos de una clase y exponer solo la interfaz pública
# desde fuera tu no sabes como arranca, no hay acceso a lo que hay por dentro de "arrancar"

# Crear una clase para llamar a la AI de OpenAI, Groq  o lo que sea
import requests
import os
from dotenv import load_dotenv
load_dotenv()


class AI_API:
    def __init__(self, api_key, url, model):
        self.api_key = api_key
        self.url = url
        self.model = model

    def call_AI(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            response = requests.post(self.url, json=data, headers=headers)
            res_json = response.json()
            print(res_json["choices"][0]["message"]["content"])
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return None



groq_ai = AI_API(os.environ.get('GROQ_API_KEY'), "https://api.groq.com/openai/v1/chat/completions", "llama-3.3-70b-versatile")
print("\nAPI DE GROQ :D")

# Una clase que encapsula la lógica, no sabemos que se hace dentro, solo que si llamamos a la api, nos da la respuesta
groq_ai.call_AI("Dame un poema corto para dedicar")

