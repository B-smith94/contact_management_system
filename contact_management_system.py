import re
import os

print("Welcome to the Contact Management System!\nMenu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit")

contact_details = {}

def add_new_contact():
    pass

def edit_contact():
    pass

def delete_contact():
    pass

def search_contacts():
    pass

def display_contacts():
    pass

def export_contacts():
    pass

def import_contacts():
    pass

while True:
    menu_select = input("\nPlease enter the task you wish to perform from the menu list (example: Add a new contact): ")
    if menu_select.lower() == 'add a new contact':
        add_new_contact()
    elif menu_select.lower() == 'edit an existing contact':
        edit_contact()
    elif menu_select.lower() == 'delete a contact':
        delete_contact()
    elif menu_select.lower() == 'search for a contact':
        search_contacts()
    elif menu_select.lower() == 'display all contacts':
        display_contacts()
    elif menu_select.lower() == 'export contacts to a text file':
        export_contacts()
    elif menu_select.lower() == 'import contacts from a text file':
        import_contacts()
    elif menu_select.lower() == 'quit':
        confirm = input("Are you sure you would like to quit the program? (type yes or no): ")
        if confirm.lower() == 'yes':
            break
        else:
            continue
    else:
        print("Invalid input, please try again.")