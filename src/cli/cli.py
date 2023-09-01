import argparse
from database.initializer import init_db
from database.operations import db_create_todo
from utils.dotenv_manager import update_db_scope


def main(conn):
    parser = argparse.ArgumentParser(
        prog="Todo CLI",
        description="A CLI for storing daily todo tasks",
        epilog="Developed in 2023 by Charlie Karafotias",
    )
    subparsers = parser.add_subparsers(title="Possible commands", dest="command")

    # Init parser instantiation
    parser_init = subparsers.add_parser(
        "init", help="Creates a new SQLite database for storing todo tasks"
    )
    parser_init.add_argument(
        "name",
        type=str,
        help="The name of the database. This will be stored in the folder './data/{name}.db",
    )

    # add new event parser instantiation
    # Properties to include: title, description, due date, priority, tags
    parser_add = subparsers.add_parser("add", help="Add a new todo")
    parser_add.add_argument(
        "name", help="The name of the todo event to add to the list."
    )
    parser_add.add_argument(
        "-d",
        "--description",
        help="The description of the new todo event",
        required=False,
    )
    parser_add.add_argument(
        "-p",
        "--priority",
        help="The priority of the new todo event. The default value will be low priority",
        default="low",
        required=False,
    )
    parser_add.add_argument(
        "-t",
        "--tags",
        nargs="+",
        help="One or more tags for the new todo event",
        required=False,
    )

    args = parser.parse_args()

    match args.command:
        case "init":
            init_db(args.name)
            # set .env variable
            update_db_scope(args.name)
        case "add":
            db_create_todo(
                conn,
                {
                    "todo_name": args.name,
                    "description": args.description,
                    "priority": args.priority,
                    "tags": args.tags,  # TODO: need to add tags with multiple tables, refer to this: https://stackoverflow.com/questions/334183/what-is-the-most-efficient-way-to-store-tags-in-a-database
                },
            )
