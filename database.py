import sqlite3
import os.path

class Database:
    """ Class to handle saving/gettting
        records for database
    """

    def __init__(self):
        self.conn = None
        self.db_file = '%s/.db_pytime' % os.path.expanduser('~')
        self._create_tables()

    def _create_tables(self):
        """ create tables
        """
        if not self._table_exists(name='activities'):
            cursor = self.conn.cursor()
            cursor.execute('''create table activities
             (id INTEGER PRIMARY KEY, 
              start TIMESTAMP, 
              end TIMESTAMP, 
              description text)''')
            self.conn.commit()
            cursor.close()
            self.conn.close()

    def _table_exists(self, name=''):
        """ test if table exists
        """
        exists = False
        self.open()
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT * FROM %s" % name)
            exists = True
        except:
            pass
        cursor.close()
        return exists

    def _run_query(self, query, values=()):
        """ Run database query returning the cursor object
        """
        self.open()
        cursor = self.conn.cursor()
        cursor.execute(query, values)
        return cursor

    def open(self):
        """ Open database file
        """
        self.conn = sqlite3.connect(self.db_file, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    
    def insert_record(self, obj):
        """ Insert a record into the database
        """
        values = (obj.start, obj.end, obj.description, )
        query = 'insert into activities values (NULL,?,?,?)'
        cursor = self._run_query(query, values)
        row_id = cursor.lastrowid
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return row_id

    def get_records(self):
        """ Return a list of records from the database
        """
        query = 'select * from activities'
        cursor = self._run_query(query)
        results = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return results
