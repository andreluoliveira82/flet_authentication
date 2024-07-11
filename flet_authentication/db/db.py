import sqlite3
import os
from . import db_path


# function to verify if table exists
def table_exists(conn, table_name):
    """Checks if a table exists in the SQLite database connection.

    Args:
        conn: A sqlite3.Connection object representing the database connection.
        table_name: The name of the table to check for existence.

    Returns:
        True if the table exists, False otherwise.
    """

    cursor = conn.cursor()
    try:
        # Use a parameterized query with a tuple for safety and clarity
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (table_name,),
        )
        return cursor.fetchone() is not None
    except sqlite3.ProgrammingError as e:
        # Handle potential errors gracefully
        print(f"Error checking table existence: {e}")
        return False  # Assume table doesn't exist if error occurs


# function to create the dabase if not exists, and create the table users
def create_database():
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT NOT NULL, 
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
            """
        )
        conn.commit()
        conn.close()
    else:
        conn = sqlite3.connect(db_path)
        if not table_exists(conn, "users"):
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    first_name TEXT NOT NULL, 
                    last_name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
                """
            )
            conn.commit()
        conn.close()
