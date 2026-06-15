'''print("Banking Transaction Management System")
customer_name = input("Customer Name : ")
customer_age = int(input("Customer Age : "))
branch_name = input("Enter branch name : " ).lower()
account_type= input("Account Type (Savings/Credit/Current) : ").lower()

if account_type in ("credit","current","savings"):
    print("Account is valid")
else:
    print("Invalid Account")

if branch_name in {"balaramapuram","palode","attukal"}:
    print("Branch Name is Valid")
else:
    print("Invalid Branch Name")

account = {
    "acc1": {
      "customer_name": "Sidharth",
      "customer_age" : 22,
      "branch_name" : "Balaramapuram",
      "account_type" : "Savings"
    },
    "acc2": {
      "customer_name" : "Gowtham",
      "customer_age" : 20,
      "branch_name" : "Attukal",
      "account_type" : "Credit"
    },
    "acc3": {
        "customer_name" : "Arshak",
        "customer_age" : 17,
        "branch_name" : "Palode",
        "account_type" : "Current"
    }
}

print(account)


transactions = []

for i in range(5):
    amount = float(input(f"Enter {i+1} transaction : "))
    transactions.append(amount)
print("Transactions : ",transactions)

highest_transaction = max(transactions)
lowest_transaction = min(transactions)

print("Highest Transaction : ",highest_transaction)
print("Lowest Transaction : ",lowest_transaction)

opening_balance = 10000000
remain_balance = opening_balance - sum(transactions)
print("Remaining Balance after Transaction : ",remain_balance)

search_name = input("Enter customer name to search: ")

for acc_no, details in account.items():
    if details["customer_name"].lower() == search_name.lower():
        print("Account Found")
        print(details)
    else:
        print("Not Account Found")

customers = [
    {"name" : "Sidharth" , "balance" : "100000"},
    {"name" : "Gowtham" , "balance" : "100000"},
    {"name" : "Arshak" , "balance" : "50000"}
]

customers.sort(key=lambda x:x["balance"])
print(customers)

print("\n----- ACCOUNT SUMMARY -----")
print("Customer Name:", customer_name)
print("Customer Age:", customer_age)
print("Branch:", branch_name)
print("Account Type:", account_type)
print("Balance:", remain_balance)
print("Highest Transaction:", highest_transaction)
print("Lowest Transaction:", lowest_transaction)
'''

print("College Admission Management System")

names = []
courses = []
marks = []
cities = set()
students = {}

for i in range(1,11):
    print(f"Student {i} details")
    name = input("Enter Name : ")
    age = input("Enter Age : ")
    course = input("Course : ")
    mark = input("Marks : ")
    city = input("City : ")
else:
    print("No data")

#stores name in a list
names.append(name)
#stores courses in a list
course.append(courses)
mark.append(marks)
#store unique cities in a set
city.add(cities)

#Store student details in a dictionary
students[name] = {
    "Age" : age,
    "Course" : course,
    "Marks" : mark,
    "City" : city
}

courses = tuple(courses)

print("\n Names List : ")
print(names)

print("\n Course Tuple : ")
print(courses)

print("\n Unique cities set ")
print(cities)

print("\n Student Details")
for name,details in students.item():
    print(name,":",details)

for i in range(1,11):
    avg_marks = marks/i

print(avg_marks)

topper_scorer=max(marks)
lower_scorer=min(marks)

students.sort(key=lambda x:x["marks"])
print(students)

for name,details in students.item():
    search_name = input("Enter name to search : ")
    if search_name == name:
        print(details)
    else:
        print("No valid details")

for name,mark in students.item():
    if mark > 75:
        print(f"{name} is eligible")
    else:
        print(f"{name} is not eligible")