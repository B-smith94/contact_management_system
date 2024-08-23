import re
import os

contact_details = {}

def add_new_contact(contact_dict):
    first_name = input("Please enter the contact's first name: ")
    last_name = input("Please enter the contact's last name: ")
    full_name = first_name + " " + last_name
    while True:    
        home_or_cell = input(f"Please enter {full_name}'s phone home or phone number (ex: 123-456-7890): ")
        phone_format = re.search(r"\d{3}-\d{3}-\d{4}", home_or_cell)
        if phone_format:
            print("Number successfully added.")
            break
        else:
            print("Invalid input, please use this format: 123-456-7890")
            continue
    while True:
        email = input(f"Please enter {full_name}'s email (enter 'none' if unknown): ")
        email_format = re.search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z|A-Z]{2,}', email)
        if email.lower() == 'none':
            break
        else:
            if email_format:
                print("Email successfully added.")
                break
            else:
                print("Invalid format, please try again.")
                continue
    while True:
        address = input(f"Please enter {full_name}'s address (enter 'none' if address unknown): ")
        if address.lower()=='none':
            break
        else:
            address_format=re.search(r"\w+(\s\w+){2,}", address)
            if address_format:
                print("Address successfully added.")
                break
            else:
                print("Invalid input, please use this format: 123 Example Road/Rd. City, State")
                continue
    while True:
        work_phone = input(f"Please enter {full_name}'s work phone number (example: 123-456-7890)(enter 'none' if unknown): ")
        if work_phone.lower()=='none':
            break
        else:
            phone_format = re.search(r"\d{3}-\d{3}-\d{4}", work_phone)
            if phone_format:
                print("Work phone successfully added.")
                break
            else:
                print("Invalid format, please use this format: 123-456-7890")
                continue
    contact_dict[full_name] = {'Name': full_name, 'Home/Cell': home_or_cell, 'Email Address': email, 'Home Address': address, 'Work Phone Number': work_phone}
    print("Contact successfully added!")

def edit_contact(contact_dict):
    pass

def delete_contact(contact_dict):
    pass

def search_contacts(contact_dict):
    pass

def display_contacts(contact_dict):
    for contact, details in contact_dict.items():
        print(f"Contact: {contact}")
        for category, info in details.items():
            print(f"    {category}: {info}")

def export_contacts(contact_dict):
    with open('contact_list.txt', 'w') as file:
        for contact, info in contact_dict.items():
            file.write(f"{contact}: {info}, ")
            for item, details in info.items():
                file.write(f"{item}: {details}")
        print("Contacts exported.")

def import_contacts(contact_dict):
    with open('contact_list.txt', 'r') as file:
        for line in file:
            match = re.match(r'\s*([^:]+)\s*:\s*(.+)\s*', line)
            if match:
                contact, item = match.groups()
                if ',' in item:
                    contact_dict[contact] = item.split(',')
                else:
                    contact_dict[contact] = item
    print(contact_dict)

while True:
    print("Welcome to the Contact Management System!\nMenu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit")
    menu_select = input("\nPlease enter the task you wish to perform from the menu list (example: Add a new contact): ")
    if menu_select.lower() == 'add a new contact':
        add_new_contact(contact_details)
        continue
    elif menu_select.lower() == 'edit an existing contact':
        edit_contact(contact_details)
        continue
    elif menu_select.lower() == 'delete a contact':
        delete_contact(contact_details)
        continue
    elif menu_select.lower() == 'search for a contact':
        search_contacts(contact_details)
        continue
    elif menu_select.lower() == 'display all contacts':
        display_contacts(contact_details)
        continue
    elif menu_select.lower() == 'export contacts to a text file':
        export_contacts(contact_details)
        continue
    elif menu_select.lower() == 'import contacts from a text file':
        import_contacts(contact_details)
        continue
    elif menu_select.lower() == 'quit':
        confirm = input("Are you sure you would like to quit the program? (type yes or no): ")
        if confirm.lower() == 'yes':
            print("Have a nice day!")
            break
        else:
            continue
    else:
        print("Invalid input, please try again.")
        continue