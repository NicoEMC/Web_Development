from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener la URI de conexión desde el archivo .env
MONGO_URI = os.getenv("MONGO_URI")

def test_mongodb_connection():
    """
    Prueba la conexión a MongoDB Atlas.
    """
    print("🔍 Probando conexión a MongoDB...")

    try:
        client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
        db = client.get_database()

        # Intentar obtener las colecciones
        collections = db.list_collection_names()
        print(f"✅ Conexión exitosa. Colecciones disponibles: {collections}")
    except Exception as e:
        print(f"❌ Error en la conexión a MongoDB: {e}")

if __name__ == "__main__":
    test_mongodb_connection()