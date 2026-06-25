'''
#Prime number

number = int(input("Enter a number : "))
if number <= 1 :
    print("Not a Prime Number")
else:
    is_prime = True
    for i in range(2,int(number//2)+1):
       if number%i == 0:
          is_prime = False
          break
    if is_prime == True:
       print("It is a prime number")
    else:
       print("Not a prime number")   
'''
'''
#fibonacci series


n = int(input("Enter a number : "))
a = 0
b = 1

for i in range(n):
   print(a,end=",")
   c = a+b
   a = b
   b = c
'''
'''
#palindrome

number = int(input("Enter a number : "))
temp =number
reverse = 0
while number > 0:
   remainder = number%10
   reverse = reverse*10+remainder
   number = number//10

if temp == reverse:
   print("Number is Palindrome")
else:
   print("Not a palindrome")

#Palindrome - String

str = input("Enter a string : ")
rev = ""

for i in str:
   rev = i + rev

if str == rev:
   print(f"{rev} is a Palindrome")
else:
   print("Not a palindrome")

'''
'''
#count the number of digits
number = int(input("Enter a number : "))
count = 0
temp = abs(number)

if temp == 0:
   count = 1
else:
   while temp > 0:
     temp = temp//10
     count+=1

print("Count is :",count)
'''
'''
#Sum of digits
number = int(input("Enter a number : "))
sum_digits = 0
temp = abs(number)

while temp > 0:
   digit = temp%10
   sum_digits += digit
   temp = temp//10

print("Sum of digits : ",sum_digits)
'''
'''
#Product of digits
number = int(input("Enter a number : "))
product_digits = 0
temp = abs(number)

while temp > 0:
   digit = temp%10
   product_digits *= digit
   temp = temp//10

print("Product of digits : ",product_digits)
'''
'''
#ATM 
correct_pin = 2255
balance =100000
attempts = 0

while attempts<3:
   pin = int(input("Enter the pin :"))
   if pin == correct_pin:
      print("Login Successfull")
      while True:
         print("\n1.Balance Check")
         print("2.Withdraw")
         print("3.Deposit")
         print("4.Exit")
         choice = int(input("Enter a choice : "))
         if choice == 1:
            print("Balance: ",balance)
         elif choice == 2:
            amount = int(input("Enter the withdrawal amount : "))
            if amount <= balance:
               balance -= amount
            else:
               print("Insufficient balance")
         elif choice == 3:
            amount = int(input("Enter the amount to be deposited : "))
            balance += amount
            print("Amount deposited successfully.")
         elif choice == 4:
            print("Thank you")
            break
         else:
            print("Invalid choice")
      break
   else:
      attempts += 1
      print("Incorrect PIN")
else:
   print("Account blocked")
'''
'''
#Seat Availability System
available_seats = 35

while available_seats > 0:
   print("Available Seats are : ",available_seats)
   book_seats = int(input("Enter the number of seats to be booked : "))
   if book_seats <= available_seats:
      available_seats -= book_seats
      print(f"{book_seats} seats are booked successfully")
      remaining_seats = available_seats
      print("Remaining Seats are : ",remaining_seats)
   else:
      print("Seats are not available")
   choice = input("Do you want to continue (Yes/No): ").lower()
   if choice == "no":
      break
print("Booking closed")
'''
'''
#Fizzbuzz patern
start_value = int(input("Enter the value to start : "))
end_value = int(input("Enter the value to end : "))
for num in range(start_value,end_value+1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num% 5 == 0:
        print("Buzz")
    else:
        print(num)
'''
'''
#find the largest and smallest number in a list
numbers = []
n = int(input("Enter the numbers to add in list : "))
for i in range (n):
   num = int(input(f"Enter number {i+1}: "))
   numbers.append(num)
largest=numbers[0]
smallest=numbers[0]
for num in numbers:
   if num > largest:
      largest = num
   if num < smallest:
      smallest = num
print("Largest of given number : ",largest)
print("Smallest of given number : ",smallest)
'''
'''
#10,15,21,3,8
largest=10
smallest=10
num=10
num=15
10>15 False
10 < 15
largest =15
num =21
21 > 10
'''
'''
numbers=tuple(map(int,input("Enter the numbers to be inserted : ").split(",")))
elements=int(input("Enter the element : "))
count = 0
for item in numbers:
   if item == elements:
      count+=1
print("Tuple elements are :",numbers)
print(f"Occurance of {elements} is : {count}")
'''


'''input = 1 2 3 4 5 6
target = 6
output = [1,5][2,4][3,3]
'''
'''
numbers=tuple(map(int,input("Enter the numbers to be inserted : ").split(",")))
target=int(input("Enter the target sum : "))

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print((numbers[i], numbers[j]))
'''

#reverse of a dictionary

data = {
    "a": 1,
    "b": 2,
    "c": 3,
}
reverse_data={}
keys = list(data.keys())
for key in keys[::-1]:
    reverse_data[key]=data[key]
print(reverse_data)
print(type(reverse_data))