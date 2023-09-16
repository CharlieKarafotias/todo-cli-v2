from unittest import TestCase
from src.database.initializer import init_db, remove_db
from src.database.operations import *


class Test(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._conn = init_db('test_db_operations')

    @classmethod
    def tearDownClass(cls) -> None:
        remove_db('test_db_operations')

    def test_db_create_todo_valid_fields(self):
        fields = {
            'todo_name': 'test',
            'description': 'this is a test todo',
            'priority': 'medium'
        }
        db_create_todo(self._conn, fields)
        res = db_read_todo(self._conn, '1')
        self.assertEqual(res[0], 1)  # check id
        self.assertEqual(res[1], fields['todo_name'])  # check todo_name
        self.assertEqual(res[2], fields['description'])  # check description
        self.assertEqual(res[3], fields['priority'])  # check priority
