from src.database.initializer import init_db
from src.utils.dotenv_manager import update_db_scope

def handler(args):
    """
    Runs the handler that controls what happens when init is called
    :param args: the arguments parsed by the parser
    :return: no return; creates a db and sets .env variables
    """

    init_db(args.name)
    # set .env variable
    update_db_scope(args.name)
