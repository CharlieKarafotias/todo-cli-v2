import pytest
from src.database.initializer import init_db, remove_db
from src.database.operations import *


class TestDBOperations:
    def setup_method(self):
        """
        Setup any state tied to the execution of the given method in a
        class. Setup_method is invoked for every test method of a class.
        """
        self._conn = init_db('test_db_operations')


    def teardown_method(self):
        """
        Teardown any state that was previously setup with a setup_method call.
        """
        remove_db('test_db_operations')


    def test_db_create_todo_all_valid_fields(self):
        """
        Test to ensure that a new task is created correctly when all valid fields
        are supplied.
        """
        fields = {
            'todo_name': 'test',
            'description': 'this is a test todo',
            'priority': 'medium'
        }
        db_create_todo(self._conn, fields)
        res = db_read_todo(self._conn, '1')
        assert res[0] == 1  # check id
        assert res[1] == fields['todo_name'] # check todo_name
        assert res[2] == fields['description'] # check description
        assert res[3] == fields['priority'] # check priority


    def test_db_create_no_fields(self, capfd):
        """
        Test to ensure that a new task is not created when incorrect fields
        are supplied. Also tests for error message to console.
        """
        fields = {}
        db_create_todo(self._conn, fields)

        # ensure no task was added to table
        assert len(db_read_all(self._conn)) == 0

        # ensure correct error message
        out, _ = capfd.readouterr()
        assert out == "ERROR: Unable to add to database at this time\n"


    def test_db_create_todo_minimum_valid_fields(self):
        """
        Test to ensure that a new task is created correctly when all valid fields
        are supplied.
        """
        fields = {
            'todo_name': 'minimum task field',
        }
        db_create_todo(self._conn, fields)
        res = db_read_todo(self._conn, '1')
        assert res[0] == 1  # check id
        assert res[1] == fields['todo_name'] # check todo_name
        assert res[2] is None # check description is not set
        assert res[3] is None # check priority is not set


    def test_db_read_todo_invalid_id(self, capfd):
        """
        Test to ensure that a db_read_todo does not return a todo
        when the id given doesn't exist in the database.
        """
        res = db_read_todo(self._conn, '1')
        out, _ = capfd.readouterr()
        assert out == "None\n"
        assert res is None


    def test_db_read_todo_valid_id(self, capfd):
        """
        Test to ensure that after a new task is created, it 
        can be read correctly.
        """
        # Create task and add to db
        fields = {
            'todo_name': 'test',
            'description': 'this is a test todo',
            'priority': 'medium'
        }
        db_create_todo(self._conn, fields)

        # Read todo
        res = db_read_todo(self._conn, '1')

        # Ensure printout occurs
        out, _ = capfd.readouterr()
        assert out is not None

        # Ensure fields in return tuple are correct
        assert res[0] == 1  # check id
        assert res[1] == fields['todo_name'] # check todo_name
        assert res[2] == fields['description'] # check description
        assert res[3] == fields['priority'] # check priority


    def test_db_read_all_empty_db(self):
        """
        Test to ensure that read_all returns [] and no printout when
        there are no tasks in the database.
        """
        # Read all todos
        res = db_read_all(self._conn)

        # Ensure Empty List Is Returned
        assert res == []


    def test_db_read_all_multiple_tasks(self):
        """
        Test to ensure that read_all returns list of tasks 
        when database has tasks.
        """
        # Create multiple tasks
        fields = {
            'todo_name': 'minimum task field',
        }
        db_create_todo(self._conn, fields)
        db_create_todo(self._conn, fields)
        db_create_todo(self._conn, fields)

        # Read all todos
        res = db_read_all(self._conn)

        # Ensure List Is Returned
        assert len(res) == 3
        # Ensure tasks are listed
        assert res[1][1] == 'minimum task field'


    def test_db_update_todo_valid_field(self):
        """
        Test that db_update_todo updates the correct field
        """
        assert True


    def test_db_update_todo_multiple_valid_field(self):
        """
        Test that db_update_todo updates all the valid fields.
        """
        assert True


    def test_db_update_todo_invalid_field(self):
        """
        Test that db_update_todo does not apply the invalid fields
        and no update occurs.
        """
        assert True

    def test_db_update_todo_valid_and_invalid_field(self):
        """
        Test that db_update_todo updates only the valid fields
        and ignores the invalid ones.
        """
        assert True


# TODO add tests for all operation functions (read_all, update_todo, delete_todo)
# TODO add tests for new cli using the described proposed plan
