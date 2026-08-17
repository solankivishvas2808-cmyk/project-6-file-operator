from datetime import datetime

filename = "journal.txt"

while True:

    print("\n==============================")
    print("Personal Journal Manager")
    print("==============================")
    print("1. Add New Entry")
    print("2. View All Entries")
    print("3. Search Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Entry
    if choice == "1":

        try:
            entry = input("Enter your journal entry: ")

            if entry == "":
                print("Entry cannot be empty.")
            else:
                date_time = datetime.now()

                file = open(filename, "a")

                file.write("Date: ")
                file.write(str(date_time))
                file.write("\n")

                file.write("Entry: ")
                file.write(entry)
                file.write("\n")

                file.write("------------------------------\n")

                file.close()

                print("Entry added successfully.")

        except PermissionError:
            print("Permission denied.")

        except OSError:
            print("Error while accessing file.")

    # View Entries
    elif choice == "2":

        try:
            file = open(filename, "r")

            data = file.read()

            file.close()

            if data == "":
                print("No journal entries found.")
            else:
                print("\nYour Journal Entries:")
                print("------------------------------")
                print(data)

        except FileNotFoundError:
            print("Journal file does not exist.")

        except PermissionError:
            print("Permission denied.")

    # Search Entry
    elif choice == "3":

        try:
            keyword = input("Enter keyword to search: ")

            file = open(filename, "r")

            data = file.read()

            file.close()

            if keyword.lower() in data.lower():
                print("\nEntry found.")
                print("------------------------------")

                lines = data.split("\n")

                for line in lines:
                    if keyword.lower() in line.lower():
                        print(line)

            else:
                print("Entry not found.")

        except FileNotFoundError:
            print("Journal file does not exist.")

        except PermissionError:
            print("Permission denied.")

    # Delete Entries
    elif choice == "4":

        try:
            confirmation = input(
                "Are you sure you want to delete all entries? (yes/no): "
            )

            if confirmation.lower() == "yes":

                file = open(filename, "w")
                file.write("")
                file.close()

                print("All entries deleted successfully.")

            elif confirmation.lower() == "no":
                print("Delete operation cancelled.")

            else:
                print("Please enter yes or no.")

        except PermissionError:
            print("Permission denied.")

    # Exit
    elif choice == "5":

        print("Thank you for using Personal Journal Manager.")
        break

    else:
        print("Invalid choice.")


"""
==============================
Personal Journal Manager
==============================
1. Add New Entry
2. View All Entries
3. Search Entry
4. Delete All Entries
5. Exit
Enter your choice: 1
Enter your journal entry: today i learned python file handling.
Entry added successfully.

==============================
Personal Journal Manager
==============================
1. Add New Entry
2. View All Entries
3. Search Entry
4. Delete All Entries
5. Exit
Enter your choice: 2

Your Journal Entries:
------------------------------
Date: 2026-08-13 14:08:47.832615
Entry: today i learned python file handling.
------------------------------


==============================
Personal Journal Manager
==============================
1. Add New Entry
2. View All Entries
3. Search Entry
4. Delete All Entries
5. Exit
Enter your choice: 3
Enter keyword to search: today i learned python file handling.

Entry found.
------------------------------
Entry: today i learned python file handling.

==============================
Personal Journal Manager
==============================
1. Add New Entry
2. View All Entries
3. Search Entry
4. Delete All Entries
5. Exit
Enter your choice: 4
Are you sure you want to delete all entries? (yes/no): yes
All entries deleted successfully.

==============================
Personal Journal Manager
==============================
1. Add New Entry
2. View All Entries
3. Search Entry
4. Delete All Entries
5. Exit
Enter your choice: 5
Thank you for using Personal Journal Manager.
"""
