""" Use this to delete all the records from the testtable. """

from pyodbc import connect

connection_string = (
    'DRIVER=SQLite3;'
    'DATABASE=joonasdb.db;'
)

conn = connect(connection_string)

cursor = conn.cursor()

cursor.execute("DELETE FROM testtable")
cursor.commit()

conn.close()
