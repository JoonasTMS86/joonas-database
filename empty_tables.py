""" Use this to empty the tables. """

from pyodbc import connect

connection_string = (
    'DRIVER=SQLite3;'
    'DATABASE=joonasdb.db;'
)

conn = connect(connection_string)

cursor = conn.cursor()

cursor.execute("DELETE FROM users")
cursor.commit()
cursor.execute("DELETE FROM roles")
cursor.commit()

conn.close()
