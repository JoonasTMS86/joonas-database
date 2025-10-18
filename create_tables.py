""" Use this to create the tables for the local database. """

from pyodbc import connect

connection_string = (
    'DRIVER=SQLite3;'
    'DATABASE=joonasdb.db;'
)

conn = connect(connection_string)

cursor = conn.cursor()

"""
Tables
======

users
-----
id: int not null, unique ID for each user
firstname: varchar not null, first name of user
lastname: varchar not null, last name of user
birthdate: date not null, birthdate of user
role: int not null, role of the user which maps to the roles table
info: varchar, optional additional info

roles
-----
roleid: int not null, unique ID for the role
rolename: varchar not null, role description (CTO, Software Developer, Marketing, Human Resources)

"""

cursor.execute("CREATE TABLE users(" \
"id int not null," \
"firstname varchar(100) not null," \
"lastname varchar(100) not null," \
"birthdate date not null," \
"role int not null," \
"info varchar(512)" \
")")
cursor.commit()
cursor.execute("CREATE TABLE roles(" \
"roleid not null," \
"rolename varchar(255) not null" \
")")
cursor.commit()

conn.close()
