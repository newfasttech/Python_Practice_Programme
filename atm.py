accounts = {}

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        acc_no = input("Account Number: ")
        name = input("Name: ")
        accounts[acc_no] = {"name": name, "balance": 0}
        print("Account created!")

    elif choice == "2":
        acc_no = input("Account Number: ")
        amount = int(input("Amount to deposit: "))
        accounts[acc_no]["balance"] += amount
        print("Amount deposited!")

    elif choice == "3":
        acc_no = input("Account Number: ")
        amount = int(input("Amount to withdraw: "))
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        acc_no = input("Account Number: ")
        print("Balance:", accounts[acc_no]["balance"])

    elif choice == "5":
        break
