""" Use this to create a test table named testtable into joonasdb.db. """

from pyodbc import connect

connection_string = (
    'DRIVER=SQLite3;'
    'DATABASE=joonasdb.db;'
)

conn = connect(connection_string)

cursor = conn.cursor()

cursor.execute("CREATE TABLE testtable(id int, name varchar(255))")
cursor.commit()

conn.close()
