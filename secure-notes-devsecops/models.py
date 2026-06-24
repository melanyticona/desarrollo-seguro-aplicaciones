from db import get_db
from mysql.connector import Error


def get_user_by_username(username):
    db = None
    cursor = None
    
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        
        cursor.execute(
            "SELECT id, username, password FROM usuarios WHERE username = %s",
            (username,)
        )
        
        user = cursor.fetchone()
        return user
    
    except Error as e:
        print(f"Error en get_user_by_username: {e}")
        return None
    
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


def get_user_by_id(user_id):
    db = None
    cursor = None
    
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        
        cursor.execute(
            "SELECT id, username, password FROM usuarios WHERE id = %s",
            (user_id,)
        )
        
        user = cursor.fetchone()
        return user
    
    except Error as e:
        print(f"Error en get_user_by_id: {e}")
        return None
    
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()