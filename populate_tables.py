""" Use this to pre-populate the tables with example data. """

from pyodbc import connect

connection_string = (
    'DRIVER=SQLite3;'
    'DATABASE=joonasdb.db;'
)

conn = connect(connection_string)

cursor = conn.cursor()

cursor.execute("INSERT INTO users VALUES" \
"(1, 'Joonas', 'Lindberg', '1986-10-17', 0, null)," \
"(2, 'Some', 'Guy', '1990-01-01', 2, null)," \
"(3, 'Somebody', 'Someone', '1994-03-06', 3, null)," \
"(4, 'Abc', 'Def', '1998-06-09', 4, null)," \
"(5, 'Ghi', 'Jkl', '2002-09-12', 3, null)" \
)
cursor.commit()
cursor.execute("INSERT INTO roles VALUES" \
"(0, 'CTO')," \
"(1, 'CEO')," \
"(2, 'Software Developer')," \
"(3, 'Marketing')," \
"(4, 'HR')" \
)
cursor.commit()

conn.close()
