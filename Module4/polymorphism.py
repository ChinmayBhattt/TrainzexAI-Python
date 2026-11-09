# Polymorphism in Python – Basic to Intermediate
# 1. What is Polymorphism?
# Polymorphism is one of the four main pillars of Object-Oriented Programming (OOP).

# The word Polymorphism comes from two Greek words:
# - Poly = Many
# - Morph = Forms
# Therefore, Polymorphism means One Name, Many Forms.

# In Python, polymorphism allows the same method, function, or operator to perform different operations depending on the object or data type.

# Real-life example:

# Consider a person who can perform different roles:
# - As a student → Studies.
# - As an employee → Works.
# - As a teacher → Teaches.
# The person is the same, but the behaviour changes depending on the role.class Dog:


# class Dog:
#     def sound(self):
#         print("Dog barks")


# class Cat:
#     def sound(self):
#         print("Cat meows")


# class Cow:
#     def sound(self):
#         print("Cow moos")


# # Creating objects
# d = Dog()
# c = Cat()
# co = Cow()

# # Calling same method
# d.sound()
# c.sound()
# co.sound()

# # 1. How many class? -  3
# # 2. how many methods? - 3
# # methods  - name? - sounds

class Animal: # one name
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal): # many forms
    def sound(self):
        print("Dog barks")


class Cat(Animal):  # many forms
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()