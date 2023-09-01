import os


def dotenv_exists():
    file_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_root_lst = file_dir.split("/")[:-2]
    root_dir = "/"
    for i in path_to_root_lst:
        root_dir = os.path.join(root_dir, i)

    return os.path.isfile(os.path.join(root_dir, ".env"))


def create_dotenv():
    if not dotenv_exists():
        with open(".env", "w") as f:
            f.write("CURR_DB_NAME=")


def update_db_scope(db_name):
    create_dotenv()
    l = None
    with open(".env") as f:
        l = list(f)

    with open(".env", "w") as output:
        for line in l:
            if line.startswith("CURR_DB_NAME"):
                output.write(f"CURR_DB_NAME={db_name}\n")
            else:
                output.write(line)
