""" Use this to display all the rows of the tables. """

from pyodbc import connect

# Use mode 0 to simply view the tables. Use a non-0 value to view the users table the way it is presented in the actual app.
mode = 1

connection_string = (
    'DRIVER=SQLite3;'
    'DATABASE=joonasdb.db;'
)

conn = connect(connection_string)

cursor = conn.cursor()

if mode == 0:
    print("users table:")
    for row in cursor.execute('SELECT * FROM users'):
      print(row)
    print("roles table:")
    for row in cursor.execute('SELECT * FROM roles'):
      print(row)
else:
    for row in cursor.execute('SELECT users.id, users.firstname, users.lastname, users.birthdate, roles.rolename, users.info FROM users, roles WHERE roles.roleid = users.role ORDER BY users.id'):
      print(str(row[0]) + ", " + row[1] + ", " + row[2] + ", " + str(row[3]) + ", " + row[4] + ", " + str(row[5]))

conn.close()
