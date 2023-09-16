import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
ROOT_DIR = os.getenv("ROOT_DIR")


def connect_db(db_name: str) -> sqlite3.Connection:
    """
    Connects / Creates a new database and returns the connection
    @param db_name: the name of the database (file name)
    @return: the new database connection or None db can't be created
    """
    conn = sqlite3.connect(os.path.join(ROOT_DIR, "data", f"{db_name}.db"))
    return conn


def setup_table(conn):
    """
    Initializes the database with the given schema
    @param conn: the database connection
    """
    cur = conn.cursor()
    schema = ""
    with open(
        os.path.join(
            ROOT_DIR, "src", "database", "schemas", "create_table_todo.sqlite"
        ),
        "r",
    ) as f:
        schema = f.read()

    cur.execute(schema)


def init_db(db_name: str) -> sqlite3.Connection:
    """
    Creates a new database, sets up a todo table and returns the connection
    @param db_name: the name of the database file
    @returns: A database connection with a table named todo
    """
    if os.path.isfile(os.path.join(ROOT_DIR, "data", f"{db_name}.db")):
        conn = connect_db(db_name)
    else:
        # checks if there is a folder called data
        if not os.path.isdir(os.path.join(ROOT_DIR, "data")):
            os.mkdir(os.path.join(ROOT_DIR, "data"))
        conn = connect_db(db_name)
        setup_table(conn)
    return conn
