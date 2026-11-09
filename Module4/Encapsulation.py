# class Student: #private
#     __marks = 90

# obj = Student()
# print(obj.__marks)

# Basic Encapsulation Example

class Student:

    def __init__(self, name, marks):
        self.name = name # public
        self.__marks = marks # private

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)


# Creating object
s = Student("Chinmay", 90)

s.display()