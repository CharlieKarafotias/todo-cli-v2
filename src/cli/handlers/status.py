import os
import sqlite3
from dotenv import load_dotenv
from src.database.operations import db_read_all

def handler(conn: sqlite3.Connection) -> dict:
    """
    Handles the status command
    :param conn: the database connection
    :return: a dictionary containing daata making up status
    """
    data = {
        'db_name': None,
        'db_absolute_path': None,
        'total_tasks': None
    }
    # get env variables
    load_dotenv()
    data['db_name'] = os.getenv("CURR_DB_NAME")
    data['db_absolute_path'] = os.path.join(os.getenv("ROOT_DIR"), "data", f"{data['db_name']}.db")

    # get total tasks
    data['total_tasks'] = len(db_read_all(conn))
    status_printer(data)
    return data


def status_printer(data: dict) -> None:
    key_terms = {
        'db_name': 'Current Database Set: ',
        'db_absolute_path': 'Absolute Path To Database File: ',
        'total_tasks': 'Total Tasks Stored In Database: '
    }
    for k, v in data.items():
        if k in key_terms:
            print(f'{key_terms[k]}{v}')
        else:
            print(f'{k}: {v}')
