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
car = Car()
car.start_engine()
car.stop_engine()
car.headlights_on()
'''
