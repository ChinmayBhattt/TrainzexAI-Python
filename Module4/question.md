class Payment:
    def pay(self, amount):
        print("Processing payment")


class UPI(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class CreditCard(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")


class Cash(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Cash")


# Creating objects
payments = [
    UPI(),
    CreditCard(),
    Cash()
]

# Polymorphism
for payment in payments:
    payment.pay(1000)


    https://www.geeksforgeeks.org/python/polymorphism-in-python/




Q1. Student Management

Create a Student class with private attributes __name and __marks. Create getter methods to display their values.

Basic
Q2. Employee Salary

Create an Employee class with a private salary attribute. Use getter and setter methods to update the salary.

Intermediate
Q3. Bank Account

Create a BankAccount class with private balance. Implement deposit, withdraw, and check balance methods.

Intermediate
Q4. Product Inventory

Create a Product class with private price and quantity. Prevent negative values using setter methods.

Intermediate
Q5. Login System

Create a User class with a private password. Implement a method to validate the password without exposing it directly.