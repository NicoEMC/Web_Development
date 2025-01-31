import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def get_database():
    """
    Crea una conexión a la base de datos MongoDB.

    Returns:
        Database: Objeto de la base de datos MongoDB.
    """
    CONNECTION_STRING = os.getenv("MONGO_URI")
    if not CONNECTION_STRING:
        raise ValueError("La variable MONGO_URI no está configurada en el archivo .env")
    
    client = MongoClient(CONNECTION_STRING)
    # Define manualmente el nombre de la base de datos si no está en la URI
    db_name = "mydb"  # Cambia esto por el nombre deseado
    return client[db_name]