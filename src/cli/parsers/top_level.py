import argparse


def init_top_level() -> argparse.ArgumentParser:
    """
    Initializes the top level parser and attaches a command subparser to the top level.
    :return: returns a fully initializes parser with all available commands attached
    """
    parser = argparse.ArgumentParser(
        prog="Todo CLI",
        description="A CLI for storing daily todo tasks",
        epilog="Developed in 2023 by Charlie Karafotias",
    )

    command_parser = parser.add_subparsers(title="Possible commands", dest="command")
    init_add_level(command_parser)
    init_delete_level(command_parser)
    init_init_level(command_parser)
    init_list_level(command_parser)
    init_setdb_level(command_parser)
    init_status_level(command_parser)
    init_uninit_level(command_parser)

    return parser


def init_init_level(command_subparser):
    """
    Initializes the subparser for the init operation. 
    The init parser defines the name argument representing the name of the database file.
    :param command_subparser: a subparser representing a command
    :return: no return; the init command is added as an option for the command position of the CLI
    """
    parser_init = command_subparser.add_parser(
        "init", help="Creates a new SQLite database for storing todo tasks"
    )
    parser_init.add_argument(
        "name",
        type=str,
        help="The name of the database. This will be stored in the folder './data/{name}.db",
    )


def init_add_level(command_subparser):
    """
    Initializes the subparser for the add operation. 
    The add parser defines several arguments: name, --description, --priority, --tags
    :param command_subparser: a subparser representing a command
    :return: no return; the add command is added as an option for the command position of the CLI
    """
    parser_add = command_subparser.add_parser("add", help="Add a new todo")
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


def init_list_level(command_subparser):
    """
    Initializes the subparser for the list operation. 
    :param command_subparser: a subparser representing a command
    :return: no return; the list command is added as an option for the command position of the CLI
    """
    command_subparser.add_parser("list", help="Lists the tasks currently stored")


def init_status_level(command_subparser):
    """
    Initializes the subparser for the status operation. 
    :param command_subparser: a subparser representing a command
    :return: no return; the status command is added as an option for the command position of the CLI
    """
    command_subparser.add_parser(
        "status",
        help="Shows status of the todo cli (current database name and path, task information, etc.)"
    )


def init_delete_level(command_subparser):
    """
    Initializes the subparser for the delete operation. 
    :param command_subparser: a subparser representing a command
    :return: no return; the delete command is added as an option for the command position of the CLI
    """
    parser_delete = command_subparser.add_parser("delete", help="Deletes a task")
    parser_delete.add_argument(
        "id", help="The id of the task to delete"
    )


def init_uninit_level(command_subparser):
    """
    Initializes the subparser for the uninit operation. 
    The uninit parser deletes the current database (if it exists) and resets the .env file
    :param command_subparser: a subparser representing a command
    :return: no return; the uninit command is added as an option for the command position of the CLI
    """
    parser_init = command_subparser.add_parser(
        "uninit", help="Deletes an existing SQLite database (if it exists)"
    )
    parser_init.add_argument(
        "name",
        type=str,
        help="The name of the database. The current database set can be found by running the 'status' command",
    )


def init_setdb_level(command_subparser):
    """
    Initializes the subparser for the setdb operation. 
    :param command_subparser: a subparser representing a command
    :return: no return; the setdb command is added as an option for the command position of the CLI
    """
    parser_setdb = command_subparser.add_parser(
        "setdb",
        help="Change the working database to a different (already existing) database. Use the listdb command to see all existing databases."
    )
    parser_setdb.add_argument(
        "name",
        type=str,
        help="The name of the database to change to.",
    )
