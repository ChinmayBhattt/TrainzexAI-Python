# Why do we use Inheritance?
# Inheritance is useful for:
# 1. Code Reusability: Reuse existing code.
# 2. Less Code Duplication: Avoid writing the same methods repeatedly.
# 3. Easy Maintenance: Update common functionality in one place.
# 4. Extensibility: Add new features to existing classes.
# 5. Better Structure: Organize related classes logically.

# class Parent:
#     # Parent class properties and methods
#     pass

# class Child(Parent):
#     # Child class properties and methods
#     pass

# - Parent is the base class.
# - Child is the derived class.
# - Child(Parent) means Child inherits from Parent.



# class Animal: # base class
    
#     def eat(self):
#         print("Animal is eating")



# class Dog(Animal): # derived class
#     def bark(self):
#         print("Dog is barking")


# # Creating object
# d = Dog() # called only one class

# d.eat()   # Inherited method
# d.bark()  # Own method


# # Types of Inheritance in Python
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance


# class Father:
#     def house(self):
#         print("Father owns a house")

# class Son(Father):
#     def bike(self):
#         print("Son owns a bike")


# s = Son()

# s.house()
# s.bike()


# Multiple Inheritance # When one child class inherits from two or more parent classes, it is called Multiple Inheritance.
# class Father: # base 
#     def skills1(self):
#         print("Father: Programming")

# class Mother: # base 
#     def skills2(self):
#         print("Mother: Cooking")

# class Child(Father, Mother): # derieved
#     def skills3(self):
#         print("Child: Gaming")


# c = Child()

# c.skills1()
# c.skills2()
# c.skills3()

# Multilevel Inheritance
# When a class inherits from another child class, creating a chain of inheritance, it is called Multilevel Inheritance.

# class Grandfather: # base
#     def land(self):
#         print("Grandfather owns land")

# class Father(Grandfather):
#     def house(self): # derived
#         print("Father owns a house")

# class Son(Father): # derived
#     def car(self):
#         print("Son owns a car")


# s = Son()

# s.land()
# s.house()
# s.car()


# Hierarchical Inheritance
# When multiple child classes inherit from a single parent class, it is called Hierarchical Inheritance.

# class Animal: #base
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal): # derived
#     def bark(self):
#         print("Dog is barking")

# class Cat(Animal):# derived
#     def meow(self):
#         print("Cat is meowing")


# d = Dog()
# c = Cat()

# d.eat()
# d.bark()

# c.eat()
# c.meow()


# Hybrid Inheritance
# Hybrid Inheritance is a combination of two or more types of inheritance.

# class A: # base
#     def showA(self):
#         print("Class A")

# class B(A): # derived
#     def showB(self):
#         print("Class B")

# class C(A): # derived
#     def showC(self):
#         print("Class C")

# class D(B, C):
#     def showD(self):
#         print("Class D")


# obj = D()

# obj.showA()
# obj.showB()
# obj.showC()
# obj.showD()





# # Parent Class / base class
# class Animal: 
    
#     def eat(self):
#         print("Animal is eating")


# # Child Class / derived class
# class Dog(Animal): # inheritance: single
#     def bark(self):
#         print("Dog is barking")

# # Creating object
# d = Dog()

# d.eat()   # Inherited method
# d.bark()  # Child class method


class Person: # inheritance  - single # base
    def __init__(self, name): # constructor
        self.name = name

    def display(self):
        print("Name:", self.name)


class Student(Person): # derived
    def __init__(self, name, roll_no):  # constructor
        
        super().__init__(name) # super().__init__(name) calls the parent class constructor.
        
        self.roll_no = roll_no

    def show(self):
        print("Roll Number:", self.roll_no)


s = Student("Shyam", 101) #object - val

s.display()
s.show()