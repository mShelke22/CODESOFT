contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for name, details in contacts.items():
        print(name, "-", details["phone"])

def search_contact():
    search = input("Enter name or phone to search: ")
    for name, details in contacts.items():
        if search == name or search == details["phone"]:
            print("Name:", name)
            print("Phone:", details["phone"])
            print("Email:", details["email"])
            print("Address:", details["address"])
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        contacts[name]["phone"] = input("New phone: ")
        contacts[name]["email"] = input("New email: ")
        contacts[name]["address"] = input("New address: ")
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book")
        break
    else:
        print("Invalid choice")
