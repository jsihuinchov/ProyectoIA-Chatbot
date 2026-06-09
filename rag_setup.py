from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma

try:
    from langchain_community.embeddings import HuggingFaceEmbeddings
except ModuleNotFoundError as e:
    print("Error: falta la dependencia necesaria para los embeddings.")
    print("Instala torch y torchvision en este entorno con:")
    print("    pip install torch torchvision")
    raise

# 1. Cargamos el archivo de menú que acabas de crear
loader = TextLoader("menu.txt", encoding='utf-8')
docs = loader.load()

# 2. Preparamos el modelo local (HuggingFace) para convertir texto a vectores
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 3. Creamos la base de datos ChromaDB y la guardamos en la carpeta 'chroma_db'
db = Chroma.from_documents(docs, embeddings, persist_directory="./chroma_db")

print("¡Base de datos creada exitosamente!")