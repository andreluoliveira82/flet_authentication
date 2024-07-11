import sqlite3

# function to connect database
def connect_to_database(db_path):
    conn =sqlite3.connect(db_path)
    return conn

# function to get data
def get_data(conn, table_name, conditions=None) -> dict:
    """
    Retrieves data from a database table.

    Args:
        conn: A database connection object.
        table_name (str): The name of the table to retrieve data from.
        conditions (str, optional): A SQL WHERE clause to filter the data. Defaults to None.

    Returns:
        dict: A list of dictionaries, where each dictionary represents a row in the table.

    Example:
        >>> conn = create_connection("mydatabase.db")  # Replace with your connection creation code
        >>> data = get_data(conn, "mytable", "age > 18")
        >>> print(data)
        [
            {'id': 1, 'name': 'John', 'age': 25},
            {'id': 2, 'name': 'Jane', 'age': 22},
            {'id': 3, 'name': 'Bob', 'age': 30}
        ]
    """
    cursor = conn.cursor()
    if conditions:
        sql_command = f"SELECT * FROM {table_name} WHERE {conditions}"
    else:
        sql_command = f"SELECT * FROM {table_name}"

    cursor.execute(sql_command)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    result = [{columns[i]:row[i]} for i in range(len(columns)) for row in rows]
    return result


# function to check if data exists
def check_data_exists(conn, table_name, condition) -> bool:
    """
    Checks if data exists in a table based on a given condition.

    Args:
        conn (connection object): A connection object to the database.
        table_name (str): The name of the table to check.
        condition (str): The condition to check for (e.g. "id = 1" or "name = 'John'").

    Returns:
        bool: True if data exists, False otherwise.

    """
    cursor = conn.cursor()
    sql_command = f"SELECT EXISTS (SELECT 1 FROM {table_name} WHERE {condition})"
    cursor.execute(sql_command)
    return cursor.fetchone()[0] == 1


# function to insert data into the table in database
def insert_data(conn, table_name, values) -> None:

    cursor = conn.cursor()
    columns = ", ".join(values.keys())
    placeholders = ", ".join(["?"] * len(values))
    sql_command = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.execute(sql_command, list(values.values()))
    conn.commit()
    conn.close()
    
    