""" Use this to pre-populate the roles table with example data. """

from pyodbc import connect

connection_string = (
    'DRIVER=SQLite3;'
    'DATABASE=joonasdb.db;'
)

conn = connect(connection_string)

cursor = conn.cursor()

cursor.execute("INSERT INTO roles VALUES" \
"(0, 'CTO')," \
"(1, 'CEO')," \
"(2, 'Software Developer')," \
"(3, 'Marketing')," \
"(4, 'HR')" \
)
cursor.commit()

conn.close()
