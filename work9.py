units = int(input("Enter units consumed: "))
bill = 0
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)
else:
    bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)

print("Electricity Bill =", bill)

#calculator

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", num1 + num2)
    elif choice == 2:
        print("Result =", num1 - num2)
    elif choice == 3:
        print("Result =", num1 * num2)
    elif choice == 4:
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Division by zero not allowed")
    elif choice == 5:
        print("Calculator Closed")
        break
    else:
        print("Invalid Choice")

#student grade system

total = 0

for i in range(1, 6):
    mark = int(input(f"Enter mark of subject {i}: "))
    total += mark

average = total / 5

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "F"

print("Total =", total)
print("Average =", average)
print("Grade =", grade)

#voting eligibility check

n = int(input("Enter number of people: "))

for i in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    if age >= 18:
        print(name, "is eligible to vote")
    else:
        print(name, "is not eligible to vote")

#number guessing game

secret = 25
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        print("Correct Guess")
        break

print("Total Attempts =", attempts)

#student attendance ststus checker

n = int(input("Enter number of students: "))

for roll in range(1, n + 1):

    if roll % 3 == 0 and roll % 5 == 0:
        print("Attendance Warning")
    elif roll % 3 == 0:
        print("Low Attendance")
    elif roll % 5 == 0:
        print("Eligible for Exam")
    else:
        print(roll)

#traffic signal simulation

seconds = int(input("Enter total seconds: "))

for sec in range(1, seconds + 1):

    if sec % 3 == 0 and sec % 5 == 0:
        print("YELLOW")
    elif sec % 3 == 0:
        print("RED")
    elif sec % 5 == 0:
        print("GREEN")
    else:
        print(sec)

#online order processing

start = int(input("Enter starting order ID: "))
end = int(input("Enter ending order ID: "))

for order_id in range(start, end + 1):

    if order_id % 3 == 0 and order_id % 5 == 0:
        print("Premium Customer Offer")
    elif order_id % 3 == 0:
        print("Express Delivery")
    elif order_id % 5 == 0:
        print("Discount Applied")
    else:
        print(order_id)

#library book categorization

n = int(input("Enter number of books: "))

for book_id in range(1, n + 1):

    if book_id % 3 == 0 and book_id % 5 == 0:
        print("Reference Book")
    elif book_id % 3 == 0:
        print("Science Book")
    elif book_id % 5 == 0:
        print("Literature Book")
    else:
        print("General Book")

#electricity bill alert system

start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

for customer_id in range(start, end + 1):

    if customer_id % 3 == 0 and customer_id % 5 == 0:
        print("Service Suspension Warning")
    elif customer_id % 3 == 0:
        print("High Usage Alert")
    elif customer_id % 5 == 0:
        print("Payment Due")
    else:
        print(customer_id)