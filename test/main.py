# ____________________ files handling ____________________

# # f = open('myfile.txt', 'r') 
# f = open('myfile.txt') # r is default
# # f = open('myfile.txt', 'rt') # as a text file open
# f = open('myfile.txt', 'rb') # as a binary

# txt = f.read()
# print(txt)
# f.close()

# -----

# f = open('myfile.txt', 'a')
# f = open('myfile.txt', 'w')
# f.write("Hello world")
# f.close()

# -----

# with open('myfile.txt', 'a') as f:
#     f.write('Hey i am new ')

# -----# -----# -----# -----# -----# -----# -----

# f = open("myfile.txt", 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[0]
#     print(f"marks of students {i} is {m1*4}")
#     print(f"marks of students {i} is {m2}")
#     print(f"marks of students {i} is {m3}")

# print(type(m1))
# print(type(m2))

# -----# -----# -----# -----# -----# -----# -----


# f = open("myfile2.txt", 'w')
# lines = ['line 1\n','line 2\n','line 3\n']
# f.writelines(lines)
# f.close()
# ____________________ os ____________________


#os

# import os 
# # os.mkdir("data")

# if(not os.path.exists()):
#     os.mkdir("data")

# for i in range(1,10):
#     os.mkdir(f"Data/Day {i+1}")




# import os
# # os.mkdir("Data")

# for i in range(1,10):
#     os.mkdir(f"Data/Day {i+1}")


# import os
# # os.mkdir("Data")
# # if(not os.path.exists()):
# #     os.mkdir("Data")

# for i in range(0,10):
#     os.rename(f"Data/New {i+1}", f"Data/Create {i+1}")


# import os
# folders = os.listdir("Data")

# # print(folders)

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"Data/{folder}"))



# ____________________ Pathlib ____________________
# print(os.getcwd())
# os.chdir("/Users")
# print(os.getcwd())


# from pathlib import Path
# # Creating
# p1 = Path("data/file.txt")
# # print (p1)
# # Windows-style absolute path (raw string)
# p2 = Path(r"C:\Users\Amar\doc")
# print (p2)
# # Linux/mac absolute path
# p3 = Path("/home/amar/doc")
# print (p3)

# file = open("students.csv", "r")
# data = file.read()
# print(data)
# file.close()


# ____________________ CSV ____________________

# 1\. CSV (Comma-Separated Values): CSV is a file format used to store tabular data in rows and columns, where values are typically separated by commas. In Python, the built-in `csv` module is used to read and write CSV files.

# 2\. JSON (JavaScript Object Notation): JSON is a lightweight data-interchange format used to store and exchange structured data using key-value pairs and arrays. In Python, the built-in `json` module is used to read, write, and process JSON data.

# file = open("students.csv", "r")
# data = file.read()
# print(data)
# file.close()

# with open("students.csv", "r") as file:
#     data = file.read()
#     print(data)

# import csv

# with open('students.csv', 'w', newline='') as file:
#     writer = csv.writer(file)

#     writer.writerow(["name", "age", "branch"])
#     writer.writerow(["Chinmay", 20, "AI"])
#     writer.writerow(["Gautam", 21, "CSE"])
#     writer.writerow(["Harsh", 20, "IT"])

# with open('students.csv', 'r', newline='') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)



# import csv

# with open("student.csv", "r", newline="") as file:
#     reader = csv.DictReader(file)

#     for student in reader:
#         print(student["name"], student["marks"])
        


# import csv

# fields = ["id", "name", "marks"]

# student = {"id": 4, "name": "Rahul", "marks": 88}

# with open("students.csv", "a", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=fields)
#     writer.writerow(student)



# import csv

# with open("students.csv", "r", newline="") as file:
#     reader = csv.DictReader(file)

#     for student in reader:
#         if student["id"] == "2":
#             print(student)
#             break


# import csv

# total = 0
# count = 0

# with open("students.csv", "r", newline="") as file:
#     reader = csv.DictReader(file)

#     for student in reader:
#         total += float(student["marks"])
#         count += 1

# if count > 0:
#     print("Average:", total / count)
# else:
#     print("No student records found")



# ____________________ JSON processing ____________________


# import json

# student = {
#     "id": 1,
#     "name": "Chinmay",
#     "marks": 85,
#     "passed": True
# }

# with open("myjson.json", "w") as file:
#     json.dump(student, file, indent=4)


# with open("student.json", "r") as file:
#     student = json.load(file)

# print("\n")

# print(student)
# print("\n")

# print(student["name"])
# print(student["marks"])
# print(student["passed"])
# print("\n")

# json.load(file)
# JSON file → Python object
# data = json.load(file)

# json.dump(data, file)
# Python object → JSON file
# json.dump(data, file, indent=4)



# student = {
#     "name": "Chinmay",
#     "college": {
#         "name": "Arya College",
#         "city": "Jaipur"
#     },
#     "skills": ["Python", "AI", "Web"]
# }

# print(student["college"]["city"])
# print(student["skills"][0])


# data - mongodb - json 
# json data store easy, 
