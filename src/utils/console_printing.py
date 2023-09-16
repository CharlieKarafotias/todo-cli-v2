from datetime import datetime
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from terminaltables import AsciiTable


def print_err(message):
    colorama_init()
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")


def print_warn(message):
    colorama_init()
    print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")


def print_tasks(data):
    """
    Turns a list of tasks into a nicely formatted console output.
    :param data: a list of tasks in format [(task), (task)]
    :return: None; prints to console
    """

    columns = ['id', 'todo_name', 'description', 'priority', 'create_date', 'complete_date']

    table_data = [
        columns
    ]

    for task in data:
        start_date = datetime.strptime(task[4], "%Y-%m-%d %H:%M:%S").strftime(
            "%m-%d-%y"
        )
        end_date = (
            datetime.strptime(task[5], "%Y-%m-%d %H:%M:%S").strftime("%m-%d-%y")
            if task[5]
            else "IN-PROGRESS"
        )
        table_data.append([
            task[0], task[1], task[2], task[3], start_date, end_date
        ])
    
    table = AsciiTable(table_data)
    print(table.table)
