import re
import os

print("Welcome to the Contact Management System!\nMenu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit")

contact_details = {}

def add_new_contact(contact_dict):
    best_phone_num = input("Please enter the best phone number to reach the new contact: (ex: 123-456-7890): ")
    name = input("What is the name of the contact you wish to add? ")
    home_or_cell = input(f"Please enter {name}'s phone home or phone number (ex: 123-456-7890): ")
    email = input(f"Please enter {name}'s email: ")
    address = input(f"Please enter {name}'s address (enter 'none' if address unknown): ")
    work_phone = input(f"Please enter {name}'s work phone number (example: 123-456-7890)(enter 'none' if unknown): ")
    contact_dict.append(best_phone_num, {})
    contact_dict[best_phone_num].setdefault('Name', name)
    contact_dict[best_phone_num].setdefault('Home/Cell', home_or_cell)
    contact_dict[best_phone_num].setdefault('Email', email)
    contact_dict[best_phone_num].setdefault('Address', address)
    contact_dict[best_phone_num].setdefault('Work Phone', work_phone)
    print(contact_dict)

def edit_contact(contact_dict):
    pass

def delete_contact(contact_dict):
    pass

def search_contacts(contact_dict):
    pass

def display_contacts(contact_dict):
    pass

def export_contacts(contact_dict):
    with open('contact_list.txt', 'w') as file:
        for contact, info in contact_dict.items():
            file.write(f"{contact}: {info}")
            for item, details in info.items():
                file.write(f"{item}: {details}")
        print("Contacts exported.")

def import_contacts(contact_dict):
    pass

while True:
    menu_select = input("\nPlease enter the task you wish to perform from the menu list (example: Add a new contact): ")
    if menu_select.lower() == 'add a new contact':
        add_new_contact(contact_details)
    elif menu_select.lower() == 'edit an existing contact':
        edit_contact(contact_details)
    elif menu_select.lower() == 'delete a contact':
        delete_contact(contact_details)
    elif menu_select.lower() == 'search for a contact':
        search_contacts(contact_details)
    elif menu_select.lower() == 'display all contacts':
        display_contacts(contact_details)
    elif menu_select.lower() == 'export contacts to a text file':
        export_contacts(contact_details)
    elif menu_select.lower() == 'import contacts from a text file':
        import_contacts(contact_details)
    elif menu_select.lower() == 'quit':
        confirm = input("Are you sure you would like to quit the program? (type yes or no): ")
        if confirm.lower() == 'yes':
            break
        else:
            continue
    else:
        print("Invalid input, please try again.")