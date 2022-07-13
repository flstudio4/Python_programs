"""Address book program ver.1.0, with GUI and MySQL database, created by Dmitrii Sumenko, date: 7/13/2022"""

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

import mysql.connector

connection = mysql.connector.connect(host="localhost", database="contacts", user="user_name", password="password")


def update_contact_window():
    def cancel():
        contact_window.destroy()

    def refresh_tree_view():
        for my_row in tree.get_children():
            tree.delete(my_row)

        cursor = connection.cursor()
        my_data_query = "select * from contact_entries"
        cursor.execute(my_data_query)
        my_data = cursor.fetchall()
        for line in my_data:
            tree.insert('', 'end', values=(line[0], line[2], line[1], line[3]))

    def update_contact():
        count = 0
        current_id = 0
        first_n = ''
        last_n = ''
        selected_iid = tree.focus()
        index = tree.index(selected_iid) + 1

        first = first_name.get().strip().title()
        last = last_name.get().strip().title()
        cell = phone_number.get().strip()

        cursor = connection.cursor()
        my_data_query = "select * from contact_entries"
        cursor.execute(my_data_query)
        my_data = cursor.fetchall()
        for line in my_data:
            count += 1
            if count == index:
                first_n = line[2]
                last_n = line[1]
                current_id = line[0]
                print(first, last, cell)
        if first != "" and last != "" and cell != "":
            user_query = "UPDATE contact_entries SET f_name = %s, l_name = %s, cellphone_number = %s WHERE id = %s"
            my_data = (first, last, cell, current_id)
            cursor.execute(user_query, my_data)
            connection.commit()
            messagebox.showinfo("Updated Contact info", f"{first_n.upper()} {last_n.upper()} contact was successfully "
                                                        f"updated!")
            refresh_tree_view()
            cancel()
        elif first == "" or last == "" or cell == "":
            messagebox.showwarning("Warning", "Please enter values in all entry boxes")
            contact_window.focus()

    contact_window = Toplevel()
    contact_window.title("Update a contact")
    contact_window.geometry("300x180")
    contact_window.focus()
    contact_window.resizable(0, 0)
    contact_window.configure(bg="light gray")
    first_frame = Frame(contact_window, bg="light gray")
    first_frame.pack()
    second_frame = Frame(contact_window, bg="light gray")
    second_frame.pack()

    first_name = StringVar()
    last_name = StringVar()
    phone_number = StringVar()

    label_first_name = Label(first_frame, text="Enter First Name", bg="light gray")
    label_first_name.grid(column=0, row=0, padx=10, pady=10, sticky=W)
    entry_first_name = Entry(first_frame, textvariable=first_name)
    entry_first_name.grid(column=1, row=0, padx=10, pady=10)

    label_last_name = Label(first_frame, text="Enter Last Name", bg="light gray")
    label_last_name.grid(column=0, row=1, padx=10, pady=10, sticky=W)
    entry_last_name = Entry(first_frame, textvariable=last_name)
    entry_last_name.grid(column=1, row=1, padx=10, pady=10)

    label_phone = Label(first_frame, text="Enter Phone Number", bg="light gray")
    label_phone.grid(column=0, row=2, padx=10, pady=10, sticky=W)
    entry_phone = Entry(first_frame, textvariable=phone_number)
    entry_phone.grid(column=1, row=2, padx=10, pady=10)

    button_create_new = Button(second_frame, text="Update", command=update_contact)
    button_create_new.grid(row=0, column=0, padx=10, pady=10)
    button_cancel = Button(second_frame, text="Cancel", command=cancel)
    button_cancel.grid(row=0, column=1, padx=10, pady=10)


def create_new_contact_window():
    def refresh_tree_view():
        for my_row in tree.get_children():
            tree.delete(my_row)

        i_cursor = connection.cursor()
        my_data_query = 'SELECT id, f_name, l_name, cellphone_number from contact_entries'
        i_cursor.execute(my_data_query)
        my_data = i_cursor.fetchall()
        for line in my_data:
            tree.insert('', 'end', values=(line[0], line[2], line[1], line[3]))

    def create_id():
        cursor = connection.cursor()
        my_data_query = "select * from contact_entries"
        cursor.execute(my_data_query)
        my_data = cursor.fetchall()
        counter = 0
        for line in my_data:
            if counter < line[0]:
                counter = line[0]
        return counter + 1

    def create_new_contact():
        first = first_name.get().strip().title()
        last = last_name.get().strip().title()
        cell = phone_number.get().strip()
        cursor = connection.cursor()
        if first != "" and last != "" and cell != "":
            user_query = "INSERT INTO contact_entries (id, l_name, f_name, cellphone_number) VALUES (%s, %s, %s, %s)"
            my_data = (create_id(), first, last, cell)
            cursor.execute(user_query, my_data)
            connection.commit()
            messagebox.showinfo("New Contact info", f"{first.upper()} {last.upper()} contact was successfully created!")
            refresh_tree_view()
            cancel()
        elif first == "" or last == "" or cell == "":
            messagebox.showwarning("Warning", "Please enter values in all entry boxes")
            contact_window.focus()

    def cancel():
        contact_window.destroy()

    contact_window = Toplevel()
    contact_window.title("Create a new contact")
    contact_window.geometry("300x180")
    contact_window.focus()
    contact_window.resizable(0, 0)
    contact_window.configure(bg="light gray")
    first_frame = Frame(contact_window, bg="light gray")
    first_frame.pack()
    second_frame = Frame(contact_window, bg="light gray")
    second_frame.pack()

    first_name = StringVar()
    last_name = StringVar()
    phone_number = StringVar()

    label_first_name = Label(first_frame, text="Enter First Name", bg="light gray")
    label_first_name.grid(column=0, row=0, padx=10, pady=10, sticky=W)
    entry_first_name = Entry(first_frame, textvariable=first_name)
    entry_first_name.grid(column=1, row=0, padx=10, pady=10)

    label_last_name = Label(first_frame, text="Enter Last Name", bg="light gray")
    label_last_name.grid(column=0, row=1, padx=10, pady=10, sticky=W)
    entry_last_name = Entry(first_frame, textvariable=last_name)
    entry_last_name.grid(column=1, row=1, padx=10, pady=10)

    label_phone = Label(first_frame, text="Enter Phone Number", bg="light gray")
    label_phone.grid(column=0, row=2, padx=10, pady=10, sticky=W)
    entry_phone = Entry(first_frame, textvariable=phone_number)
    entry_phone.grid(column=1, row=2, padx=10, pady=10)

    button_create_new = Button(second_frame, text="Create", command=create_new_contact)
    button_create_new.grid(row=0, column=0, padx=10, pady=10)
    button_cancel = Button(second_frame, text="Cancel", command=cancel)
    button_cancel.grid(row=0, column=1, padx=10, pady=10)


def delete():
    first_name = ''
    last_name = ''
    current_id = 0
    count = 0
    selected_iid = tree.focus()
    index = tree.index(selected_iid) + 1
    cursor = connection.cursor()
    my_data_query = "select * from contact_entries"
    cursor.execute(my_data_query)
    my_data = cursor.fetchall()
    for line in my_data:
        count += 1
        if count == index:
            first_name = line[1]
            last_name = line[2]
            current_id = (line[0],)

    if messagebox.askyesno("Item for deletion", f"{first_name.upper()} {last_name.upper()} entry will be deleted, are "
                                                f"you sure?"):
        cursor.execute("DELETE FROM contact_entries WHERE id = %s", current_id)
        connection.commit()
        tree.delete(selected_iid)
        messagebox.showinfo("Info", f"{first_name.upper()} {last_name.upper()} entry was successfully deleted")


def update():
    update_contact_window()


window = Tk()
window.title("Address book")
window.config(bg='light gray')
window.resizable(0, 0)
upper_frame = Frame(window, bg='light gray')
upper_frame.grid(row=0, column=0, pady=10)
bottom_frame = Frame(window, bg='light gray')
bottom_frame.grid(row=1, column=0)
columns = ('id', 'First name', 'Last name', 'Phone')
tree = Treeview(upper_frame, column=columns, show='headings')
tree.heading('id', text='id')
tree.heading('First name', text='First Name')
tree.heading('Last name', text='Last Name')
tree.heading('Phone', text='Phone')
tree.column('id', width=50, anchor=CENTER)
tree.column('First name', width=100, anchor=W)
tree.column('Last name', width=100, anchor=W)
tree.column('Phone', width=100, anchor=CENTER)
tree.pack(padx=10, pady=10)

button_create = Button(bottom_frame, text="Create contact", command=create_new_contact_window)
button_create.grid(column=0, row=0, padx=10, pady=10)
button_delete = Button(bottom_frame, text="Delete contact", command=delete)
button_delete.grid(column=1, row=0, padx=10, pady=10)
button_update = Button(bottom_frame, text="Update contact", command=update)
button_update.grid(column=2, row=0, padx=10, pady=10)

my_cursor = connection.cursor()
data_query = 'SELECT id, f_name, l_name, cellphone_number from contact_entries'
my_cursor.execute(data_query)
data = my_cursor.fetchall()
for row in data:
    tree.insert('', 'end', values=(row[0], row[1], row[2], row[3]))

window.geometry("372x340")
window.mainloop()
