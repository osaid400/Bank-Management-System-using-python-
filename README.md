# Bank Management System

A console-based Bank Management System built with Python. This project demonstrates the use of functions, lists, dictionaries, loops, conditional statements, exception handling, and JSON-based file persistence to perform basic banking operations.

## Features

* Create a new bank account
* View all accounts
* Deposit money
* Withdraw money
* Check account balance
* Delete an account
* Prevent duplicate account numbers
* Validate user input
* Persistent storage — accounts are saved to a JSON file and reload automatically on the next run

## Technologies Used

* Python 3

## Concepts Covered

* Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements
* Exception Handling
* User Input
* Data Validation
* List Methods (`append()`, `remove()`)
* File Handling with JSON (`json.load()`, `json.dump()`)
* `os.path.exists()` for safe file loading
* Problem Solving

## Project Structure

```text
Bank-Management-System/
│
├── Bank Management System.py
├── .gitignore
└── README.md
```

> Note: `accounts.json` is created automatically when the program runs and stores account data locally. It is excluded from the repository via `.gitignore` since it holds runtime/test data rather than source code.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/osaid400/Bank-Management-System.git
```

2. Navigate to the project folder:

```bash
cd Bank-Management-System
```

3. Run the program:

```bash
python "Bank Management System.py"
```

## How Data Persistence Works

* On startup, the program checks if `accounts.json` exists using `os.path.exists()`.
* If it exists, all accounts are loaded into memory using `json.load()`.
* If it doesn't exist, the program starts with a default set of sample accounts and saves them to `accounts.json`.
* Every time an account is created, deposited into, withdrawn from, or deleted, the full account list is saved back to `accounts.json` using `json.dump()`, so no data is lost between runs.

## Future Improvements

* Add PIN authentication
* Maintain transaction history
* Transfer money between accounts
* Add account types (Savings/Current)
* Migrate from JSON file storage to SQLite
* Implement Object-Oriented Programming (OOP)

## Learning Outcomes

This project helped me practice:

* Writing modular code using functions
* Managing data with lists and dictionaries
* Searching, updating, and deleting records
* Implementing validation logic and exception handling
* Building a menu-driven console application
* Persisting data between program runs using JSON file handling
* Improving debugging and problem-solving skills

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400