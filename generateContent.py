import google.generativeai as genai
import os

# Asegúrate de configurar tu API KEY aquí
os.environ["GOOGLE_API_KEY"] = "AIzaSyBVaN7gQDhBrq8iYpkDS37ppzMhOaEIYiw"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Listar modelos disponibles
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"Nombre del modelo: {m.name}")