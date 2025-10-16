""" Use this to display all the rows of the testtable. """

from pyodbc import connect

connection_string = (
    'DRIVER=SQLite3;'
    'DATABASE=joonasdb.db;'
)

conn = connect(connection_string)

cursor = conn.cursor()

for row in cursor.execute('SELECT * FROM testtable'):
  print(row)

conn.close()
