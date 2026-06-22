file = open("data.txt", "wt")  
content = file.write("eda eda edaaa")
file.close()

file = open("data.txt", "rt")  
print(file.read())
file.close()

file = open("data.txt", "r+")
file.write("Hello")
file.close()

file = open("data.txt", "rt") 
print(file.read())
file.close()

file = open("data.txt", "w+")
file.write("New Data")
file.seek(0)
print(file.read())
file.close()

file = open("data.txt", "a+")
file.write("\nAdded line")
file.seek(0)
print(file.read())
file.close()

student = open("student.txt","w")
student.write("Student Records Started")
student.close()


attendance = open("attendance.txt","w")
attendance.write("Sidharth M N - present")
attendance.close()
attendance = open("attendance.txt","a")
attendance.write("\nRonaldo - present \nVirat - present \nWalter - absent \nThanos - absent")
attendance.close()

marks = open("marks.txt","w")
marks.write("Sidharth - 40")
marks.close()
marks = open("marks.txt","a")
marks.write("\nRonaldo - 35 \nVirat - 39 \nWalter - 0 \nThanos - 30")

marks = open("marks.txt","r")
print(marks.read())
marks.close()

#read() , readline() , readlines()

marks = open("marks.txt","r")
print(marks.read())
marks.close()

marks = open("marks.txt","r")
print(marks.readline())
print(marks.readline())
print(marks.readline())
print(marks.readline())
print(marks.readline())
marks.close()

marks = open("marks.txt","r")
for line in marks.readlines():
    print(line.strip())
marks.close()

#write and writelines

student = open("student.txt", "w")

student.write("Student Records")
student.write("\nName: Sidharth, Marks: 40, Attendance: 95%\n")
student.write("Name: Ronaldo, Marks: 35, Attendance: 92%\n")
student.write("Name: Virat, Marks: 39, Attendance: 92%\n")
student.write("Name: Walter, Marks: 0, Attendance: 50%\n")
student.write("Name: Thanos, Marks: 30, Attendance: 50%\n")
student.close()

#writelines

student = open("student.txt", "a")

data = [
    "Name: John, Marks: 40, Attendance: 90%\n",
    "Name: Alex, Marks: 32, Attendance: 95%\n",
    "Name: Sam, Marks: 27, Attendance: 88%\n"
]

student.writelines(data)

student.close()

with open("student.txt", "r") as file:
    student = file.read()
    print(student)

#automatically closes file when the read is complete - with statment

#display .name, .mode ,.closed

file = open("student.txt", "r")
print(file.name)
file.close()

file = open("student.txt", "r")
print(file.mode)
file.close()

file = open("student.txt", "r")
print(file.closed) #check if close is true or false
file.close()
print(file.closed)

#use seek and tell
#tell
file = open("student.txt", "r")
print(file.tell())
file.close()

#seek
file = open("student.txt", "r")
file.read(5) #reads from that position
print(file.tell()) #tell current position
print(file.read()) # reads from the postion

file.seek(0)        # move back to start
print(file.tell())
file.close()

#os module in python

import os

#os.mkdir("student_records") Make directory
print(os.listdir()) #list directory

#os.rename("records.txt", "rec.txt") Rename directory
print(os.listdir())

if os.path.exists("student.txt"):
    print("File exists")
else:
    print("File not found")

#exceptional handling

try:
    file = open("students.txt","r") #students.txt not exists
    print(file.read())

except FileNotFoundError:
    print("File not exists")

finally:
    print("Operation Completed")

try:
    file = open("data.txt", "z") #z is a invalid file mode

except ValueError:
    print("Invalid file mode")

finally:
    print("Execution finished")

try:
    file = open("D:/SIDSOID/python/__pycache__/calculator.cpython-314.pyc", "r")

except PermissionError:
    print("Permission denied")

finally:
    print("Process completed")

#read binary and write binary
#wb
file = open("data.bin", "wb")
file.write(b"Hello Binary Data")
file.close()
#rb
file = open("data.bin", "rb")
print(file.read())
file.close()

#read image in binary

file = open("car.jpg", "rb")
data = file.read()

file2 = open("student.jpg", "wb")
file2.write(data)

file.close()
file2.close()

#serialisation
#pickle.dump() store list or tuple or--
# python objects to save in a file 

import pickle

students = [
    {"name": "Sidharth", "marks": 40, "attendance": 95},
    {"name": "Ronaldo", "marks": 35, "attendance": 92},
    {"name": "Virat", "marks": 39, "attendance": 92},
    {"name": "Walter", "marks": 0, "attendance": 50},
    {"name": "Thanos", "marks": 30, "attendance": 50},
    {"name": "John", "marks": 40, "attendance": 90},
    {"name": "Alex", "marks": 32, "attendance": 95},
    {"name": "Sam", "marks": 27, "attendance": 88}
]

file = open("students.pkl", "wb")
pickle.dump(students, file)
file.close()

#pickle.load()

file = open("students.pkl", "rb")
data = pickle.load(file)

print(data)
file.close()

#json.dump()

import json

students = [
    {"name": "Sidharth", "marks": 40, "attendance": 95},
    {"name": "Ronaldo", "marks": 35, "attendance": 92},
    {"name": "Virat", "marks": 39, "attendance": 92},
    {"name": "Walter", "marks": 0, "attendance": 50},
    {"name": "Thanos", "marks": 30, "attendance": 50},
    {"name": "John", "marks": 40, "attendance": 90},
    {"name": "Alex", "marks": 32, "attendance": 95},
    {"name": "Sam", "marks": 27, "attendance": 88}
]

file = open("students.json", "w")
json.dump(students, file)
file.close()

#json.load()
file = open("students.json", "r")
data = json.load(file)

print(data)
file.close()

#final output

students = []

while True:
    print("\n------ STUDENT RECORD MANAGEMENT SYSTEM ------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Save as JSON")
    print("4. Save as Pickle")
    print("5. File Info Demo")
    print("6. Directory Contents")
    print("7. Exit")

    choice = input("Enter choice: ")

    # 1. Add Student
    if choice == "1":
        student = {
            "name": input("Enter Name: "),
            "marks": int(input("Enter Marks: ")),
            "attendance": int(input("Enter Attendance: "))
        }
        students.append(student)
        print("Student Added Successfully")

    # 2. View Students
    elif choice == "2":
        for s in students:
            print(s)

    # 3. Save as JSON
    elif choice == "3":
        file = open("students.json", "w")
        json.dump(students, file)
        file.close()
        print("JSON File Created Successfully")

    # 4. Save as Pickle
    elif choice == "4":
        file = open("students.pkl", "wb")
        pickle.dump(students, file)
        file.close()
        print("Pickle File Created Successfully")

    # 5. File Object Demo
    elif choice == "5":
        file = open("students.txt", "w+")
        file.write("Student Records Data")

        print("File Name:", file.name)
        print("File Mode:", file.mode)
        print("File Closed Status:", file.closed)
        print("Current File Pointer Position:", file.tell())

        file.close()
        print("Operation completed")

    # 6. Directory Listing
    elif choice == "6":
        print("Directory Contents:")
        print(os.listdir())

    # 7. Exit
    elif choice == "7":
        print("Exiting System...")
        break

    else:
        print("Invalid Choice")