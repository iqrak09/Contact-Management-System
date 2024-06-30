# Contact Management System

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, email, phone):
        new_contact = Contact(name, email, phone)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found!")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return
        print("Contact not found!")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully!")
                return
        print("Contact not found!")

    def update_contact(self, name, new_email=None, new_phone=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_email:
                    contact.email = new_email
                if new_phone:
                    contact.phone = new_phone
                print(f"Contact {name} updated successfully!")
                return
        print("Contact not found!")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            contact_manager.add_contact(name, email, phone)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            name = input("Enter name to search: ")
            contact_manager.search_contact(name)
        elif choice == "4":
            name = input("Enter name to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "5":
            name = input("Enter name to update: ")
            new_email = input("Enter new email (optional): ")
            new_phone = input("Enter new phone (optional): ")
            contact_manager.update_contact(name, new_email, new_phone)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()