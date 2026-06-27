# Bank Management System

print("============ Welcome to Bank Managment System =============")

accounts = [
    {"Name" : "Ali", "Balance": 15000, "Account Number": 3011},
    {"Name" : "Abdullah", "Balance": 23500, "Account Number": 3012},
    {"Name" : "Ahmed", "Balance": 18000, "Account Number": 3013},
    {"Name" : "Abdul Hadi", "Balance": 56000, "Account Number": 3014},
    {"Name" : "Alina", "Balance": 29000, "Account Number": 3015},
    {"Name" : "Rida", "Balance": 250000, "Account Number": 3016},
    {"Name" : "Areeba", "Balance": 17000, "Account Number": 3017},
    {"Name" : "Ayesha", "Balance": 23500, "Account Number": 3018},
]


# Functions of Menu:
def create_account():
    name = input("Enter the Name: ")
    account_number = int(input("Enter the Account number: "))
    balance= int(input("Enter the initial balance: "))
    
    if balance < 0:
        print("Initial Balance cannot be Negative!")
        return

    if account_number <= 0:
        print("Invalid Account Number!")
        return

    for account in accounts:
        if account["Account Number"] == account_number:
            print("Account Number already exists!")
            return

    new_account = {
        "Name" : name,
        "Balance" : balance,
        "Account Number" : account_number,
    }
    
    accounts.append(new_account)
    
    print("New Account Added Successfully!")


def view_account():
    for account in accounts:
        print("---------------------------------------------------")
        print("Name:", account["Name"])
        print("Balance:", account["Balance"])
        print("Account Number:", account["Account Number"])
        print("---------------------------------------------------")

def deposit_money():
    search = int(input("Enter the Account number: "))
    found = False
    for account in accounts:
            if account["Account Number"] == search:
                print("Account Found Successfully!")
                amount = int(input("Enter Amount: "))
                if amount <= 0:
                    print("amount cannot be Negative or Zero!")
                    return
                account["Balance"] += amount
                print("Money Deposit Successfully!")
                found = True
                break
    if found == False:
        print("Account Not Found")

def withdraw_money():
    search = int(input("Enter the Account number: "))
    found = False
    for account in accounts:
        if account["Account Number"] == search:
            print("Account Found Successfully!")
            amount = int(input("Enter Amount: "))
            if amount <= 0:
                    print("Invalid Amount!")
                    return
            if amount > account ["Balance"]:
                print("Insufficent Balance!")
                return
            account["Balance"] -= amount
            print("Money Withdraw Successfully!")
            found = True
            break
    if found == False:
        print("Account Not Found")

def check_balance():
    search = int(input("Enter the Account number: "))
    found = False
    for account in accounts:
        if account["Account Number"] == search:
            print("Account Found Successfully!")
            print("The Balance is: ", account["Balance"])
            found = True
            break
    if found == False:
        print("Account Not Found")

def delete_account():
    search = int(input("Enter the account number: "))
    found = False

    choice = input("Are you sure? (y/n): ").lower()

    if choice == "y":
        for account in accounts:
            if account["Account Number"] == search:
                accounts.remove(account)
                print("Account Deleted Successfully!")
                found = True
                break
        if found == False:
            print("Account Not Found")
    else:
        print("Delete Cancelled!")

# Menu
while True:
    print()
    print("=============== Select the Option ===============")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Delete Account")
    print("0. Exit")

    choice = int(input("Enter the number: "))

    if choice == 1:
        create_account()
    elif choice == 2:
        view_account()
    elif choice == 3:
        deposit_money()
    elif choice == 4:
        withdraw_money()
    elif choice == 5:
        check_balance()
    elif choice == 6:
        delete_account()
    elif choice == 0:
        print("Thank You for using our application :) ")
        print("Good Bye!")
        break
    else:
        print("Invalid Choice!")