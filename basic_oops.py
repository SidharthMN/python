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