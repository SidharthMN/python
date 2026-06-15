'''
#Employeee Salary Report Generator
salary = 0
for i in range(1,6):
    temp = int(input(f"Enter the salary of Employee {i} : "))
    salary += temp
print("Total Salary Expenditure : ",salary)
'''
'''
#Student Attendance Counter
present = "P"
absent = "A"
present_count = 0
absent_count = 0
for i in range(1,11):
    temp = input(f"Student {i} Attendance: ")
    if temp == "P" :
        present_count += 1
    elif temp == "A":
        absent_count += 1
    else:
        print("Invalid")

print("Total Present Students : ",present_count)
print("Total Absent Students : ",absent_count)
'''
'''
#Supermarket Billing System
amount = 0
for i in range(1,6):
    temp = int(input(f"Item {i} Price : "))
    amount += temp
print("Total Bill Amount : ",amount)
'''

'''
#Cricket Score Analyzer
score= 0
for i in range(1,7):
    temp = int(input(f"Ball {i} Runs : "))
    score += temp
print("Total Runs Scored : ",score)
'''
'''
#Cricket Score Analyzer
books= 0
for i in range(1,8):
    temp = int(input(f"Section {i} Books : "))
    books += temp
print("Total Books in Library : ",books)
'''
'''
# Online Exam Marks Calculator 
marks = 0
for i in range(1,6):
    temp = int(input(f"Subject {i} Marks : "))
    marks += temp
    avg = marks/i
print("Total Marks: ",marks)
print("Average Marks: ",avg)
'''
'''
#Daily Temperature Monitor 
highest_temperature=0
for i in range(1,7):
    temp = int(input(f"Enter {i} temperature : "))
    if temp > highest_temperature:
        highest_temperature = temp
print("Highest Temperature : ",highest_temperature)
'''

'''
#Mobile Recharge Collection System
recharge = 0
for i in range(1,11):
    temp = int(input(f"Cusstomer {i} Recharge : "))
    recharge += temp
print("Total Collection : ",recharge)

'''
'''
#Mobile Recharge Collection System
water = 0
for i in range(1,8):
    temp = int(input(f"Day {i} Consumption : "))
    water += temp
print(f"Total Water Consumed : {water} litres")
'''
'''
#Total Annual Production
production = 0
for i in range(1,13):
    temp = int(input(f"Month {i} Production : "))
    production += temp
print(f"Total Annual Production : {production}  Units ")
'''
