# 🍔 BurguerChatbot - Bembos AI Assistant (Demo)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75C2?logo=googlegemini&logoColor=white)](https://ai.google.dev/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=chainlink&logoColor=white)](https://github.com/langchain-ai/langchain)

Un sistema de asistente virtual inteligente con enfoque interactivo y juvenil adaptado a la identidad de la marca **Bembos Perú**. El ecosistema combina una interfaz web réplica de alta fidelidad visual y un motor conversacional avanzado potenciado por Inteligencia Artificial y arquitecturas de recuperación de información en tiempo real.

---

## 🚀 Características Clave

* **Frontend Premium & Urbano:** Réplica web dinámica basada en la paleta oficial de Bembos (azul, rojo y amarillo) usando fuentes modernas (`Rubik` y `Poppins`) y efectos de interacción fluida.
* **Chatbot In-App Integrado:** Caja de chat flotante embebida de manera nativa mediante un contenedor que consume la aplicación del servidor local sin redirecciones toscas.
* **Arquitectura RAG (Generación Aumentada por Recuperación):** Capacidad de consultar un menú dinámico de hamburguesas, combos y dúos sin requerir un reentrenamiento del modelo de lenguaje.
* **Control de Alucinaciones:** El sistema restringe sus respuestas exclusivamente al catálogo de productos indexado, mitigando la generación de información falsa o fuera del negocio de la franquicia.
* **Personalidad de Marca:** Respuestas moldeadas con tono amigable, entusiasta y uso de jerga juvenil local (*"causita"*, *"bravazo"*, *"billetera"*).

---

## 🏗️ Arquitectura del Sistema

El proyecto opera bajo un flujo desacoplado compuesto por dos capas principales interactuando en tiempo real:
