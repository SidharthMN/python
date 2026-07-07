'''
class Student:
    def display(self): #self represents the cuurent object/instance of a class
        print("I am a student")
student = Student() #object creation
student.display()

class Employee:
    def __init__(self): #Constructor are used of initializing objects and it are called when the object is created
        print("Default Constructor is called")
emp = Employee()

class Car:
    colour = "red" #class variable
    def __init__(self,brand,model):
        self.brand = brand  #instance variable
        self.model = model   
car = Car("Porsche",911)
print(car.brand,car.model,car.colour)

car1 = Car("BMW","M5")
print(car1.brand,car1.model)

# self = each object maintains its own data
# method can access object properties
#without self = cannot access object variables 
# can't store data seperately for each object 
# method cannot know which object called them

class Library:
    def __init__(self,name,location="Trivandrum",total_books=0):
        self.name = name
        self.location = location
        self.total_books = total_books
library = Library("Sukhu")
print(library.name,library.location,library.total_books)

library1 = Library("Shibu","Kollam")
print(library1.name,library1.location,library1.total_books)

library2 = Library("Thanos","Kochi",10)
print(library2.name,library2.location,library2.total_books)

'''
'''
#Single Inheritance

class User: #parent class/base class/super class
    def login(self):
        print("User Logged In")

class Influencer(User): #child class/sub class/derived class
    def post_reels(self):
        print("Influencer posted a new reel")


influencer = Influencer()
influencer.login()
influencer.post_reels()

#Multi-Level Inheritance

class Vehicle:
    def category(self,name,mode):
       print("Category : ",name)
       print("Mode of transport : ",mode)

class Car(Vehicle):
    def vehicle_category(self,category,variant,colour):
        print("Type of Vehicle : ",category)
        print("Variant of Vehicle : ",variant)
        print("Colour of Vehicle : ",colour)

class ElectricCar(Car):
    def car_type(self,brand,category,variant,price):
        print("Car Brand : ",brand)
        print("Car Category : ",category)
        print("Car Variant : ",variant)
        print("Car Price : ",price)

electriccar = ElectricCar()
electriccar.category("Car","Road")
electriccar.vehicle_category("SUV","AWD","Black")   
electriccar.car_type("Porsche","Macan","Electric",12162000.00)
'''
'''
#Multiple Inheritance

class ImageUpload:
    def picture_upload(self,user_name,picture_name):
        print(f"The {picture_name} from {user_name} uploaded successfully.")

class ReelUpload:
    def reel_upload(self,user_name,reel_name):
        print(f"{user_name} uploaded {reel_name}")

class Instagram(ImageUpload,ReelUpload):
    def user_analytics(self,user_name,owner,reaction):
        print(f"{user_name} is having a {owner} account with {reaction} on the post.")

instagram = Instagram()
instagram.picture_upload("sid.xoid","pic1")
instagram.reel_upload("sid.xoid","reel1")
instagram.user_analytics("pamman.memes","sid.xoid","like")

#hybrid(multiple + multilevel)
#hierarchy(3 child class access from parent 1 parent - 3 child)
'''
'''
#polymorphism

#method overloading 
# same method ,same class, different parameters

print(len("chichichi"))
print(len([10,20,30,40,50,60,70,80,90]))

class Calculator:
    def add(self,num1=0,num2=0,num3=0):
      return num1+num2+num3
    
calculator = Calculator()
print(calculator.add(9,8,0))
print(calculator.add(-1,3,5))
print(calculator.add(10,20,5))
'''
'''
#Example 2 : 
email = input("Enter the e-mail : ")
password = input("Enter the password : ")
phone_no = input("Enter the phone number : ")
class Facebook:
   def login(self,email=None,password=None,phone_no=None):
      if email and password :
         print(f"Login through Email ID : {email}")
      elif phone_no and password:
         print(f"Login through Mobile Number : {phone_no}")
      else:
         print("Invalid Login")

facebook = Facebook()

if email:
   facebook.login(email=email,password=password)
else:
   facebook.login(phone_no=phone_no,password=password)
'''
'''
class Payment:
   def pay(self,amount,method="cash"):
      if method == "cash":
         print(f"{amount} is collected via cash")
      elif method == "upi":
         print(f"{amount} is collected via upi")
      elif method =="card":
         print(f"{amount} is collected via card")
      else:
         print(f"{amount} is not received")

payment = Payment()
payment.pay(540)
payment.pay(720,method="upi")
payment.pay(1200,method="card")
'''
'''
#Method Overriding
#different class, same method , same parameters

class Employee:
   def work(self):
      print("Working as Employee")
   def skill(self):
      print("Python full stack intern")
class Manager(Employee):
   def work(self):
      super().work()
      print("Managing Team")



manager=Manager()
manager.work()
manager.skill()

'''
'''
class Order:
    def order_details(self,product_name,quantity):
        print(f"Order placed for {quantity} {product_name}.")

class OnlineOrder(Order):
    def order_details(self,product_name,quantity,address):
        super().order_details(product_name,quantity)
        print(f"Order delivered to {address}")

online_order=OnlineOrder()
online_order.order_details("Munch",5,"Bakery Junction")
'''
#abstraction : hiding implementation details from the user
'''
from abc import ABC , abstractmethod
class Vehicle(ABC):
    #decorators
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    @abstractmethod
    def headlights_on(self):
        print("Headlights are on")

class Car(Vehicle):
    def start_engine(self):
        print("Car started using key.")
    def stop_engine(self):
        print("Engine stopped using key")

vehicle = Vehicle()
vehicle.start_engine()
vehicle.stop_engine()
vehicle.headlights_on()
'''

'''
car = Car()
car.start_engine()
car.stop_engine()
car.headlights_on()
'''
'''
#encapsulation
class Person:
    def __init__ (self,name,age):
        self.name = name
        self.__age = age  #private variable

    def show_age(self):
        print(self.__age)

person = Person("Abhi",23)
print(person.name)
person.show_age()
'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age #private variable

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
       if age > 0:
           self.__age = age

person = Person("Abhi",23)
print(person.name)
print(person.get_age())
person.set_age(25)
print(person.get_age())
'''

    
#data hiding mechanism by using rivate variables
class Library:
    def __init__ (self,student_name):
        self.student_name=student_name
        self.__books_issued = 0
        print(student_name)
'''

#method overloading:same class,same method,different arguments

"""class Facebook:
    def login(self,email=None,password=None,phone_number=None):
        if email and password:
            print(f"Login through Email ID: {email}")
        elif phone_number and password:
            print(f"Login through Mobile Number: {phone_number}")
        else:
            print("Invalid Login")

facebook=Facebook()
facebook.login(email="arunagsnair18@gmail.com",password="arunag39")
facebook.login(phone_number=7492028738,password="arunag39")"""

"""class Payment:
    def pay(self,amount,method="cash"):#it is default
        if method=="cash":
            print(f"{amount} is collected via {method} method.")
        elif method=="upi":
            print(f"{amount} is collected via {method} method.")
        elif method=="card":
            print(f"{amount} is collected via {method} method.")

payment=Payment()
payment.pay(540)#ivde method specify chynda becz default ait cash enn koduthitund
payment.pay(350,method="upi")
payment.pay(670,method="card")"""

#over riding...diferent classs,same method,same parameters

"""class Employee:
    def work(self):
        print("Working as Employee")
    def skill(self):
        print("Python full stack Intern")

class Manager(Employee):
    def work(self):s
        super().work()#superkeyword
        print("Managing Team")

manager=Manager()
manager.work()
manager.skill()"""
'''
class Order:
    def order_details(self,product_name,quantity):
        print(f"Order placed for {quantity} Qty {product_name}.")

class OnlineOrder(Order):
    def order_details(self,product_name,quantity,address):
        super().order_details(product_name,quantity)
        print(f"Order Delivered to {address}")

online_order=OnlineOrder()
online_order.order_details("Cinthol",4,"Bakery Junction")'''

#Abstarction..hiding the implementation details from the user
#class abc it is from abc module


"""from abc import ABC,abstractmethod
class Vehicle(ABC): #ABC is a class here 
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass#here pass for future purposes
    def headlights_on(self):
        print("Headlights are set to low")

class Car(vehicle):
    def start_engine(self):
        print("Car started using key.")
    def stop_engine(self):
        print("Engine stopped using key")"""
'''
vehicle=Vehicle()
vehicle.stop_engine()
vehicle.start_engine() 
vehicle.headlights_on()
'''
"""car=Car()
car.start_engine()
car.stop_engine()
car.headlights_on()"""

#encapsulation....hiding the data 
#data hiding mechanism by using private variables

"""class Person:
    def _init_(self,name,age):
        self.name=name
        self.__age=age#private varible

    def show_age(self):
        print(self.__age)    

person=Person("Aruna",21)
print(person.name)
print.show_age()"""   

"""class Person:
    def _init_(self,name,age):
        self.name=name#publically accesible 
        self.__age=age#private variable

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Age must be Positive !!!") 
person=Person("Aruna",21)
print(person.name)   
print(person.get_age())
person.set_age(23)
print(person.get_age())"""


"""class Library:
    def _init_ (self,student_name):
        self.student_name=student_name
        self.__books_issued=0#private variable
        print(student_name)
    def set_books(self,count):
        if count>=0:
            self.__books_issued=count
        else:
            print("Invalid Book Count")

    def issue_book(self):
        self.__books_issued+=1
        print("Book Issued Successfully")

    def return_book(self):
        if self.__books_issued>0:
            self.__books_issued-=1
             print("Book Returned Successfully")
        else:
            print("No Books To Returned !!!!")  

    def get_books(self):
        return self.__books_issued     

library=Library("Aruna")
library.issue_book()
library.issue_book()       
library.issue_book()
library.return_book()
print(f"Total Books : {library.get_books()}")"""

class BankAccount:
    def _init_(self,account_holder,balance,pin):
        self.account_holder=account_holder #public variable
        self._balance=balance #protected variable
        self.__pin=pin#private variable

    #public method
    def deposit(self,amount):
        print("Public Method for Depositing")




