
# # # Encapsulation in Python is the object-oriented programming practice of bundling data (attributes) and methods inside a single class while restricting direct external access to internal state. Unlike languages such as Java or C++, Python does not enforce strict access modifiers at the compiler level, relying instead on naming conventions and name mangling.
# # # 
# # # 
# # # # class Student: #private
# # #     __marks = 90

# # # obj = Student()
# # # print(obj.__marks)

# # # Basic Encapsulation Example

# # class Student:

# #     def __init__(self, name, marks):
# #         self.name = name # public
# #         self.__marks = marks # private

# #     def display(self):
# #         print("Name:", self.name)
# #         print("Marks:", self.__marks)


# # # Creating object
# # s = Student("Chinmay", 90)

# # s.display()





# # __marks - private
# # _mark - protective
# # mark - public

# class Student:

#     def __init__(self, name, marks): # constructor
#         self.name = name       # Public
#         self.__marks = marks   # Private

#     def get_marks(self): # method(function) - get marks - variable called = return = public or private
#         return self.__marks

#     def set_marks(self, marks):
#         if marks >= 0 and marks <= 100:
#             self.__marks = marks # private varible
#         else:
#             print("Invalid marks!")


# # Creating object
# s1 = Student("Shyaam", 85)

# print(s1.name)

# # Accessing private data using method
# print(s1.get_marks())

# # Updating private data
# s1.set_marks(95)

# print(s1.get_marks())



# 3. Real-life example: Bank Account

# Imagine you have a bank account.
# - You can check your balance.
# - You can deposit money.
# - You can withdraw money.
# - You cannot directly change your bank balance.

class BankAccount: #simple class 

    def __init__(self, balance): #constructor # val: object
        self.__balance = balance

    def deposit(self, amount): # deposit
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount): # withdraw
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self): # show balanece
        return self.__balance


account = BankAccount(5000) # object

account.deposit(2000)
account.withdraw(1000)

print(account.get_balance())


# 4. Advantages of encapsulation
# 1. Data Security: Protects data from unintended modification.
# 2. Data Hiding: Restricts direct access to internal variables.
# 3. Controlled Access: Allows modification through getter and setter methods.
# 4. Code Maintainability: Makes code easier to manage and update.
# 5. Validation: Helps validate data before modifying it.