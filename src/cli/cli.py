from src.cli.parsers.top_level import init_top_level
from src.cli.handlers.status import handler as status_handler
from src.cli.handlers.init import handler as init_handler
from src.cli.handlers.add import handler as add_handler
from src.cli.handlers.list import handler as list_handler

def main(conn):
    parser = init_top_level()
    args = parser.parse_args()

    match args.command:
        case "init":
            init_handler(args)
        case "add":
            add_handler(conn, args)
        case "list":
            list_handler(conn)
        case "status":
            status_handler(conn)
