# Object-Oriented Programming
#1. Create a class called car with attributes brand and color. Instantiate an object of the car class and print its attributes.
class Car:

    # class attribute
    wheels = 4

    # initializer / instance attributes
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    # method 1
    def showDescription(self):
        print("This car is a", self.color, self.brand)

c = Car('Black', 'Ford')

# call method 1
c.showDescription()
# Prints This car is a Black Ford

#2. Add a method called start_engine to the car class that prints a message saying the engine of the car has started. Create an instance of car and call the method.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

        #method 
        def start_engine(self):
            print(f"The engine of the {self.color}  {self.brand} car has started.")
            c = Car('Black','Ford')
        c.start_engine()

#3. Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount
# Withdraw an amount(only if sufficient balance exists)
# Print the account balance
# Define a class called Bank to implement a simple banking system
class Bank:
    # Initialize the bank with an empty dictionary to store customer accounts and balances
    def __init__(self):
        self.customers = {}

    # Create a new account with a given account number and an optional initial balance (default to 0)
    def create_account(self, account_number, initial_balance=0):
        if account_number in self.customers:
            print("Account number already exists.")
        else:
            self.customers[account_number] = initial_balance
            print("Account created successfully.")

    # Make a deposit to the account with the given account number
    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount
            print("Deposit successful.")
        else:
            print("Account number does not exist.")

    # Make a withdrawal from the account with the given account number
    def make_withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Account number does not exist.")

    # Check and print the balance of the account with the given account number
    def check_balance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f"Account balance: {balance}")
        else:
            print("Account number does not exist.")

# Create an instance of the Bank class
bank = Bank()

# Create customer accounts and perform account operations
acno1= "SB-123"
damt1 = 1000
print("New a/c No.: ",acno1,"Deposit Amount:",damt1)
bank.create_account(acno1, damt1)

acno2= "SB-124"
damt2 = 1500
print("New a/c No.: ",acno2,"Deposit Amount:",damt2)
bank.create_account(acno2, damt2)

wamt1 = 600
print("\nDeposit Rs.",wamt1,"to A/c No.",acno1)
bank.make_deposit(acno1, wamt1)

wamt2 = 350
print("Withdraw Rs.",wamt2,"From A/c No.",acno2)
bank.make_withdrawal(acno2, wamt2)

print("A/c. No.",acno1)
bank.check_balance(acno1)

print("A/c. No.",acno2)
bank.check_balance(acno2)

wamt3 = 1200
print("Withdraw Rs.",wamt3,"From A/c No.",acno2)
bank.make_withdrawal(acno2, wamt3)

acno3 = "SB-134"
print("A/c. No.",acno3)
bank.check_balance(acno3)  # Non-existent account number 

#4. Implement a class called Library that manages a collection of books. Each book has a title, author and available status. The Library class should have methods to:
# Add a book to the library
# Remove a book from the library
# Check if the book is available by the title.
# Borrow a book (mark it as unavailable if it's available).
# Return a book (mark it as available again if it was borrowed).
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self,title,author):
        self.books.append(Book(title, author))

    def remove_book(self,title):
        self.books = [book for book in self.books if book.title != title]

    def is_available(self,title):
        for book in self.books:
            if book.title == title:
             return book.available
        return False

    def borrrow_book(self,title):
        for book in self.books:
            if book.title == title:
                book.available = 'Unavailable'

    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                book.available = 'available'


library = Library()
library.add_book('Python Programming', 'Monica Atim')
print(library.is_available('Python Programming'))
library.borrrow_book(('Python Programming'))
print(library.is_available('Python Programming'))
library.return_book('Python Programming')
print(library.is_available('Python Programming'))
pass
pass