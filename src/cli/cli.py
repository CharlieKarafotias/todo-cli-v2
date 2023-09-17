from src.cli.parsers.top_level import init_top_level
from src.cli.handlers.status import handler as status_handler
from src.cli.handlers.init import handler as init_handler
from src.cli.handlers.add import handler as add_handler
from src.cli.handlers.list import handler as list_handler
from src.cli.handlers.delete import handler as delete_handler
from src.cli.handlers.uninit import handler as uninit_handler
from src.cli.handlers.setdb import handler as setdb_handler
from src.cli.handlers.listdb import handler as listdb_handler
from src.cli.handlers.update import handler as update_handler

def main(conn):
    """
    Design for CLI
        todo
            |-- add
            |-- delete
            |-- init
            |-- list
            |-- listdb
            |-- setdb
            |-- status
            |-- uninit
            |-- update
    TODO: Proposed Design for Future CLI
        todo
            |-- database
                |-- add
                    |-- name
                |-- remove
                    |-- name
                |-- list
                |-- set
                    |-- name
            |-- task
                |-- add
                    |-- name
                    |-- --description
                    |-- --priority
                    |-- --tags
                |-- complete
                    |-- id
                |-- delete
                    |-- id
                |-- list
                |-- remove
                    |-- id
                |-- update
                    |-- id
                    |-- --name
                    |-- --description
                    |-- --priority
                    |-- --tags
            |-- status (program level status)
    """
    parser = init_top_level()
    args = parser.parse_args()

    # Run the correct handler for the following commands
    # add, delete, init, list, status, uninit, update
    match args.command:
        case "add":
            add_handler(conn, args)
        case "delete":
            delete_handler(conn, args)
        case "init":
            init_handler(args)
        case "list":
            list_handler(conn)
        case "listdb":
            listdb_handler()
        case "setdb":
            setdb_handler(args)
        case "status":
            status_handler(conn)
        case "uninit":
            uninit_handler(args)
        case "update":
            update_handler(conn, args)
