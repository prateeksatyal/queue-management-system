# Purpose: Handles database connection and table creationimport sqlite3

# Define the database file name
DB_NAME = "queue_system.db"

def get_db_connection():
    """
    Creates and returns a connection to the SQLite database.
    This simple project uses a local file 'queue_system.db'.
    """
    conn = sqlite3.connect(DB_NAME)
    # This allows us to access columns by name (row["column_name"])
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    """
    Creates the necessary tables (users, tokens) if they don't exist.
    Run this function once when the app starts.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Create Users Table
    # Stores login credentials and role (Customer/Staff)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    # 2. Create Tokens Table
    # Stores queue tokens linked to users.
    # status can be 'Pending', 'Serving', 'Completed'
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            token_number INTEGER NOT NULL,
            status TEXT DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    conn.commit()
    conn.close()
    print("Database and tables checked/created successfully.")

if __name__ == "__main__":
    # If we run this file directly, it will setup the DB
    create_tables()
