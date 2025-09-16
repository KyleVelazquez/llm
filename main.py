import os
from openai import OpenAI

# Inicializar cliente con tu API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generar_texto(idea):
    """Genera un texto a partir de una idea."""
    prompt = f"Escribe un párrafo claro y coherente sobre el siguiente tema: {idea}"
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return respuesta.choices[0].message.content

def corregir_texto(texto):
    """Corrige gramática y estilo de un texto dado."""
    prompt = f"Corrige la gramática y mejora el estilo del siguiente texto, manteniendo el sentido original:\n\n{texto}"
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return respuesta.choices[0].message.content

def sugerir_continuacion(texto_inicial):
    """Sugiere cómo continuar un texto dado."""
    prompt = f"Continúa de forma coherente el siguiente texto:\n\n{texto_inicial}"
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return respuesta.choices[0].message.content

if __name__ == "__main__":
    print("=== Asistente de Escritura Automática ===")
    print("1. Generar texto a partir de una idea")
    print("2. Corregir gramática y estilo")
    print("3. Sugerir continuación de un texto")

    opcion = input("Elige una opción (1/2/3): ")

    if opcion == "1":
        idea = input("Escribe tu idea: ")
        print("\nTexto generado:\n", generar_texto(idea))
    elif opcion == "2":
        texto = input("Escribe el texto a corregir: ")
        print("\nTexto corregido:\n", corregir_texto(texto))
    elif opcion == "3":
        inicio = input("Escribe el inicio de tu texto: ")
        print("\nContinuación sugerida:\n", sugerir_continuacion(inicio))
    else:
        print("Opción no válida.")
