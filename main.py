import os
from dotenv import load_dotenv
from src.cli.cli import main as cli_main
from src.database.initializer import connect_db
from src.utils.dotenv_manager import create_dotenv

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
