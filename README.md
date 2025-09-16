# 📝 Asistente de Escritura Automática

Este proyecto utiliza la **API de OpenAI** para ayudar a los usuarios a escribir correos, artículos o cualquier tipo de texto.  
El asistente puede:
- Generar un texto a partir de una idea.
- Corregir gramática y estilo.
- Sugerir la continuación de un texto.

---

##  Instalación
1. Clona este repositorio:
   git clone <git@github.com:KyleVelazquez/llm.git>
   cd asistente_escritura
Crea un entorno virtual e instálalo:

python3 -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows
pip install -r requirements.txt

Configura tu API key de OpenAI:
export OPENAI_API_KEY="tu_api_key"   # En Linux/Mac
setx OPENAI_API_KEY "tu_api_key"     # En Windows

Ejecución
python main.py
Se mostrará un menú con 3 opciones:

Generar texto

Corregir texto

Sugerir continuación

👤 Autor
Kyle Velázquez

Curso: Inteligencia Artificial