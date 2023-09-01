def db_create_todo(conn, fields: dict):
    # TODO: update this to support new columns
    sql = f"INSERT INTO todo (todo_name) VALUES ('{fields['todo_name']}')"
    conn.execute(sql)
    conn.commit()


def db_read_todo(conn, id):
    sql = f"SELECT * FROM todo WHERE id = {id}"
    res = conn.execute(sql)
    print(res.fetchone())


def db_update_todo(conn, id, update_fields: dict = None):
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


def db_delete_todo(conn, id):
    sql = f"DELETE FROM todo WHERE id = {id}"
    conn.execute(sql)
    conn.commit()
