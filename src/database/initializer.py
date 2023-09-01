import sqlite3
import os
from utils.console_printing import print_err


def connect_db(db_name: str) -> sqlite3.Connection:
    """
    Connects / Creates a new database and returns the connection
    @param db_name: the name of the database (file name)
    @return: the new database connection or None db can't be created
    """
    conn = sqlite3.connect(f"./data/{db_name}.db")
    return conn


def setup_table(conn):
    """
    Initializes the database with the given schema
    @param conn: the database connection
    """
    cur = conn.cursor()
    schema = ""
    with open("./src/database/schemas/create_table_todo.sqlite", "r") as f:
        schema = f.read()

    cur.execute(schema)


def init_db(db_name: str) -> sqlite3.Connection:
    """
    Creates a new database, sets up a todo table and returns the connection
    @param db_name: the name of the database file
    @returns: A database connection with a table named todo
    """
    if os.path.isfile(f"./data/{db_name}.db"):
        conn = connect_db(db_name)
    else:
        conn = connect_db(db_name)
        setup_table(conn)
    return conn
