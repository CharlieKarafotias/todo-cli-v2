from src.database.operations import db_read_all
from src.utils.console_printing import print_tasks

def handler(conn):
    """
    Runs the handler that controls what happens when the list command is run
    :param conn: the database connection
    :return: no return; prints all tasks to console
    """

    data = db_read_all(conn)
    print_tasks(data)
