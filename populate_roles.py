""" Use this to pre-populate the roles table with example data. """

from pyodbc import connect

connection_string = (
    'DRIVER=SQLite3;'
    'DATABASE=joonasdb.db;'
)

conn = connect(connection_string)

cursor = conn.cursor()

cursor.execute("INSERT INTO roles VALUES" \
"(1, 'CTO')," \
"(2, 'CEO')," \
"(3, 'Software Developer')," \
"(4, 'Marketing')," \
"(5, 'HR')" \
)
cursor.commit()

conn.close()
