import argparse


def init_top_level() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="Todo CLI",
        description="A CLI for storing daily todo tasks",
        epilog="Developed in 2023 by Charlie Karafotias",
    )

    command_parser = parser.add_subparsers(title="Possible commands", dest="command")
    init_add_level(command_parser)
    init_init_level(command_parser)
    init_status_level(command_parser)
    # TODO: add support for listing all tasks, completed tasks, in progress tasks, today's tasks (should be the
    #  default)
    #  TODO: add support for status (should show current database (name); where it is stored; number of
    #   tasks today; total task number)

    return parser


def init_init_level(command_subparser):
    # Init parser instantiation
    parser_init = command_subparser.add_parser(
        "init", help="Creates a new SQLite database for storing todo tasks"
    )
    parser_init.add_argument(
        "name",
        type=str,
        help="The name of the database. This will be stored in the folder './data/{name}.db",
    )


def init_add_level(command_subparser):
    # Properties to include: title, description, due date, priority, tags
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
    parser_read = command_subparser.add_parser("list", help="Lists the tasks currently stored")
    pass


def init_status_level(command_subparser):
    # Init parser instantiation
    parser_init = command_subparser.add_parser(
        "status", help="Shows status of the todo cli (current database name and path, task information, etc.)"
    )
