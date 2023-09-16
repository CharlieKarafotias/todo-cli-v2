from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from datetime import datetime


def print_err(message):
    colorama_init()
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")


def print_warn(message):
    colorama_init()
    print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")


def print_tasks(data):
    """
    Turns a list of tasks into a nicely formatted console output.
    @param data: a list of tasks in format [(task), (task)]
    @return: None; prints to console
    """
    # TODO: automate this as a util function so you can get acceptable columns anytime from schema file
    database_schema = {
        "0": "id",
        "1": "todo_name",
        "2": "description",
        "3": "priority",
        "4": "create_date",
        "5": "complete_date",
    }
    colorama_init()
    for task in data:
        start_date = datetime.strptime(task[4], "%Y-%m-%d %H:%M:%S").strftime(
            "%m-%d-%y"
        )
        end_date = (
            datetime.strptime(task[4], "%Y-%m-%d %H:%M:%S").strftime("%m-%d-%y")
            if task[5]
            else "IN-PROGRESS"
        )

        print(
            f"{database_schema['0']}: {task[0]} - {Style.BRIGHT}{task[1]}{Style.RESET_ALL} | ({start_date} - {end_date})"
        )

    pass
