# 🍔 BurguerChatbot - Bembos AI Assistant (Premium RAG)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75C2?logo=googlegemini&logoColor=white)](https://ai.google.dev/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=chainlink&logoColor=white)](https://github.com/langchain-ai/langchain)

Este proyecto implementa un asistente virtual inteligente embebido en una interfaz réplica de alta fidelidad para la marca **Bembos Perú**. El ecosistema combina una experiencia de usuario interactiva y juvenil en el frontend junto con un motor conversacional avanzado potenciado por Inteligencia Artificial y una arquitectura de recuperación de información semántica en tiempo real.

---

## 🚀 Características del Proyecto

* **Frontend Premium & Urbano:** Interfaz web fluida basada en la paleta de colores oficial de Bembos (azul, rojo y amarillo) utilizando fuentes dinámicas (`Rubik` y `Poppins`) y animaciones interactivas.
* **Experiencia In-App Unificada:** Ventana de chat flotante integrada de forma nativa a través de un contenedor `iframe` optimizado, eliminando redirecciones toscas hacia el backend.
* **Arquitectura RAG (Generación Aumentada por Recuperación):** Capacidad de consultar un menú estructurado (Hamburguesas, Combos Personales, Dúos y Promociones) sin requerir el reentrenamiento del modelo base.
* **Mitigación de Alucinaciones:** El sistema restringe el contexto de respuesta estrictamente al archivo indexado, impidiendo que el bot invente información o desvíe la conversación fuera del negocio.
* **Personalidad Corporativa:** Respuestas adaptadas al tono amigable y entusiasta que caracteriza la identidad de la marca, empleando expresiones y jergas juveniles del entorno peruano.

---

## 🏗️ Arquitectura del Sistema

El flujo de información opera bajo un diseño desacoplado que interactúa en tiempo real:

[ Usuario ]
│
▼ (Interactúa en la Web Réplica)
[ Frontend HTML/CSS/JS ]
│
▼ (A través de un iframe embebido)
[ Backend Streamlit ]
│
├─► [ ChromaDB (Vector Store) ] ── (Busca similitud semántica) ──► [ Menú Local ]
│                                                                        │
▼ (Genera Prompt Enriquecido: Instrucción + Contexto + Pregunta)          │
[ Google Gemini API (LLM) ] ◄────────────────────────────────────────────────┘
│
▼ (Respuesta con identidad Bembos)
[ Interfaz de Usuario ]


### Componentes Tecnológicos
1. **Capa de Presentación:** HTML5, CSS3 (Grid y Flexbox), JavaScript nativo para el control del chat y FontAwesome para la iconografía.
2. **Capa de Recuperación (RAG):** Base de datos vectorial **ChromaDB** alimentada por modelos de embedding locales `sentence-transformers/all-MiniLM-L6-v2` mediante **LangChain**.
3. **Capa de Inferencia:** Modelo fundacional **Gemini 2.5 Flash** gestionado mediante estados de sesión de Streamlit para preservar el hilo y la memoria del chat de forma limpia.

---

## 💻 Instalación y Despliegue Local

### Requisitos Previos
* Tener Python 3.10 o superior instalado.
* Disponer de una API Key válida en Google AI Studio (Gemini API).

### 1. Clonar el repositorio e instalar dependencias
# Clonar el proyecto
git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
cd TU_REPOSITORIO

# Instalar las librerías necesarias
pip install streamlit google-generativeai langchain-community langchain-chroma sentence-transformers

2. Indexar el Catálogo del Menú en la Base de Datos
Asegúrate de que tu archivo menu_bembos.txt se encuentre en la raíz del proyecto y ejecuta el script de vectorización automatizada para poblar la persistencia local de ChromaDB:
python indexar_datos.py

3. Ejecutar el Ecosistema
Inicia el servidor lógico que orquesta el backend del chatbot con Streamlit:
streamlit run app.py

Por último, abre el archivo index.html de la capa de presentación directamente en tu navegador preferido. El componente flotante se conectará de manera automática al puerto local http://localhost:8501/?embed=true.

📂 Estructura del Proyecto
index.html: Capa de interfaz web interactiva con estilo corporativo Bembos.
app.py: Backend lógico en Streamlit que procesa la entrada del usuario, realiza la búsqueda en ChromaDB e invoca la API de Gemini.
rag_setup.py: Script automatizado para la fragmentación, generación de embeddings y almacenamiento persistente en el Vector Store.
menu.txt: Dataset en texto plano que contiene la estructura detallada de las hamburguesas, ingredientes, alérgenos, promociones y stocks vigentes.

/chroma_db/: Directorio autogenerado que contiene los índices y vectores locales procesados.

💡 Proyecto académico desarrollado en el marco del Laboratorio de Inteligencia Artificial y Robótica (LIAR) - FIA USMP, 2026.
