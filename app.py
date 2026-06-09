import streamlit as st
import google.generativeai as genai
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# =====================================================================
# 1. CONFIGURACIÓN DE LA PÁGINA (¡Siempre debe ir primero!)
# =====================================================================
st.set_page_config(page_title="BurguerChatbot", page_icon="🍔")
st.title("")

# Configuración de API Key
genai.configure(api_key="AIzaSyBVaN7gQDhBrq8iYpkDS37ppzMhOaEIYiw")

# =====================================================================
# 2. BASE DE DATOS Y CONFIGURACIÓN DE GEMINI
# =====================================================================
# Inicializamos embeddings y Base de Datos RAG
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

def get_context(query):
    results = db.similarity_search(query, k=2)
    return "\n".join([doc.page_content for doc in results])

# Definimos el modelo antes de la interfaz para que esté disponible globalmente
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash', # Actualizado al modelo estándar compatible
    system_instruction=(
        "Eres un asistente de hamburguesas de Bembos. Responde de forma amable, "
        "juvenil y entusiasta. Responde basándote estrictamente en el contexto del menú provisto. "
        "Si el usuario te saluda o hace preguntas de cortesía, responde amigablemente sin pedir contexto. "
        "Si te pregunta algo fuera del menú que no sabes, di que no tienes esa información cordialmente."
    )
)

# =====================================================================
# 3. FUNCIONES DE CONTROL (CALLBACKS)
# =====================================================================
def limpiar_conversacion():
    # Reinicia el chat de Gemini limpiamente desde el estado de la sesión
    st.session_state.chat = model.start_chat(history=[])

# Inicialización del chat en la sesión si no existe
if "chat" not in st.session_state:
    limpiar_conversacion()

# =====================================================================
# 4. PANEL LATERAL (Configuración)
# =====================================================================
with st.sidebar:
    st.header("⚙️ Configuración")
    st.write("Personaliza tu asistente:")
    
    # Widgets de personalización
    temperatura = st.slider("Creatividad (Temperatura)", 0.0, 1.0, 0.7)
    modo = st.selectbox("Personalidad", ["Asistente Amigable", "Asistente Formal"])
    
    st.divider()
    st.write("Acciones:")
    # Usamos 'on_click' para ejecutar la limpieza de manera segura antes de renderizar
    st.button("Limpiar conversación 🧹", on_click=limpiar_conversacion, use_container_width=True)
    
    st.divider()
    st.write("Info del Proyecto:")
    st.caption("Proyecto IA - USMP 2026")

# =====================================================================
# 5. MOSTRAR HISTORIAL PREVIO
# =====================================================================
for message in st.session_state.chat.history:
    role = "user" if message.role == "user" else "assistant"
    # Evitamos mostrar el texto feo del "Contexto del menú" al usuario en la interfaz
    text_to_show = message.parts[0].text
    if "Contexto del menú:" in text_to_show and "\n\nPregunta del usuario:" in text_to_show:
        # Extraemos solo la pregunta original del usuario para que el chat se vea limpio
        text_to_show = text_to_show.split("\n\nPregunta del usuario: ")[1]
        
    with st.chat_message(role):
        st.markdown(text_to_show)

# =====================================================================
# 6. INTERACCIÓN Y PROCESAMIENTO (RAG)
# =====================================================================
if prompt := st.chat_input("¿Qué deseas ordenar?"):
    # 1. Mostramos inmediatamente el mensaje del usuario en la UI
    st.chat_message("user").markdown(prompt)
    
    # 2. Obtenemos contexto de tu ChromaDB
    context = get_context(prompt)
    
    # 3. Creamos el prompt enriquecido para Gemini
    full_prompt = f"Contexto del menú:\n{context}\n\nPregunta del usuario: {prompt}"
    
    # 4. Enviamos a la API de Gemini y mostramos la respuesta en vivo
    with st.chat_message("assistant"):
        # Ajustamos los parámetros dinámicamente según los sliders del sidebar
        config = genai.types.GenerationConfig(temperature=temperatura)
        response = st.session_state.chat.send_message(full_prompt, generation_config=config)
        st.markdown(response.text)