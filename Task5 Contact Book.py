class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact.name}: {contact.phone_number}")

    def search_contact(self, search_term):
        search_results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                search_results.append(contact)
        return search_results

    def update_contact(self, contact_index, new_contact):
        if 0 <= contact_index < len(self.contacts):
            self.contacts[contact_index] = new_contact
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, contact_index):
        if 0 <= contact_index < len(self.contacts):
            del self.contacts[contact_index]
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address: ")
            contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(contact)
            print("Contact added successfully.")

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_results = contact_manager.search_contact(search_term)
            if search_results:
                print("\nSearch Results:")
                for idx, contact in enumerate(search_results, start=1):
                    print(f"{idx}. {contact.name}: {contact.phone_number}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            contact_index = int(input("Enter index of contact to update: ")) - 1
            name = input("Enter new contact name: ")
            phone_number = input("Enter new contact phone number: ")
            email = input("Enter new contact email: ")
            address = input("Enter new contact address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.update_contact(contact_index, new_contact)

        elif choice == '5':
            contact_index = int(input("Enter index of contact to delete: ")) - 1
            contact_manager.delete_contact(contact_index)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
