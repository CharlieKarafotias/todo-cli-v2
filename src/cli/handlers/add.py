from src.database.operations import db_create_todo

def handler(conn, args):
    """
    Runs the handler that controls what happens when the add command is run
    :param conn: the database connection
    :param args: the arguments parsed by the parser
    :return: no return; adds a task to the database
    """

    db_create_todo(conn, {
        "todo_name": args.name,
        "description": args.description,
        "priority": args.priority,
        "tags": args.tags,  # TODO: need to add tags with multiple tables, refer to this: https://stackoverflow.com/questions/334183/what-is-the-most-efficient-way-to-store-tags-in-a-database
        }
    )
