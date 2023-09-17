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
