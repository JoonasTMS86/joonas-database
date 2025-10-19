import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pyodbc import connect

# Global variables
window = tk.Tk()
window.title("Joonas Database")
list_of_employees = Listbox(window, listvariable = "", height = 5)
col_users_id = []
col_users_firstname = []
col_users_lastname = []
col_users_birthdate = []
col_users_role = []
col_users_info = []
col_roles_roleid = []
col_roles_rolename = []

info = tk.Label(text = "Add a new employee with the \"Add\" button.\n" \
"View or edit the information of an employee with the \"View / Edit\" button.\n" \
"Delete a record with the \"Delete\" button.",
height = 9,
anchor = "w",
justify = "left")
info.grid(row = 0, column = 0)

list_of_employees.grid(row = 1, column = 0, sticky = "w")

def load_db_table_roles():
    col_roles_roleid.clear()
    col_roles_rolename.clear()
    connection_string = (
    'DRIVER=SQLite3;'
    'DATABASE=joonasdb.db;'
    )
    conn = connect(connection_string)
    cursor = conn.cursor()
    for row in cursor.execute('SELECT * FROM roles ORDER BY roleid'):
        col_roles_roleid.append(row[0])
        col_roles_rolename.append(row[1])
    conn.close()

def load_db_table_users():
    col_users_id.clear()
    col_users_firstname.clear()
    col_users_lastname.clear()
    col_users_birthdate.clear()
    col_users_role.clear()
    col_users_info.clear()
    connection_string = (
    'DRIVER=SQLite3;'
    'DATABASE=joonasdb.db;'
    )
    conn = connect(connection_string)
    cursor = conn.cursor()
    offset = 0
    for row in cursor.execute('SELECT * FROM users ORDER BY firstname, lastname'):
        list_of_employees.insert(offset, row[1] + " " + row[2])
        col_users_id.append(row[0])
        col_users_firstname.append(row[1])
        col_users_lastname.append(row[2])
        col_users_birthdate.append(row[3])
        col_users_role.append(row[4])
        col_users_info.append(row[5])
        offset = offset + 1
    conn.close()

def must_be_digit(character):
    char_as_int = ord(character)
    if char_as_int >= 48 and char_as_int <= 57:
        return True
    return False

def must_be_dash(character):
    char_as_int = ord(character)
    if char_as_int == 45:
        return True
    return False

def validate(firstname, lastname, birthdate):
    if firstname == "":
        messagebox.showerror(title = "Error", message = "First name may not be blank.")
        return False
    if lastname == "":
        messagebox.showerror(title = "Error", message = "Last name may not be blank.")
        return False
    if birthdate == "":
        messagebox.showerror(title = "Error", message = "Birthdate may not be blank.")
        return False
    valid_dob = False
    if len(birthdate) == 10:
        c0 = must_be_digit(birthdate[0])
        c1 = must_be_digit(birthdate[1])
        c2 = must_be_digit(birthdate[2])
        c3 = must_be_digit(birthdate[3])
        c4 = must_be_dash(birthdate[4])
        c5 = must_be_digit(birthdate[5])
        c6 = must_be_digit(birthdate[6])
        c7 = must_be_dash(birthdate[7])
        c8 = must_be_digit(birthdate[8])
        c9 = must_be_digit(birthdate[9])
        if c0 and c1 and c2 and c3 and c4 and c5 and c6 and c7 and c8 and c9:
            valid_dob = True
    if valid_dob == False:
        messagebox.showerror(title = "Error", message = "Invalid birthdate. Please use the format YYYY-MM-DD, eg. 2000-01-01.")
        return False
    return True

def open_add_or_edit_user_window(which_one):
    index_of_selected_row_of_employees = 0
    roleid_of_selected_user = 0
    if which_one == 1:
        index_of_selected_row_of_employees = list_of_employees.curselection()[0]

    firstname = ""
    lastname = ""
    birthdate = ""
    infoText = ""
    rolename = col_roles_rolename[0]
    add_or_edit_user_window = Tk()
    add_or_edit_user_window_container = ttk.Frame(add_or_edit_user_window, padding=(5, 5, 12, 0))
    add_or_edit_user_window_container.grid(column = 0, row = 0, sticky = (N, W, E, S))
    add_or_edit_user_window.grid_columnconfigure(3, weight = 1)
    add_or_edit_user_window.grid_rowconfigure(8,weight = 1)
    add_or_edit_user_window.geometry("450x225-655+290")

    def okButton(*args):
        valid = validate(firstnameBox.get(), lastnameBox.get(), birthdateBox.get())
        if valid:
            personInfo = infoBox.get("1.0", END)
            personInfo = personInfo[:-1]
            connection_string = (
            'DRIVER=SQLite3;'
            'DATABASE=joonasdb.db;'
            )
            conn = connect(connection_string)
            cursor = conn.cursor()
            if which_one == 0:
                df_users = pd.DataFrame(col_users_id)
                new_id = df_users.max()[0] + 1
                cursor.execute("INSERT INTO users VALUES(" \
                + str(new_id) + ", " \
                "'" + firstnameBox.get() + "', " \
                "'" + lastnameBox.get() + "', " \
                "'" + birthdateBox.get() + "', " \
                + str(col_roles_roleid[roleBox.current()]) + ", " \
                "'" + personInfo + "')")
            else:
                cursor.execute("UPDATE users SET " \
                "firstname = '" + firstnameBox.get() + "', " \
                "lastname = '" + lastnameBox.get() + "', " \
                "birthdate = '" + birthdateBox.get() + "', " \
                "role = " + str(col_roles_roleid[roleBox.current()]) + ", " \
                "info = '" + personInfo + "'" \
                " WHERE id = " + str(col_users_id[index_of_selected_row_of_employees]))
            cursor.commit()
            conn.close()
            list_of_employees.delete(0, (list_of_employees.size() - 1))
            load_db_table_users()
            add_or_edit_user_window.destroy()

    if which_one == 0:
        add_or_edit_user_window.title("Add New Entry")
    else:
        add_or_edit_user_window.title("Edit Entry")
        firstname = col_users_firstname[index_of_selected_row_of_employees]
        lastname = col_users_lastname[index_of_selected_row_of_employees]
        birthdate = col_users_birthdate[index_of_selected_row_of_employees]
        roleid_of_selected_user = col_users_role[index_of_selected_row_of_employees]
        rowindex = 0
        for row in col_roles_roleid:
            if row == roleid_of_selected_user:
                rolename = col_roles_rolename[rowindex]
            rowindex = rowindex + 1
        infoText = col_users_info[index_of_selected_row_of_employees]
        if infoText == None:
            infoText = ""

    tx1 = ttk.Label(add_or_edit_user_window_container, text = "First Name")
    tx1.grid(column = 0, row = 0, columnspan = 1, sticky = (N, W))
    firstnameBox = ttk.Entry(add_or_edit_user_window_container)
    firstnameBox.insert(0, firstname)
    firstnameBox.grid(column = 1, row = 0, columnspan = 1, sticky = (N, W))

    tx2 = ttk.Label(add_or_edit_user_window_container, text = "Last Name")
    tx2.grid(column = 0, row = 1, columnspan = 1, sticky = (N, W))
    lastnameBox = ttk.Entry(add_or_edit_user_window_container)
    lastnameBox.insert(0, lastname)
    lastnameBox.grid(column = 1, row = 1, columnspan = 1, sticky = (N, W))

    tx3 = ttk.Label(add_or_edit_user_window_container, text = "Birthdate (as YYYY-MM-DD)")
    tx3.grid(column = 0, row = 2, columnspan = 1, sticky = (N, W))
    birthdateBox = ttk.Entry(add_or_edit_user_window_container)
    birthdateBox.insert(0, birthdate)
    birthdateBox.grid(column = 1, row = 2, columnspan = 1, sticky = (N, W))

    tx4 = ttk.Label(add_or_edit_user_window_container, text = "Role")
    tx4.grid(column = 0, row = 3, columnspan = 1, sticky = (N, W))
    roleBox = ttk.Combobox(add_or_edit_user_window_container, values = col_roles_rolename, state = 'readonly')
    roleBox.grid(column = 1, row = 3, columnspan = 1, sticky = (N, W))
    roleBox.set(rolename)

    tx5 = ttk.Label(add_or_edit_user_window_container, text = "Additional Info")
    tx5.grid(column = 0, row = 4, columnspan = 1, sticky = (N, W))
    infoBox = tk.Text(add_or_edit_user_window_container, height = 6, width = 30)
    infoBox.insert(END, infoText)
    infoBox.grid(column = 1, row = 4, columnspan = 1, sticky = (N, W))

    ok_button = ttk.Button(add_or_edit_user_window_container, text = "OK", command = okButton, default = "active")
    ok_button.grid(column = 0, row = 5, sticky = "w")

def addButton(*args):
    open_add_or_edit_user_window(0)
def editButton(*args):
    if len(list_of_employees.curselection()) > 0:
        open_add_or_edit_user_window(1)

def deleteButton(*args):
    if len(list_of_employees.curselection()) > 0:
        index_of_selected_row_of_employees = list_of_employees.curselection()[0]
        user_id = col_users_id[index_of_selected_row_of_employees]
        selection = messagebox.askokcancel('Remove Entry', 'Are you sure?')
        if selection == True:
            connection_string = (
            'DRIVER=SQLite3;'
            'DATABASE=joonasdb.db;'
            )
            conn = connect(connection_string)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = " + str(user_id))
            cursor.commit()
            conn.close()
            list_of_employees.delete(0, (list_of_employees.size() - 1))
            load_db_table_users()

load_db_table_roles()
load_db_table_users()

add_button = ttk.Button(window, text = "Add", command = addButton, default = "active")
add_button.grid(row = 2, column = 0, sticky = "w")
edit_button = ttk.Button(window, text = "View / Edit", command = editButton, default = "active")
edit_button.grid(row = 3, column = 0, sticky = "w")
delete_button = ttk.Button(window, text = "Delete", command = deleteButton, default = "active")
delete_button.grid(row = 4, column = 0, sticky = "w")

window.mainloop()
