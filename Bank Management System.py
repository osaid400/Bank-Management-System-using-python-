# Bank Management System
# Author: Muhammad Abdullah Farooq
# Language: Python
# Level: Beginner

import json
import os
import sys

print("============ Welcome to Bank Managment System =============")

# ---------------- File Handling ----------------

def load_accounts():
    if os.path.exists("accounts.json"):
        with open("accounts.json", "r") as file:
            data = json.load(file)
        return data
    else:
        return []

def save_accounts():
    with open("accounts.json", "w") as file:
        json.dump(accounts, file, indent=3)

accounts = load_accounts()

if not accounts:
    accounts = [
        {"Name" : "Ali", "Balance": 15000, "Account Number": 3011},
        {"Name" : "Abdullah", "Balance": 23500, "Account Number": 3012},
        {"Name" : "Ahmed", "Balance": 18000, "Account Number": 3013},
        {"Name" : "Abdul Hadi", "Balance": 56000, "Account Number": 3014},
        {"Name" : "Alina", "Balance": 29000, "Account Number": 3015},
        {"Name" : "Rida", "Balance": 250000, "Account Number": 3016},
        {"Name" : "Areeba", "Balance": 17000, "Account Number": 3017},
        {"Name" : "Ayesha", "Balance": 23500, "Account Number": 3018},
        {"Name" : "Alishba", "Balance": 43000, "Account Number": 3019},
        {"Name" : "Bilal", "Balance": 78000, "Account Number": 3020},
    ]
    save_accounts()

# Functions of Menu:

def create_account():
    name = input("Enter the Name: ").strip()
    if name == "":
        print("Name cannot be empty!")
        return

    try:
        account_number = int(input("Enter the new account ID: "))
    except ValueError:
        print("Invalid account ID! Please enter a number.")
        return

    if account_number <= 0:
        print("Enter a valid account ID!")
        return

    for account in accounts:
        if account["Account Number"] == account_number:
            print("account ID already exists!")
            return

    try:
        balance= int(input("Enter the initial balance: "))
    except ValueError:
        print("Invalid Balance!")
        return

    if balance < 0:
        print("Initial Balance cannot be Negative!")
        return

    new_account = {
        "Name" : name,
        "Balance" : balance,
        "Account Number" : account_number,
    }
    
    accounts.append(new_account)

    save_accounts()
    print("New Account Added Successfully!")

def view_account():
    for account in accounts:
        print("---------------------------------------------------")
        print("Name:", account["Name"])
        print("Balance:", account["Balance"])
        print("Account Number:", account["Account Number"])
        print("---------------------------------------------------")

def deposit_money():
    try:
        search = int(input("Enter the Account number: "))
    except ValueError:
        print("Invalid Account Number!")
        return

    found = False
    for account in accounts:
            if account["Account Number"] == search:
                print("Account Found Successfully!")
                try:
                    amount = int(input("Enter Amount: "))
                except ValueError:
                    print("Invalid Amount!")
                    return
                if amount <= 0:
                    print("amount cannot be Negative or Zero!")
                    return
                account["Balance"] += amount
                save_accounts()
                print("Money Deposit Successfully!")
                found = True
                break
    if found == False:
        print("Account Not Found")

def withdraw_money():
    try:
        search = int(input("Enter the Account number: "))
    except ValueError:
        print("Invalid Account Number!")
        return
    found = False
    for account in accounts:
        if account["Account Number"] == search:
            print("Account Found Successfully!")
            try:
                amount = int(input("Enter Amount: "))
            except ValueError:
                print("Invalid Amount!")
                return
            if amount <= 0:
                    print("Zero and Negative amount can't be withdraw!")
                    return
            if amount > account ["Balance"]:
                print("Insufficent Balance!")
                return
            account["Balance"] -= amount
            save_accounts()
            print("Money Withdraw Successfully!")
            found = True
            break
    if found == False:
        print("Account Not Found")

def check_balance():
    try:
        search = int(input("Enter the Account number: "))
    except ValueError:
        print("Invalid Account Number!")
        return
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
    try:
        search = int(input("Enter the account number: "))
    except ValueError:
        print ("Invalid Account Number!")
        return
    found = False

    choice = input("Are you sure? (y/n): ").lower()

    if choice == "y":
        for account in accounts:
            if account["Account Number"] == search:
                accounts.remove(account)
                save_accounts()
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

    try:
        choice = int(input("Enter the number (0-6): "))
    except ValueError:
        print("Invalid Number!")
        continue

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
        sys.exit()
    else:
        print("Invalid Choice!")