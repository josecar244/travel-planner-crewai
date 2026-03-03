# app.py - Nuestro Frontend de Chatbot de Viajes

import streamlit as st
import requests
import os

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Asistente de Viajes IA",
    page_icon="✈️",
    layout="centered"
)

# --- Definición del Endpoint del Backend ---
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8005/plan-trip")#"https://teknik-backend-crewai-itinerario-de-viajes.3q9yis.easypanel.host/plan-trip")#, 

# --- Título y Cabecera de la Aplicación ---
st.title("✈️ Asistente de Viajes IA")
st.markdown("""
Bienvenido a tu planificador de viajes personal. Describe el viaje de tus sueños y 
mi equipo de agentes de IA creará un itinerario personalizado para ti.

**Ejemplos de peticiones:**
- *"Un viaje de 10 días por la costa de Italia para una pareja, enfocado en comida y cultura."*
- *"Una aventura de 2 semanas en Costa Rica para amantes de la naturaleza con un presupuesto moderado."*
- *"¿Qué puedo hacer en 3 días en Nueva York con un presupuesto de $500?"*
""")

# --- Inicialización del Historial del Chat ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! ¿A dónde te gustaría viajar? Descríbeme tu viaje ideal."}
    ]

# --- Mostrar Mensajes Anteriores ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        # Si el mensaje del asistente tiene contenido descargable, muestra el botón
        if message.get("download_content"):
            st.download_button(
                label="📥 Descargar Itinerario (.md)",
                data=message["download_content"],
                file_name=message.get("download_filename", "itinerario.md"),
                mime="text/markdown",
            )

# --- Entrada de Usuario y Lógica de Comunicación ---
if prompt := st.chat_input("Describe el viaje de tus sueños..."):
    # Añadir y mostrar el mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Preparar y mostrar un mensaje de "pensando"
    with st.chat_message("assistant"):
        with st.spinner("Un momento, estoy consultando a mi equipo de expertos... Esto puede tardar unos minutos..."):
            try:
                # Enviar la petición al Backend
                response = requests.post(BACKEND_URL, json={"prompt": prompt}, timeout=600) # Timeout de 10 minutos
                response.raise_for_status()

                # Procesar la respuesta JSON estructurada
                result = response.json()
                chat_response = result.get("chat_response", "Lo siento, hubo un problema al generar la respuesta.")
                download_content = result.get("download_content")
                download_filename = result.get("download_filename")

                # Crear el mensaje del asistente con toda la información
                assistant_message = {
                    "role": "assistant",
                    "content": chat_response,
                    "download_content": download_content,
                    "download_filename": download_filename,
                }
                
            except requests.exceptions.RequestException as e:
                error_message = f"""
                **Error de Conexión**
                
                No pude comunicarme con mi equipo de expertos. Por favor, asegúrate de que el backend esté funcionando.
                
                *Detalles del error: {e}*
                """
                assistant_message = {"role": "assistant", "content": error_message}

    # Añadir el mensaje completo del asistente al historial y re-renderizar la página
    st.session_state.messages.append(assistant_message)
    st.rerun()