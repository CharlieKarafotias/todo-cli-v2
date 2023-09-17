from src.database.initializer import existing_db
from src.utils.dotenv_manager import update_db_scope
from src.utils.console_printing import print_err

def handler(args):
    """
    Runs the handler that controls what happens when setdb is called
    :param args: the arguments parsed by the parser
    :return: no return; sets the database in the .env file (if it exists)
    """

    if existing_db(args.name):
        # set .env variable
        update_db_scope(args.name)
    else: 
        print_err(f'ERROR: The database "{args.name}" was not found. Use the init command to create the database instead.')
