from src.database.initializer import remove_db
from src.utils.dotenv_manager import update_db_scope
from src.utils.console_printing import print_err

def handler(args):
    """
    Runs the handler that controls what happens when uninit is called
    :param args: the arguments parsed by the parser
    :return: no return; removes the specified db (if it exists) and sets .env variables
    """

    if remove_db(args.name):
        # Returns True if database is removed
        # set .env variable to empty string; no db will be set if it is deleted
        update_db_scope('')
    else:
        print_err(f'ERROR: No database found with the name {args.name}')
