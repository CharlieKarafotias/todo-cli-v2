from cli.parsers.top_level import init_top_level
from database.initializer import init_db
from database.operations import db_create_todo, db_read_all
from utils.dotenv_manager import update_db_scope
from utils.console_printing import print_tasks
from cli.handlers.status import handler as status_handler


def main(conn):
    parser = init_top_level()
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
        case "list":
            data = db_read_all(conn)
            print_tasks(data)
        case "status":
            status_handler()