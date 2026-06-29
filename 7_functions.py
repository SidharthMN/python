'''
def fuction_name(parameters):
    code to be executed

'''
'''
def greeting(user_name, age):
    print(f"Welcome {user_name}, You are {age} years old.")

user_name=input("Enter Name : ")
age = int(input("Enter Age : "))
greeting(user_name,age)
'''

'''
def addition (num1,num2):
    return num1+num2

num1= int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
print("Sum is : ",addition(num1,num2)) #result=addition(num1,num2) 
# print(result)
'''
'''    
def Welcome():
    print("Welcome Sidharth")
Welcome()

'''

'''
def book_ticket(movie_name,customer_name,seat,ticket_price):
    total = seat * ticket_price
    return f"{customer_name} booked {seat} tickets for {movie_name}.\n Total Amount : {total}"

print(book_ticket("Avatar","Sura",5,500))
print(book_ticket("Sura","Avatar",500,5))
'''
'''
print("\n Keyword Arguments")
def customer_details(customer_name,age,city):
    print(f"Customer Name : {customer_name} \n Customer Age : {age} \n Customer City : {city}")

customer_details(age=22,city="Chennai",customer_name="Shibu")
customer_details(customer_name="Sukhu",age=23,city="Trivandrum")
'''
'''
print("\n Default Arguments")

def booking_status(customer_name,status = "Confirmed",screen = "Screen 1"):  #parameter without a default first parameter with a default
    print(f"{customer_name}'s booking status : {status}")
    print(f"Screen Allocated : {screen}")

booking_status("Sashi")
booking_status("Shibu","Processing","Screen 3")
booking_status() # if customer_name="something"
'''

'''
print("\n Multiple Arguments")
#args
def calculate_bill(*ticket_prizes):
    print(f"Ticket Prizes : {ticket_prizes}")
    print(f"Total Bill :  {sum(ticket_prizes)}")
calculate_bill(140,190,170,200)

'''
'''
#kwargs
print("\n Multiple key word  Arguments")

def passenger(**details):
    print("Customer Infomation")
    for key,value in details.items():
        print(f"{key} : {value}")

passenger(name = "Sidharth" , seats = 2 , destination = "Trivandrum" , payment_status = "Pending")
passenger(name = "Shankar" , seats = 5 , city = "Chennai", payment_status = "Pending")
passenger(name = "Shibu" , seats = 10 , city = "Kaduvapokk", payment_status = "Pending")
'''
'''
print("built_in_function")
print(len("trueee"))
print(sum([3,5]))
print(min([3,4]))
print(max([3,4]))
print(abs(-4))
print(sorted([6,8,5,4,0,1,3,2]))
print(sorted([6,8,5,4,0,1,3,2],reverse=True))
'''
'''
languages=["malayalam","english","hindi","german"]
print(sorted(languages))
print(sorted(languages,reverse=True))

print(sorted(languages,key=len))
print(sorted(languages,key=len,reverse=True))
'''
#enumerate() 
# #in a colon in a function

'''LEGB RULE = LOCAL ENCLOSING GLOBAL BUILDING
#local variable
def student_details():
    name = "Sidharth M N"
    print("Student Name : ", name)
student_details()
#global variable
college_name = "Mohandas College of Engineering & Technology"
def display():
    print("College Name : ",college_name)
display()

def department():
    department_name = "Computer Science and Engineering" #enclosing variable
    def student():
        print("Department : ",department_name)
    student()
department()
'''
#Biling System , global variable = tax , function = shopping, enclosing = discount , bill(inner function), amount = amount-discount+tax
'''
tax = 100   #global variable               <=
def shopping():                            #||
    discount = 1000  #enclosing variable   <=
    def bill():                            #||
        amount= 5000  #local variable <== Scope
        total_amount = amount - discount + tax
        print(f"Amount : {amount} \n Discount : {discount} \n Tax : {tax} \n Total Amount : {total_amount}")
    bill()
shopping()
'''
'''
#Factorial of a Number
def factorial (num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)
      
print("The value is : ",factorial(5))

Working
5 * factorial (4)
4 * factorial (3)
3 * factorial (2)
2 * factorial (1)
1*2 =2 
factorial (2) =2 
3 * factorial (2) = 3*2 = 6
4 * factorial (3) = 4 *6 = 24

fact(5)
=5*fact(4)
=5*(4*fact(3))
=5*(4*(3*fact(2)))
=5*(4*(3*(2*fact(1))))


#Direct way
number =  int(input("Enter the number : "))
factorial = 1
for i in range(1,number+1):
    factorial*=number
print(number)


def add (a,b):
    return a + b
print(add(3,2)) 
'''

#lambda() function syntax

'''syntax : lambda arguments:expression'''
'''
add = lambda a,b:a+b
print(add(8,7))

square = lambda num:num*num
print(square(9))

largest = lambda a,b:a if a > b else b
print(largest(10,90))
'''

