
# peticiones en python sin librerias externas o nativas (más manual)

# import urllib.request
# import json

# # python en este caso se maneja de manera secuencial pero asincrona, espera a que lleguen los datos

# api_posts = "https://jsonplaceholder.typicode.com/posts"

# try:
#     # abrir pero sin utilizar los datos
#     response = urllib.request.urlopen(api_posts)

#     # leer los datos
#     data = response.read()

#     # decodificar los datos

#     json_data = json.loads(data.decode('utf-8')) # tipo de decodificación y transformar en un json

#     print(json_data)  

#     # cerrar la respuesta para no dejar "la pagina" abierta
#     response.close()
# except urllib.error.URLError as e:
#     print(F"Error en la solucitud: {e}")


# con dependencia (requests)

from dotenv import load_dotenv
import os
load_dotenv()
import requests

print("GET:")

api_posts = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_posts)
# print(response.json())

response_json = response.json()
print(response_json[0])

#--------------------------------------------------------------
print("\nPOST:")

try:
    api_posts = "https://jsonplaceholder.typicode.com/posts"
    input = {
        "title": "Laura y Juan",
        "body": "Felices",
        "userId": 5
    }

    response = requests.post(api_posts, json=input)
    print(response.json())
    print(response.status_code)

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

#----------------------------------------

print("\nPUT:")

try:

    response = requests.put("https://jsonplaceholder.typicode.com/posts/1", 
        json={
        "title": "Laura y Juan",
        "body": "Felices",
        "userId": 1
    })
    print(response.json())
    print(response.status_code)

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

# -------------------------------------

print("\nPATCH:")

try:

    response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", 
        json={
        "body": "Felices",
    })
    print(response.json())
    print(response.status_code)

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")


# USAR LA API DE OPEN AI

# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# print("\nAPI DE OPEN AI")
# def call_openai_gpt(api_key, prompt):
#     url = "https://api.openai.com/v1/responses"

#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {api_key}"
#     }

#     data = {
#         "model": "gpt-4o-mini", 
#         "input": prompt
#     }

#     response = requests.post(url, json=data, headers=headers)
#     print(response.json())

# call_openai_gpt(OPENAI_API_KEY, "Escribe un poema sobre la programación")


# API DE GROK 

# print("\nAPI DE GROK")

# GROK_API_KEY = os.environ.get('GROK_API_KEY')

# def call_grok(api_key, prompt):
#     url = "https://api.x.ai/v1/chat/completions"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {api_key}"
#     }

#     data = {
#         "model": "grok-4-latest",
#         "messages": [{"role": "user", "content": prompt}]
#     }

#     response = requests.post(url, json=data, headers=headers)
#     print(response.json())


# call_grok(GROK_API_KEY, "Hazme un poema sobre la programación")

# API DE GROQ
import json
print("\nAPI DE GROQ")

GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

def call_groq(api_key, prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()


api_response = call_groq(GROQ_API_KEY, "Hazme un poema corto sobre la programación")
print(json.dumps(api_response, indent=2)) # crear una cadena de texto a través del json con identación
print(api_response["choices"][0]["message"]["content"])


# CON LIBRERÍA DE OPEN AI (mucho mas fácil)

# from openai import OpenAI

# def call_openai_groq(prompt):
#     client = OpenAI(
#         api_key=os.environ.get('GROQ_API_KEY'), 
#         base_url="https://api.groq.com/openai/v1"
#     )

#     response = client.responses.create(
#         input=prompt,
#         model="openai/gpt-oss-20b",
#     )

#     print(response.output_text)

# call_openai_groq("Dame un poema corto para dedicar a mi pareja")