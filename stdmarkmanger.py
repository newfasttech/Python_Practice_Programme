students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Show Topper")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        marks = int(input("Marks: "))
        students[name] = marks

    elif choice == "2":
        for name, marks in students.items():
            print(name, marks)

    elif choice == "3":
        topper = max(students, key=students.get)
        print("Topper:", topper, students[topper])

    elif choice == "4":
        break
