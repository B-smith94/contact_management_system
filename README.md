# Contact Management System #

Author: Byron Smith

Date: 8/26/24

## Instructions ##

Welcome to the Contact Management System! Below are the instructions on how to use the program.

### Table of Contents ###

1.  Walk Through the Menu
2.  How to Add a Contact
3.  How to Edit a Contact
4.  How to Delete a Contact
5.  How to Search for a Contact
6.  How to Display All Contacts
7.  How to Export Contacts to a Text File

### 1. Walk Through the Menu ###
When you start the program, the following menu will appear:

    Welcome to the Contact Management System!
    Menu:
    1. Add a new contact
    2. Edit an existing contact
    3. Delete a contact
    4. Search for a contact
    5. Display all contacts
    6. Export contacts to a text file
    7. Quit

    Please enter the task you wish to perform from the menu list (example: Add a new contact): |

In order to access a menu item, simply type out the item you wish to access. For example, if you wanted to add a new contact, type "add a new contact" and that particular function will run.

If you wish to quit the program, type "quit", which will take you to the following message: 

    Are you sure you would like to quit the program? (type yes or no): 

Typing "yes" will cause the program to shut down. Typing "no" will take you back to the menu.

### 2. How to Add a Contact ###

To add a contact, first you enter "add a new contact" when prompted:

    Please enter the task you wish to perform from the menu list (example: Add a new contact): add a new contact|

Once this is entered, the program will prompt you to enter various information, starting with the first name of the contact you wish to enter. Press enter once you type out each piece of information in order to add it to the contact and proceed to the next one.
At the end, the program will ask you to input whether or not you would like to add additional categories of information to your contact:

    Would you like to add any other details? (yes/no): |

Entering "no" will take you back to the main menu.
Entering "yes" will cause the program to ask for the name of the category you wish to add, followed by the information you wish to put in that category:

    Please enter the category you wish to add: (ex: birthday): |

    Please enter the information for {*category}: 

When you are done, the program will ask again if you would like to add other details. Typing "yes" will walk you through the above steps. Typing "no" will return to the main menu.
  
*"category" will be replaced with the name you enter for the custom category you are adding.

### 3. How to Edit a Contact ###

To edit a contact, enter "Edit an existing contact" when prompted:

    Please enter the task you wish to perform from the menu list (example: Add a new contact): edit an existing contact|

Once you do, the program will prompt you to type the name of the contact you wish to edit:

    Please input the full name of the contact you wish to edit: |

You **must** enter the full name, or the program will display the following message and return you to the main menu:

    Contact not found.

After you successfully enter the name of the contact you wish to edit, the program will ask for the name of the category you wish to edit:

    Please input the info category you wish to edit (example: Name): |

If the category is not found, it will create a new category for the info you plan to add. Next, the program will prompt you to enter in the new information:

    Please input the updated info: |

This is where you put in the edited information.  For example, if you selected "phone", you would then input the new phone number. Afterwards, the program will display the following message and return to the main menu:

    Contact successfully edited!

### 4. How to Delete a Contact ###

To delete a contact, enter "delete a contact" when prompted:

        Please enter the task you wish to perform from the menu list (example: Add a new contact): delete a contact|

The program will then ask you to provide the name of the contact you wish to delete. The program is not case sensitive, but you must enter the name as it appears in the contact list, or the program will not be able to find the contact to delete.

        Please provide the name of the contact you wish to delete (type the name as it appears in the contact list): |

If you enter the name of the contact incorrectly, or the contact is not listed in the contact list, then the program will displya "Contact not found." and return to the menu. Otherwise, the program will display "Contact deleted." when the contact is successfully found and removed. 

### 5. How to Search for a Contact ###

To search for a contact, enter "search for a contact" when prompted:

        Please enter the task you wish to perform from the menu list (example: Add a new contact): search for a contact|

The program will then ask for you to enter the name of the contact you are searching for. As before, the program is not case sensitive, but you must enter the name as it appears in the contact list. If the program is able to find the contact you input, then it will display the contact information in the following manner:

        Contact: {'Name': 'Example Man', 'Home/Cell': '123-456-7890', 'Email': 'example.man@example.com', 'Home Address': '123 Example Dr. Example City, State',          'Work Phone': '987-654-3210', 'Birthday': '01/01/11'}

If the program cannot find the contact in the list, either because they are not in the list or because the name was entered incorrectly, the program will display "Contact not found." Whether or not the program finds the contact, it will return to the main menu after searching.

### 6. How to Display All Contacts ###

To display all contacts, enter "display all contacts when prompted:

        Please enter the task you wish to perform from the menu list (example: Add a new contact): display all contacts |

Once you do, the program will display a list of all the contacts currently in the contact list in the following format:

        Contact: Example Man
            Name: Example Man
            Home/Cell: 123-456-7890
            Email: example.man@example.com
            Home Address: 123 Example Dr. Example City, State
            Work Phone: 987-654-3210
            Extra Categories: Information You Add

Afterwards, the program will return to the main menu.

### 7. How to Export Contacts to a Text File ###

In order to export your contacts to a text file, enter "export contacts to a text file" when prompted:

        Please enter the task you wish to perform from the menu list (example: Add a new contact): export contacts to a text file|

The program will then export your contacts to a file titled "contact_list.txt". If there isn't a file with that name yet within the program's directory, it will create one by that name. If there is, it will overwrite whatever information is in the text file with whatever is on your current list. The program will then display "Contacts Exported!" and return to the main menu.
