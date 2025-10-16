""" Use this to populate the testtable. """

from pyodbc import connect

connection_string = (
    'DRIVER=SQLite3;'
    'DATABASE=joonasdb.db;'
)

conn = connect(connection_string)

cursor = conn.cursor()

cursor.execute("INSERT INTO testtable VALUES(1, 'Joonas')")
cursor.commit()

conn.close()
