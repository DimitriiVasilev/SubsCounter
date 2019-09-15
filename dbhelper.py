import sqlite3
from datetime import datetime


class CommunityDB:
    """Class for saving information about VK communities"""

    def __init__(self, db_filename: str):
        """Creates connector and cursor"""
        self.conn = sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_DECLTYPES)
        self.cursor = self.conn.cursor()

    def _create(self):
        """
        Creates table if needed.
        name - community name
        n_subs - number of subscribers
        date - when data was retrieved
        """
        query = '''
        CREATE TABLE IF NOT EXISTS subscribers 
        (name VARCHAR(50) NOT NULL,
        n_subs INTEGER NOT NULL,
        date TIMESTAMP NOT NULL)
        '''
        self.cursor.execute(query)

    def insert(self, name: str, n_subs: int, date: datetime = None):
        """
        Creates table if needed and insert data into it.
        If date was not provide uses current date.
        """
        self._create()  # if table does not exists

        if date is None:
            date = datetime.utcnow()
        query = 'INSERT INTO subscribers(name, n_subs, date) VALUES (?, ?, ?)'
        self.cursor.execute(query, (name, n_subs, date))
        self.conn.commit()
