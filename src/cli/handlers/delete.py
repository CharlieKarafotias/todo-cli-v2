from src.database.operations import db_delete_todo

def handler(conn, args):
    """
    Runs the handler that controls what happens when the delete command is run
    :param conn: the database connection
    :param args: the arguments collected by the delete subparser
    :return: no return; deletes the task from the database if found
    """

    db_delete_todo(conn, args.id)
