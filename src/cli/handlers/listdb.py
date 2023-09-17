from src.database.initializer import list_dbs
from src.utils.console_printing import print_databases

def handler():
    """
    Runs the handler that controls what happens when the listdb command is run
    :param conn: the database connection
    :return: no return; prints all databases to console
    """

    db_list = list_dbs()
    print_databases(db_list)
