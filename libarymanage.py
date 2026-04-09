available_books = set()
issued_books = {}

while True:
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View Available Books")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Book name: ")
        available_books.add(book)
        print("Book added!")

    elif choice == "2":
        book = input("Book name: ")
        name = input("Student name: ")
        if book in available_books:
            available_books.remove(book)
            issued_books[book] = name
            print("Book issued!")
        else:
            print("Book not available!")

    elif choice == "3":
        book = input("Book name: ")
        if book in issued_books:
            available_books.add(book)
            issued_books.pop(book)
            print("Book returned!")
        else:
            print("Invalid book!")

    elif choice == "4":
        print("Available Books:", available_books)

    elif choice == "5":
        break
