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
#Inheritance

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
