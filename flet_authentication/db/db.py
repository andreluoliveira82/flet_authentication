import sqlite3
import os
from . import db_path


# function to verify if table exists
def table_exists(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", {table_name}
    )
    return cursor.fetchone() is not None


# function to create the dabase if not exists, and create the table users
def create_database():
    conn = sqlite3.connect(db_path)

    #here if the database does not exist, create it and create the 'users' table automatically
    if not os.path.exists(db_path):
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT NOT NULL, 
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
            )
            """
        )
        conn.commit()
        conn.close()

# here, if the database already exists but the 'users' table does not yet exist, it will be created    elif not table_exists(conn, "users"):
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT NOT NULL, 
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
            )
            """
        )
    conn.commit()
    conn.close()
