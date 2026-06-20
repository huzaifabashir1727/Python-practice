import os
import json

if os.path.exists("contacts.json") :
    try:
        with open("contacts.json", "r") as contacts :
            contact_list = json.load(contacts)
    except (json.JSONDecodeError, ValueError):
        contact_list = {}
else :
    contact_list = {}

def add() :
    print("Adding contact")
    name = input("Enter name : ")
    number = input("Enter number : ")

    contact_list[name] = number
    
    with open("contacts.json" , "w") as contacts :
        json.dump(contact_list , contacts)
        
    print(f"{name} added to contact list")

def search() :
    if len(contact_list) == 0 :
        print("Contacts list is empty")
    else :
        name_or_number = input("Enter name or number : ")
        filtered_contact = {k : v for k,v in contact_list.items()
                            if v == name_or_number or k.lower() == name_or_number.lower() }
        if filtered_contact :
            print(filtered_contact)
        else :
            print("Contact not exist")
        
while True :
    operation = input("Enter operation you want to perform : ")
    
    if operation == "add" or operation == "Add" :
        add()
    elif operation == "search" or operation == "Search" : 
        search()
    elif operation == "terminate" or operation == "Terminate" :
        break
    else:
        print("Invalid operation")