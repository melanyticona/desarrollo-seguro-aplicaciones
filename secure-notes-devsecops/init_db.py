import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()


def init_database():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        
        cursor = connection.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS secure_notes")
        
        cursor.execute("USE secure_notes")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        connection.commit()
        cursor.close()
        connection.close()
        
        print("Base de datos inicializada correctamente")
        return True
        
    except Error as e:
        print(f"ADVERTENCIA: No se pudo conectar a MySQL")
        print(f"Asegurate que MySQL Server esta corriendo")
        print(f"Error: {e}")
        return False