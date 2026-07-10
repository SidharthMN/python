'''
def addition(num1,num2):
    return num1+num2

print(addition(10,20))

def pure_function(list1):
    new_list=[]
    for item in list1:
        new_list.append(item*2)
    return new_list
#print(pure_function([1,2,3,4,5]))
original_list=[1,2,3,4,5]
modified_list=pure_function(original_list)
print(original_list)
print(modified_list)

def calculate_final_amount(price,quantity,tax_discount):
    total_amount = price*quantity
    final_amount=total_amount+tax_discount
    print(f"Final Amount to be paid : {final_amount}")
    print(f"Total Amount : {total_amount}")
calculate_final_amount(120,20,10)

#assign function to a variable

def greet(name):
    return f"Hello {name}!"

message=greet("Sidharth")
print(message)

#passing a function as an argument

def greet():
    print(f"Hello,World!")

def display_message(func):
    func()
display_message(greet)

#return a function from another function
def outer():
    def inner():
        print("Hello from inner function!")
    return inner
result = outer()
result()

#store func in a list
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
functions = [add , subtract]
print(f"Addition: ",functions[0](10,5))
print(f"Substraction: ",functions[1](10,5))
'''
'''

def email_notification():
    print("Sending email notification....")
def sms_notification():
    print("Sending SMS Notification....")
def send_notification(notification_type):
    if notification_type == "email":
        email_notification()
    elif notification_type == "sms":
        sms_notification()
    else:
        print("Invalid notification type.")
send_notification("sms")

#first class function : what a function can do acts as an object
#higher order : what a function does

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def calculate(operation,x,y):
    return operation(x,y)

result1= calculate(add,10,5)
result2 = calculate(subtract,10,5)
print("Addition : ",result1)
print("Substraction : ",result2)
'''
'''
#function defining another function
#iterators

iter_list = iter([10,20,30,40,50])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
'''
'''
#generators

def countdown(n):
    while n > 0:
        yield n
        n-=1

count = countdown(10)
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
'''
'''

def squared_num():
    for num in range(1,11):
        yield num*num
numbers=squared_num()
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

#work : inside a function create a file using context manager using iteration
'''

#decorators
def decorator_pgm(func):
    def wrapper(*args):
        print("Calculating two numbers....")
        result = func(*args)
        print("Final Output Obtained ")
        return result
    return wrapper

@decorator_pgm
def add(num1,num2):
    return num1+num2

@decorator_pgm
def sub(num1,num2):
    return num1-num2

print(add(22,22))
print(sub(22,22))

#find missing number from a set 1 to 7 without 2 insde the set