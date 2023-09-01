import os
from cli.cli import main as cli_main
from database.initializer import connect_db
from utils.dotenv_manager import create_dotenv
from dotenv import load_dotenv

create_dotenv()  # skips if .env already exists
load_dotenv()

# connects to the current database name set
CURR_DB_NAME = os.getenv("CURR_DB_NAME")
conn = None

if CURR_DB_NAME != "":
    conn = connect_db(CURR_DB_NAME)

cli_main(conn)

if conn:
    conn.close()
