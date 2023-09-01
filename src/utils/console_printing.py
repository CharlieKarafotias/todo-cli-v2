from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


def print_err(message):
    colorama_init()
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")


def print_warn(message):
    colorama_init()
    print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")
