'''
#Online shop

purchase_amount = float(input("Enter Purchase Amount: "))
premium_member = input("Premium Member (yes/no): ").lower()
discount_percentage = float(input("Discount Applied : "))

discount_value = purchase_amount * discount_percentage / 100
final_bill_amount = purchase_amount - discount_value

if premium_member == "yes":
    final_bill_amount = final_bill_amount-200
else:
    final_bill_amount = final_bill_amount

print("Final Bill Amount : ",final_bill_amount)
'''

'''
#University Admission Eligibility

higher_sec_percent= float(input("Enter Higher Secondary Percentage : "))
maths_percent= float(input("Enter Maths Percentage : "))
entrance_score = float(input("Enter Entrance Score : "))

if higher_sec_percent > 80 and maths_percent > 70 and entrance_score > 80:
    print("Admission Status : Eligible")
    print("Suggested Course : Computer Science")
elif higher_sec_percent > 70 and maths_percent > 60 and entrance_score > 70:
    print("Admission Status : Eligible")
    print("Suggested Course : Civil Engineering")
elif higher_sec_percent > 60 and maths_percent > 50 and entrance_score > 60:
    print("Admission Status : Eligible")
    print("Suggested Course : Mechanical Engineering")
else:
    print("Admission Status : Not Eligible")
'''

'''
#Loan approval System

age = int(input("Enter Age : "))
salary = float(input("Enter Salary : "))
credit_score = int(input("Enter Credit Score : "))
loan_status = input("Existing Loan (yes/no) : ").lower()
if loan_status == "yes":
    print("Existing Loan is present")
else:
    print("No Existing Loan present")

if salary>=25000 and credit_score>=500:
    print("Loan Status : Approved")
else:
    print("Loan Status : Not Approved")
''' 

'''
#Hospital Patient Priority System

age = int(input("Enter Age : "))
condition = input("Enter Condition (critical/severe/mid) : ").lower()

if condition == "critical":
    print("Priority Category : High Priority")
elif condition == "severe":
    print("Priority Category : Medium Priority")
elif condition == "mid":
    print("Priority Category : Low Priority")
else:
    print("Invalid , Please try again")
'''

'''
#Employee Bonus Management

year_of_service = int(input("Enter Years of Service : "))
performace_rating = input("Enter Performance Rating (Excellent/Average/None) : ").lower()
attendance_percentage = float(input("Enter Attendance Percentage : "))
if performace_rating not in ["excellent", "average", "none"]:
    print("Performance rating is invalid")
else:
    if year_of_service >= 5 and performace_rating=="excellent" and attendance_percentage >= 90:
        print("Bonus Percentage : 20%")
        print("Bonus Amount : 10000")
    elif year_of_service >= 5 and performace_rating=="average" and attendance_percentage >= 90:
        print("Bonus Percentage : 10%")
        print("Bonus Amount : 5000")
    elif year_of_service >= 5 and performace_rating=="none" and attendance_percentage >= 90:
        print("Bonus Percentage : 5%")
        print("Bonus Amount : 2500")
    else : 
        print("Not Eligible for Bonus")
'''

'''
#Smart Traffic Fine System

helmet_worn = input("Helmet Worn (yes/no) : ").lower()
seatbelt_usage = input("Seatbelt Usage (yes/no) : ").lower()
speed_violation = input("Speed Limit Violation (yes/no) : ").lower()
valid_license = input("Valid License (yes/no) : ").lower()

fine = 0
if helmet_worn == "no":
    fine += 500

if seatbelt_usage == "no":
    fine += 500

if speed_violation == "yes":
    fine += 1000

if valid_license == "no":
    fine += 2500

if fine > 0:
    print("Total Fine:", fine)
else:
    print("No Fine")
'''

'''
#Cinema Ticket Booking System

age = int(input("Enter Age : "))
seat_type = input("Seat Type (Normal/Premium) : ").lower()
day_type = input("Seat Type (Weekday/Weekend) : ").lower()
student = input("Student (yes/no) : ").lower()

if seat_type == "normal":
    ticket_cost = 200
elif seat_type == "premium":
    ticket_cost = 400
else:
    ticket_cost = 0

if day_type == "weekend" and student == "yes":
    ticket_cost -= 120
elif day_type == "weekend":
    ticket_cost -= 100
elif student == "yes":
    ticket_cost -= 20
else:
    print("No Discount")

print("Final Ticket Cost : ",ticket_cost)
'''

'''
#Scholarship Eligibility System

family_income = int(input("Enter Family Income : "))
academic_percent = float(input("Enter Academic Percentage : "))
attendance_percent = float(input("Enter Attendance Percentage : "))

if family_income <= 200000 and academic_percent >= 75 and attendance_percent >= 90:
    print("Schloarship Status : Full Scholarship")
elif family_income <= 500000 and academic_percent >= 80 and attendance_percent >= 90:
    print("Schloarship Status : Half Scholarship")
elif family_income > 500000:
    print("Schloarship Status : No Scholarship")
else:
    print("Not Eligible")
'''


'''
#Student performance analytics system
sum = 0
for i in range (5):
    marks = int(input("Enter Marks in 5 Subjects: "))
    sum = sum + marks
print("Total Marks : ",sum)
percentage = float((sum / 500)* 100)
print("Percentage : ",percentage)

if percentage <= 100 and percentage >= 90:
    print("Grade : A +")
elif percentage <= 89  and percentage >= 80:
    print("Grade : A ")
elif percentage <= 79  and percentage >= 70:
    print("Grade : B + ")
elif percentage <= 69  and percentage >= 60:
    print("Grade : B ")
elif percentage <= 59  and percentage >= 50:
    print("Grade : C + ")
else:
    print("Grade : F ")

if percentage >= 50 :
    print("Result : Pass")
else:
    print("Result : Fail")

if percentage >= 50 :
    print("Promotion Status: Eligible ")
else:
    print("Promotion Status: Not Eligible ")

'''





