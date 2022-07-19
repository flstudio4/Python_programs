"""Address Book program using MySQL database, ver.1.0, Created by Dmitrii Sumenko, date: 7/12/2022"""

import mysql.connector

# need to change to real user name and password that you use in workbench(not root user)
connection = mysql.connector.connect(host="localhost", database="contacts", user="flstudio4", password="Dimka1985!")


def contact_lookup():
    search = input("Name to search for: ")
    search.lower().strip().title()
    my_list = search.split()
    new_list = [my_list[0].lower().title(), my_list[1].lower().title()]
    my_cursor = connection.cursor()
    data_query = "select * from contact_entries"
    my_cursor.execute(data_query)
    data = my_cursor.fetchall()
    print('{0:<6} {1:<14} {2:<14} {3:<14}'.format("ID", "First Name", "Last Name", "Phone"))
    for line in data:
        if line[2] == new_list[0] and line[1] == new_list[1]:
            print('{0:<6} {1:<14} {2:<14} {3:<14}'.format(str(line[0]), str(line[2]), str(line[1]), str(line[4])))
    print(47 * "-")


def delete_by_id(id_number):
    delete_query = "DELETE from contact_entries where id = %s"
    cursor.execute(delete_query, (id_number,))
    connection.commit()


def update_by_id(first, last, phone, id_num):
    my_cursor = connection.cursor()
    update_query = "UPDATE contact_entries SET f_name = %s, l_name = %s, cellphone_number = %s WHERE id = %s"
    my_data = (first, last, phone, id_num)
    my_cursor.execute(update_query, my_data)
    connection.commit()


def create_id():
    my_cursor = connection.cursor()
    my_data_query = "select * from contact_entries"
    my_cursor.execute(my_data_query)
    my_data = cursor.fetchall()
    counter = 0
    for line in my_data:
        if counter < line[0]:
            counter = line[0]
    return counter + 1


def create():
    id_num = create_id()
    first = input("Enter first name: ").strip().title()
    last = input("Enter last name: ").strip().title()
    cell = input("Enter cellphone number: ").strip().title()
    my_cursor = connection.cursor()
    user_query = "INSERT INTO contact_entries (id, l_name, f_name, cellphone_number) VALUES (%s, %s, %s, %s)"
    data = (id_num, last, first, cell)
    my_cursor.execute(user_query, data)
    connection.commit()


entry = ''

while entry != "6":
    print(22 * " " + "MENU")
    print(47 * "-")
    print("1 - Display All")
    print("2 - Create a New Contact Entry")
    print("3 - Read a Contact Entry")
    print("4 - Update a Contact Entry")
    print("5 - Delete a Contact Entry")
    print("6 - EXIT")
    entry = input("Enter your choice: ")

    if entry == "1":    # Print all the contacts
        sql_select_Query = "select * from contact_entries"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("")
        print('{0:<6} {1:<14} {2:<14} {3:<14}'.format("ID", "First Name", "Last Name", "Phone"))
        print(47 * "-")
        for row in records:
            print('{0:<6} {1:<14} {2:<14} {3:<14}'.format(str(row[0]), str(row[2]), str(row[1]), str(row[4])))
        print(47 * "-")

    if entry == "2":    # Create a new contact
        create()
        print("The contact was created.")

    if entry == "3":    # Read specific contact
        contact_lookup()

    if entry == "4":    # Update a contact
        contact_lookup()
        user_id = int(input("Enter id of user you want to update: "))
        sql_select_Query = "select * from contact_entries"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            if row[0] == user_id:
                first_name = input("Enter first name: ").strip().title()
                last_name = input("Enter last name: ").strip().title()
                cell_phone = input("Enter cellphone number: ").strip().title()
                update_by_id(first_name, last_name, cell_phone, user_id)
        print("Entry updated.")

    if entry == "5":    # Delete a contact
        contact_lookup()
        user_id = int(input("Enter id of user you want to delete: "))
        sql_select_Query = "select * from contact_entries"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            if row[0] == user_id:
                delete_by_id(user_id)
        print("Entry deleted.")

connection.close()
