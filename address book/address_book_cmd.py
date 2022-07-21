"""Address Book program using MySQL database, ver.1.0, Created by Dmitrii Sumenko, date: 7/12/2022"""

import mysql.connector

# need to change to real user name and password that you use in workbench(not root user)
connection = mysql.connector.connect(host="localhost", database="contacts", user="*****", password="*****")


def contact_lookup():
    search = input("Name to search for: ")
    search.lower().strip().title()
    my_list = search.split()
    new_list = [my_list[0].lower().title(), my_list[1].lower().title()]
    my_cursor = connection.cursor()
    data_query = "select * from contact_entries"
    my_cursor.execute(data_query)
    data = my_cursor.fetchall()
    print('{0:<6} {1:<14} {2:<14} {3:<18} {4:<18} {5:<20} {6:<20} {7:<14} {8:<8} {9:<8}'.format("ID", "First Name",
                                                                                                "Last Name",
                                                                                                "Work Phone",
                                                                                                "Cellphone", "E-mail",
                                                                                                "Address", "City",
                                                                                                "State", "Zip Code"))
    for line in data:
        if line[2] == new_list[0] and line[1] == new_list[1]:
            print('{0:<6} {1:<14} {2:<14} {3:<18} {4:<18} {5:<20} {6:<20} {7:<14} {8:<8} {9:<8}'.format(str(line[0]),
                                                                                                        str(line[2]),
                                                                                                        str(line[1]),
                                                                                                        str(line[3]),
                                                                                                        str(line[4]),
                                                                                                        str(line[5]),
                                                                                                        str(line[6]),
                                                                                                        str(line[7]),
                                                                                                        str(line[8]),
                                                                                                        str(line[9])))
    print(149 * "-")


def delete_by_id(id_number):
    delete_query = "DELETE from contact_entries where id = %s"
    cursor.execute(delete_query, (id_number,))
    connection.commit()


def update_by_id(first, last, work_number, cell, email, address, city, state, zip_code, user_id_2):
    my_cursor = connection.cursor()
    update_query = "UPDATE contact_entries SET f_name = %s, l_name = %s, work_number = %s, cellphone_number = %s," \
                   " email = %s, address = %s, city = %s, state = %s, zip = %s WHERE id = %s"
    my_data = (first, last, work_number, cell, email, address, city, state, zip_code, user_id_2)
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
    first_name = input("Enter first name: ").strip().title()
    last_name = input("Enter last name: ").strip().title()
    work = input("Enter work phone number(10 digits): ").strip()
    cell_phone = input("Enter cellphone number(10 digits): ").strip()
    email_1 = input("Enter email address: ").strip()
    address_1 = input("Enter address: ").strip().title()
    city_1 = input("Enter city: ").strip().title()
    state_1 = input("Enter state: ").strip().upper()
    zip_code_1 = input("Enter zip code: ").strip()

    my_cursor = connection.cursor()
    user_query = "INSERT INTO contact_entries (id, l_name, f_name, work_number, cellphone_number, email, address, " \
                 "city, state, zip) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
    data = (id_num, last_name, first_name, work, cell_phone, email_1, address_1, city_1, state_1, zip_code_1)
    my_cursor.execute(user_query, data)
    connection.commit()


entry = ''

while entry != "6":
    print(69 * " " + "MENU")
    print(149 * "-")
    print("1 - Display All")
    print("2 - Create a New Contact Entry")
    print("3 - Read a Contact Entry")
    print("4 - Update a Contact Entry")
    print("5 - Delete a Contact Entry")
    print("6 - EXIT")
    entry = input("Enter your choice: ")

    if entry == "1":  # Print all the contacts
        sql_select_Query = "select * from contact_entries"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("")
        print(
            '{0:<6} {1:<14} {2:<14} {3:<18} {4:<18} {5:<20} {6:<20} {7:<14} {8:<8} {9:<8}'.format("ID", "First Name",
                                                                                                  "Last Name",
                                                                                                  "Work Phone",
                                                                                                  "Cellphone",
                                                                                                  "E-mail", "Address",
                                                                                                  "City", "State",
                                                                                                  "Zip Code"))
        print(149 * "-")
        for row in records:
            print('{0:<6} {1:<14} {2:<14} {3:<18} {4:<18} {5:<20} {6:<20} {7:<14} {8:<8} {9:<8}'.format(str(row[0]),
                                                                                                        str(row[2]),
                                                                                                        str(row[1]),
                                                                                                        str(row[3]),
                                                                                                        str(row[4]),
                                                                                                        str(row[5]),
                                                                                                        str(row[6]),
                                                                                                        str(row[7]),
                                                                                                        str(row[8]),
                                                                                                        str(row[9])))
        print(149 * "-")

    if entry == "2":  # Create a new contact
        create()
        print("The contact was created.")

    if entry == "3":  # Read specific contact
        contact_lookup()

    if entry == "4":  # Update a contact
        contact_lookup()
        user_id = int(input("Enter id of user you want to update: "))
        sql_select_Query = "select * from contact_entries"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            if row[0] == user_id:
                first_2 = input("Enter first name: ").strip().title()
                last_2 = input("Enter last name: ").strip().title()
                work_2 = input("Enter work phone number(10 digits): ").strip()
                cell_2 = input("Enter cellphone number(10 digits): ").strip()
                email_2 = input("Enter email address: ").strip()
                address_2 = input("Enter address: ").strip().title()
                city_2 = input("Enter city: ").strip().title()
                state_2 = input("Enter state: ").strip().upper()
                zip_code_2 = input("Enter zip code: ").strip()
                update_by_id(first_2, last_2, work_2, cell_2, email_2, address_2, city_2, state_2, zip_code_2, user_id)
        print("Entry updated.")

    if entry == "5":  # Delete a contact
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
