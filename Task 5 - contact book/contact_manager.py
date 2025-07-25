contacts = []

# Add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print(f"\n✅ Contact for {name} added successfully!\n")

# View all contacts
def view_contacts():
    if not contacts:
        print("\n📭 No contacts found.\n")
        return

    print("\n📒 Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

# Search contact by name or phone
def search_contact():
    keyword = input("Enter name or phone to search: ").lower()
    found = False

    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            print("\n🔍 Contact found:")
            print_contact(contact)
            found = True
            break

    if not found:
        print("\n❌ Contact not found.\n")

# Update contact
def update_contact():
    name = input("Enter the name of the contact to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("\nLeave a field blank to keep it unchanged.")
            new_phone = input(f"New phone ({contact['phone']}): ") or contact["phone"]
            new_email = input(f"New email ({contact['email']}): ") or contact["email"]
            new_address = input(f"New address ({contact['address']}): ") or contact["address"]

            contact["phone"] = new_phone
            contact["email"] = new_email
            contact["address"] = new_address

            print(f"\n✅ Contact for {contact['name']} updated successfully!\n")
            return

    print("\n❌ Contact not found.\n")

# Delete contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print(f"\n🗑️ Contact for {contact['name']} deleted successfully!\n")
            return

    print("\n❌ Contact not found.\n")

# Utility to display full contact details
def print_contact(contact):
    print(f"Name    : {contact['name']}")
    print(f"Phone   : {contact['phone']}")
    print(f"Email   : {contact['email']}")
    print(f"Address : {contact['address']}\n")

# Menu
def menu():
    while True:
        print("📇 Contact Manager")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

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
            print("\n👋 Exiting Contact Manager. Goodbye!\n")
            break
        else:
            print("❌ Invalid choice. Please enter 1-6.\n")

# Run the program
menu()
