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


# class Calculator:

#     num1 = 10
#     num2 = 20

#     def add(self):
#         print(f"{self.num1 + self.num2}")

#     def sub(self):
#         print(f"{self.num1 - self.num2}")

# cal = Calculator()
# cal.add()
# cal.sub()


# To calculate Simple Interest in Python, you use the fundamental financial formula:
# \(\mathbf{I=P\times R\times T}\)
# Where:
# • I = The total interest earned
# • P = The principal amount (the initial money borrowed or invested)
# • R = The annual interest rate (in decimal format, e.g., 5% = 0.05)
# • T = The time the money is borrowed or invested (in years)


# class math1:

#     def set(self, p,r,t):
#         self.p = p
#         self.r = r
#         self.t = t
#         self.i = self.p * self.r * self.t

#     def get(self):
#         print(f"The total interest earned {self.i}")



# result = math1()

# result.set(0,5000,5,2)
# result.get()

        


# type convesion




# class Student:
#     name = "Shyaam"
#     age = 20

#     def show(self):
#         print(self.name)
#         print(self.age)


# s1 = Student()
# s1.show()

    
# __init__() constructor


# class student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


#     def display(self):
#         print("Name",self.name)
#         print("Age",self.age)



# res = student("Shyaam",20)
# res1 = student("Muskan",19)
# res.display()
# res1.display()



class Demo:
    count = 0

    def instance_method(self):
        print("Instance method")

    @classmethod
    def class_method(cls):
        print("Class method")

    @staticmethod
    def static_method():
        print("Static method")


d = Demo()
d.instance_method()
Demo.class_method()
Demo.static_method()
