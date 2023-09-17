from sqlite3 import Connection, OperationalError
from src.utils.console_printing import print_err


def db_create_todo(conn: Connection, fields: dict) -> None:
    """
    .. |keys| replace:: ["todo_name", "description", "priority"]

    Create a new task in the database.

    Currently, the function supports the following keys for the fields dictionary:
    |keys|

    :param conn: the database connection
    :param fields: the values added for the task as key-value pairs
    :return: no return; table is updated to include this row
    """
    # TODO: update this to support new columns
    acceptable_columns = [
        "todo_name",
        "description",
        "priority",
    ]

    # check which fields are updated and add them to verified_fields
    try:
        verified_fields = {}
        for k, v in fields.items():
            if k in acceptable_columns:
                verified_fields[k] = v

        sql = "INSERT INTO todo ("
        for k in verified_fields.keys():
            sql = sql + f"{k}, "
        sql = sql[:-2] + ") VALUES ("
        for k in verified_fields.values():
            sql = sql + f"'{k}', "
        sql = sql[:-2] + ")"
        conn.execute(sql)
        conn.commit()
    except OperationalError:
        print_err('ERROR: Unable to add to database at this time')


def db_read_todo(conn: Connection, id: str):
    """
    Returns the task matching 'id' (if it exists) from the database specified by 'conn'

    :param conn: the database connection
    :param id: the id of the task
    :return: A dictionary containing the fields
    """

    # TODO: add in dictionary return using util that converts rows into [dictionary]
    sql = f"SELECT * FROM todo WHERE id = {id}"
    res = conn.execute(sql)
    val = res.fetchone()
    print(val)
    return val


def db_read_all(conn: Connection):
    """
    Returns all todos (including completed ones)

    :param conn: the database connection
    :return: a list of todos
    """

    sql = f"SELECT * FROM todo"
    res = conn.execute(sql)
    return res.fetchall()


def db_update_todo(conn: Connection, id: str, update_fields: dict = None):
    """
    Updates an existing todo with id 'id' in the specified database 'conn' under the table 'todo'.

    :param conn: the database connection
    :param id: the id of the todo
    :param update_fields: the fields to be updated
    :return: No return; updates fields in database
    """
    
    # TODO: update this to support: tags
    acceptable_columns = [
        "todo_name",
        "description",
        "priority"
    ]
    # check which fields are updated and add them to verified_fields
    verified_fields = {}
    for k, v in update_fields.items():
        if k in acceptable_columns:
            verified_fields[k] = v

    if verified_fields:
        sql = f"UPDATE todo SET "
        # append the updated fields into the sql statement

        for k, v in verified_fields.items():
            sql = sql + f"{k} = '{v}', "

        # get full sql except ", " and then add id to update
        sql = sql[:-2] + f" WHERE id = {id}"
        conn.execute(sql)
        conn.commit()


def db_delete_todo(conn: Connection, id: str):
    """
    Deletes the task with id 'id' if it exists in the database specified by 'conn'

    :param conn: the database connection
    :param id: the id of the task to delete
    :return: no return; deletes the task if it exists in the database
    """

    sql = f"DELETE FROM todo WHERE id = {id}"
    conn.execute(sql)
    conn.commit()
