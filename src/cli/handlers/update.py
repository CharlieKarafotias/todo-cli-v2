from src.database.operations import db_update_todo

def handler(conn, args):
    """
    Runs the handler that controls what happens when the update command is run
    :param conn: the database connection
    :param args: the arguments parsed by the parser
    :return: no return; updates a task in the database
    """
    fields = {}
    if args.name:
        fields['todo_name'] = args.name
    if args.description:
        fields['description'] = args.description
    if args.priority:
        fields['priority'] = args.priority
    if args.tags:
        fields['tags'] = args.tags

    db_update_todo(conn, args.id, fields)
