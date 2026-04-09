contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif choice == "2":
        name = input("Search name: ")
        print(contacts.get(name, "Contact not found"))

    elif choice == "3":
        name = input("Delete name: ")
        contacts.pop(name, None)

    elif choice == "4":
        for name, phone in contacts.items():
            print(name, phone)

    elif choice == "5":
        break
