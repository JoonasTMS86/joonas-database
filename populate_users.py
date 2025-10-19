""" Use this to pre-populate the users table with example data. """

from pyodbc import connect

connection_string = (
    'DRIVER=SQLite3;'
    'DATABASE=joonasdb.db;'
)

conn = connect(connection_string)

cursor = conn.cursor()

cursor.execute("INSERT INTO users VALUES" \
"(1, 'Joonas', 'Lindberg', '1986-10-17', 1, 'The founder of our company.')," \
"(2, 'Some', 'Guy', '1990-01-01', 3, 'Our first hire.')," \
"(3, 'Somebody', 'Someone', '1994-03-06', 4, null)," \
"(4, 'Abc', 'Def', '1998-06-09', 5, null)," \
"(5, 'Ghi', 'Jkl', '2002-09-12', 4, null)" \
)
cursor.commit()

conn.close()
