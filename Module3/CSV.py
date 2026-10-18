# 1\. CSV (Comma-Separated Values): CSV is a file format used to store tabular data in rows and columns, where values are typically separated by commas. In Python, the built-in `csv` module is used to read and write CSV files.


# import csv

# # file = open("students.csv", "r") 

# # data = file.read()
# # print(data)
# # file.close()

# with open("students.csv", "r") as file:
#     data = file.read()
#     print(data)


# import csv

# with open('students.csv', 'w', newline='') as file: # write - add
#     writer = csv.writer(file)

#     writer.writerow(["name", "age", "branch"])
#     writer.writerow(["Chinmay", 20, "AI"])
#     writer.writerow(["Gautam", 21, "CSE"])
#     writer.writerow(["Harsh", 20, "IT"])



# with open('students.csv', 'r', newline='') as file: # read - data
    # reader = csv.reader(file)
    # for row in reader:
    #     print(row)


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

# # 1. Define column headers (keys must match the dictionary keys)
# fields = ['name', 'age', 'role']

# # 2. Prepare data as a list of dictionaries
# data = [
#     {'name': 'Alice', 'age': 30, 'role': 'Engineer'}, 
#     {'name': 'Bob', 'age': 35, 'role': 'Designer'}, 
#     {'name': 'Charlie', 'age': 28, 'role': 'Manager'} 
# ]

# # 3. Write data to the CSV file
# with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
# # with open('output.csv', 'w', newline='', encoding='utf-8') as file:
#     # Initialize the DictWriter
#     writer = csv.DictWriter(file, fieldnames=fields)
    
#     # Write the header row (using the strings provided in fieldnames)
#     writer.writeheader()
    
#     # Write all data rows at once
#     writer.writerows(data)


# r - read
# w - write
# a - append - add
# x - create





# import csv

# with open("students.csv", "r", newline="") as file:
#     reader = csv.DictReader(file)

#     for student in reader:
#         if student["id"] == "2":
#             print(student)
#             break

# In Python, csv.DictReader maps the information in each row to a dictionary whose keys are given by the optional fieldnames parameter or inferred from the first row of the CSV file.
# Unlike csv.reader (which returns each row as a list of strings), csv.DictReader allows you to access columns by their actual header names, making your code much cleaner and easier to read.

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

    
