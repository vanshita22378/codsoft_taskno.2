
# Simple Contact Management System

contacts = []

def show_menu():
    print("\n--- CONTACT MANAGEMENT SYSTEM ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\n--- Contact List ---")
        for idx, c in enumerate(contacts, 1):
            print(f"{idx}. {c['name']} - {c['phone']}")

def search_contact():
    query = input("Enter Name or Phone Number to search: ").lower()
    found = False
    for c in contacts:
        if query in c["name"].lower() or query in c["phone"]:
            print("\n--- Contact Found ---")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    for c in contacts:
        if c["name"].lower() == name:
            print("Leave field blank to keep current value.")
            new_name = input(f"New Name [{c['name']}]: ") or c['name']
            new_phone = input(f"New Phone [{c['phone']}]: ") or c['phone']
            new_email = input(f"New Email [{c['email']}]: ") or c['email']
            new_address = input(f"New Address [{c['address']}]: ") or c['address']

            c.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            })
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    for i, c in enumerate(contacts):
        if c["name"].lower() == name:
            confirm = input(f"Are you sure you want to delete '{c['name']}'? (y/n): ").lower()
            if confirm == 'y':
                contacts.pop(i)
                print("Contact deleted successfully.")
            return
    print("Contact not found.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting Contact Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
