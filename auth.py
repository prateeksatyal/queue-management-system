# Purpose: Handles User Registration and Login logic. 
from database import get_db_connection
import sqlite3

def register_user(username, password, role):
    """
    Registers a new user in the database.
    Returns True if successful, False if username exists.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Simple plain text password storage as requested (academic purpose only)
        # In a real app, use hashing (bcrypt/sha256).
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                       (username, password, role))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # This occurs if username is not unique
        return False
    finally:
        conn.close()

def login_user(username, password):
    """
    Verifies user credentials.
    Returns the user row (dict-like) if valid, None otherwise.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if a user with this username AND password exists
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
                   (username, password))
    user = cursor.fetchone()
    
    conn.close()
    return user
