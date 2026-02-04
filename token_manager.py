# Purpose: core logic for Token management (Create, Read, Update, Reset).
from database import get_db_connection
import sqlite3

def generate_token(user_id):
    """
    Creates a new token for the given customer.
    The token number is auto-incremented based on the count of today's tokens.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Find the next token number (count existing tokens + 1)
    # Note: In a robust real system, we might need more complex logic.
    cursor.execute("SELECT COUNT(*) FROM tokens")
    count = cursor.fetchone()[0]
    next_token_num = count + 1
    
    cursor.execute("INSERT INTO tokens (user_id, token_number, status) VALUES (?, ?, ?)", 
                   (user_id, next_token_num, 'Pending'))
    conn.commit()
    conn.close()
    return next_token_num

def get_my_token(user_id):
    """
    Get the most recent active token for a specific customer.
    Returns None if no active token.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get the latest token for this user that isn't Completed yet
    cursor.execute("""
        SELECT * FROM tokens 
        WHERE user_id = ? AND status != 'Completed'
        ORDER BY id DESC LIMIT 1
    """, (user_id,))
    token = cursor.fetchone()
    conn.close()
    return token

def get_pending_tokens():
    """
    Returns a list of all tokens that are 'Pending'.
    Also fetch the username of the token holder for display.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT tokens.*, users.username 
        FROM tokens 
        JOIN users ON tokens.user_id = users.id
        WHERE status = 'Pending'
        ORDER BY tokens.id ASC
    """)
    tokens = cursor.fetchall()
    conn.close()
    return tokens

def get_current_serving():
    """
    Returns the token that is currently 'Serving'.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT tokens.*, users.username 
        FROM tokens 
        JOIN users ON tokens.user_id = users.id
        WHERE status = 'Serving'
        LIMIT 1
    """)
    token = cursor.fetchone()
    conn.close()
    return token

def get_next_pending():
    """
    Helper to see what the next pending token is (without updates).
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tokens WHERE status = 'Pending' ORDER BY id ASC LIMIT 1")
    token = cursor.fetchone()
    conn.close()
    return token

def call_next_token():
    """
    Staff action: Move 'Serving' to 'Completed', and the next 'Pending' to 'Serving'.
    1. Mark current 'Serving' => 'Completed'.
    2. Find oldest 'Pending' => 'Serving'.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Complete current
    cursor.execute("UPDATE tokens SET status = 'Completed' WHERE status = 'Serving'")
    
    # 2. Find next pending
    cursor.execute("SELECT id FROM tokens WHERE status = 'Pending' ORDER BY id ASC LIMIT 1")
    next_token = cursor.fetchone()
    
    if next_token:
        cursor.execute("UPDATE tokens SET status = 'Serving' WHERE id = ?", (next_token['id'],))
        
    conn.commit()
    conn.close()

def complete_current_token():
    """
    Staff action: Mark the currently serving token as Completed.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tokens SET status = 'Completed' WHERE status = 'Serving'")
    conn.commit()
    conn.close()

def reset_queue():
    """
    Staff action: Deletes ALL tokens to restart the day.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tokens")
    # Optional: Reset SQLite auto-increment or keep growing? 
    # For a simple project, keeping ID growing is fine.
    conn.commit()
    conn.close()
