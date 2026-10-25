# # Classes and objects
# In Python, Object-Oriented Programming (OOP) centers around two core concepts: classes and objects.
# • A Class is a blueprint or template for creating objects. It defines the structure, data (attributes), and behaviors (methods) that its objects will have.
# • An Object is an instance of a class. It is the actual entity created from the blueprint, containing real data in memory.


# class Person:
#     #public
#     name = "shyaam"
#     occupation = "software developer"
#     age = 26

#     def info(self): # method
#         print(f"{self.name} is a {self.occupation}")


# a = Person()
# a.info()
# # print(f"Your Name is {a.name}")
# # print(f"Your occupation is {a.occupation}")
# # print(f"Your age is {a.age}")


class Calculator:

    num1 = 10
    num2 = 20

    def add(self):
        print(f"{self.num1 + self.num2}")

    def sub(self):
        print(f"{self.num1 - self.num2}")

cal = Calculator()
cal.add()
cal.sub()