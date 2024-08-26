import re

contact_details = {}

def add_new_contact(contact_dict):
    first_name = input("Please enter the contact's first name: ")
    last_name = input("Please enter the contact's last name: ")
    full_name = first_name.capitalize() + " " + last_name.capitalize()
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
    contact_dict[full_name] = {'Name': full_name, 'Home/Cell': home_or_cell, 'Email': email, 'Home Address': address, 'Work Phone': work_phone}
    print("Contact successfully added!")
    while True:
        add_more_detail = input("Would you like to add any other details? (yes/no): ")
        if add_more_detail.lower() == 'yes':
            new_category = input("Please enter the category you wish to add (ex: birthday): ")
            new_info = input(f"Please enter the information for {new_category}: ")
            contact_dict[full_name][new_category.title()] = new_info
            continue
        elif add_more_detail.lower()!= 'yes':
            if add_more_detail.lower() == 'no':
                break
            else:
                print("Invalid input, please try again")
                continue

def edit_contact(contact_dict):
    contact = input("Please input the full name of the contact you wish to edit: ")
    if contact.title() in contact_dict:
        category = input("Please input the info category you wish to change (example: Name) ")
        new_info = input("Please input the updated info: ")
        contact_dict[contact.title()][category.title()] = new_info
        print("Contact successfully edited!")
    else:
        print("Contact not found.")
            
def delete_contact(contact_dict):
    contact = input('Please provide the name of the contact you wish to delete (type the name as it appears in the contact list): ')
    try:
        contact_dict.pop(contact_dict[contact.title()])
        print("Contact deleted.")
    except KeyError:
        print("Contact not found.")

def search_contacts(contact_dict):
    contact = input("Please enter the full name of the contact you are trying to find as it appears in the contact list: ")
    if contact in contact_dict:
        print(f"\nContact: {contact_dict[contact]}")
    else:
        print("Contact not found.\n")

def display_contacts(contact_dict):
    for contact, details in contact_dict.items():
        print(f"Contact: {contact}")
        for category, info in details.items():
            print(f"    {category}: {info}")

def export_contacts(contact_dict):
    with open('contact_list.txt', 'w') as file:
        for contact, details in contact_dict.items():
            file.write(f"{contact}:\n")
            for category, info in details.items():
                file.write(f"   {category}: {info}\n")
    print("\nContacts Exported!")

def sort_contacts(contact_dict):
    category = input("Please enter how you would like the contacts sorted (Name, Phone, Email, Address, Work Phone Number, or any added categories): ")
    sorted_contacts = sorted(contact_dict, key=lambda x: x[1][category])
    print(sorted_contacts)
            
while True:
    print("\nWelcome to the Contact Management System!\nMenu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Sort Contacts\n8. Quit")
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
    elif menu_select.lower() == 'sort contacts':
        sort_contacts(contact_details)
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