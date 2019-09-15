import unittest
import os
from sqlite3 import OperationalError
from datetime import datetime

from dbhelper import CommunityDB


class TestDB(unittest.TestCase):

    def setUp(self):
        self.db = CommunityDB('test.sqlite')

    def tearDown(self):
        os.remove('test.sqlite')

    def test_insert_creates_table(self):
        with self.assertRaises(OperationalError):
            self.db.cursor.execute('SELECT * FROM subscribers')
        self.db.insert('rambler', 100)
        self.db.cursor.execute('SELECT * FROM subscribers')  # not raises

    def test_insert_generates_timestamp(self):
        self.db.insert('rambler', 100)
        row = self.db.cursor.execute('SELECT * FROM subscribers')
        *_, date = row.fetchone()
        self.assertTrue(isinstance(date, datetime))
