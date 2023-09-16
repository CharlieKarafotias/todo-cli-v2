from sqlite3 import Connection

def db_create_todo(conn: Connection, fields: dict):
    """
    Creates a new todo in the database specified by 'conn' under the 'todo' table
    @param conn: the database connection
    @param fields: key-value pairs specifying the values to be added for the new todo. Supported keys: "todo_name", "description", "priority"
    """
    # TODO: update this to support new columns
    acceptable_columns = [
        "todo_name",
        "description",
        "priority",
    ]

    # check which fields are updated and add them to verified_fields
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


def db_read_todo(conn: Connection, id: str):
    """
    Returns the todo matching 'id' (if it exists) from the database specified by 'conn'
    @param conn: the database connection
    @param id: the id of the todo
    @returns: A dictionary containing the fields
    """
    # TODO: add in dictionary return using util that converts rows into [dictionary]
    sql = f"SELECT * FROM todo WHERE id = {id}"
    res = conn.execute(sql)
    print(res.fetchone())


def db_read_all(conn: Connection):
    """
    Returns all todos (including completed ones)
    @param conn: the database connection
    @returns: a list of todos
    """
    sql = f"SELECT * FROM todo"
    res = conn.execute(sql)
    return res.fetchall()


def db_update_todo(conn: Connection, id: str, update_fields: dict = None):
    """
    Updates an existing todo with id 'id' in the specified database 'conn' under the table 'todo'.
    @param conn: the database connection
    @param id: the id of the todo
    @param update_fields: the fields to be updated
    """
    # TODO: define a better way of copying the schema so this doesn't need updating each time
    # TODO: update this to support new columns
    acceptable_columns = [
        "todo_name",
    ]
    # check which fields are updated and add them to verified_fields
    verified_fields = {}
    for k, v in update_fields.items():
        if k in acceptable_columns:
            verified_fields[k] = v

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
    Deletes the todo with id 'id' if it exists in the database specified by 'conn'
    @param conn: the database connection
    @param id: the id of the todo to delete
    """
    sql = f"DELETE FROM todo WHERE id = {id}"
    conn.execute(sql)
    conn.commit()
