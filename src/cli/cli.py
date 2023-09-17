from src.cli.parsers.top_level import init_top_level
from src.cli.handlers.status import handler as status_handler
from src.cli.handlers.init import handler as init_handler
from src.cli.handlers.add import handler as add_handler
from src.cli.handlers.list import handler as list_handler
from src.cli.handlers.delete import handler as delete_handler
from src.cli.handlers.uninit import handler as uninit_handler
from src.cli.handlers.setdb import handler as setdb_handler

def main(conn):
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
            pass
        case "setdb":
            setdb_handler(args)
        case "status":
            status_handler(conn)
        case "uninit":
            uninit_handler(args)
        case "update":
            # update_handler(conn)
            pass
