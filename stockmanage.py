inventory = {}

while True:
    print("\n1. Add Product")
    print("2. Update Stock")
    print("3. Sell Product")
    print("4. View Inventory")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        product = input("Product name: ")
        qty = int(input("Quantity: "))
        inventory[product] = qty

    elif choice == "2":
        product = input("Product name: ")
        qty = int(input("New quantity: "))
        inventory[product] = qty

    elif choice == "3":
        product = input("Product name: ")
        qty = int(input("Quantity sold: "))
        if inventory[product] >= qty:
            inventory[product] -= qty
            print("Product sold!")
        else:
            print("Not enough stock!")

    elif choice == "4":
        for p, q in inventory.items():
            print(p, ":", q)

    elif choice == "5":
        break
