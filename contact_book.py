import sqlite3

db = sqlite3.connect('contactsdb')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS info (contact_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
               "name TEXT UNIQUE, email TEXT, phone TEXT, address TEXT)")
db.commit()


def create_contact():

    name = input("Name: ")
    if name:
        cursor.execute("SELECT * FROM info WHERE name = ?", (name,))
        data = cursor.fetchall()
        if len(data) == 1:
            print("Contact already exists!")
            name = input("Name: ")

    email = input("Email: ")
    phone = input("Phone: ")
    address = input("Address: ")


    cursor.execute("INSERT INTO info (name, phone, email, address) VALUES (?,?,?,?)", (name, email, phone, address))
    db.commit()
    print(f"{name} has been successfully added to contacts!")


def update_contact():
    column = 0
    name = input("Name: ")
    if name:
        cursor.execute("SELECT * FROM info WHERE name = ?", (name,))
        data = cursor.fetchall()
        print(len(data))
        if len(data) == 0:
            print("This contact does not exist!")
            name = input("Name: ")

    selection = int(input("What record do you want to update?\n"
                          "[1] Name\n "
                          "[2] Email\n "
                          "[3] Phone\n "
                          "[4] Address?"))

    if selection == 1:
        column = "name"
    if selection == 2:
        column = "email"
    if selection == 3:
        column = "phone"
    if selection == 4:
        column = "address"
    else:
        print("Enter a number between 1 - 4")

    updated_record = input(f"What do you want to change {column} to? : ")


    cursor.execute("UPDATE info SET {} =? WHERE name = ?".format(column), (updated_record, name))
    db.commit()

    print(f"{name} contact {column} has been successfully updated to {updated_record}!")


def find_contact():
    name = input("Whose contact details do you want to find?")
    cursor.execute("SELECT * FROM info where name = ?", (name,))
    data = cursor.fetchone()
    print("----------------------")
    print(f"{name.upper()}'S CONTACT DETAILS")
    print("----------------------")
    print(f" Name: {data[1]}\n Phone Number: {data[2]}\n Email: {data[3]}\n Address: {data[4]}")
    print("----------------------")


def list_contacts():
    cursor.execute('SELECT * FROM info')
    data = cursor.fetchall()
    db.commit()

    for i in data:
        print("----------------------")
        print(f"{i[1].upper()}'S CONTACT DETAILS")
        print("----------------------")
        print(f" Name: {i[1]}\n Phone Number: {i[2]}\n Email: {i[3]}\n Address: {i[4]}")
        print()


def delete_contact():
    name = input("Whose contact do you want to delete?")
    cursor.execute("DELETE FROM info WHERE name = ?", [name])
    db.commit()

    print(f"{name}'s contact has been deleted!")


def run():
    while True:
        print("===== Contact Book ===== \n"
              "[1] Create a new contact \n"
              "[2] Update a contact \n"
              "[3] Find a contact \n"
              "[4] List all saved contact \n"
              "[5] Delete a contact \n"
              "========================="
              )
        option = int(input("Enter an option: "))

        while 0 < option < 6:
            if option == 1:
                create_contact()
                break

            elif option == 2:
                update_contact()
                break

            elif option == 3:
                find_contact()
                break

            elif option == 4:
                list_contacts()
                break

            elif option == 5:
                delete_contact()
                break


if __name__ == "__main__":
    run()
