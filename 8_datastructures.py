'''
username = "Sidharth"
# 0  1  2  3  4  5  6  7
# S  i  d  h  a  r  t  h  index start from zero(positive indexing)
#-8 -7 -6 -5 -4 -3 -2 -1

print("User Name : ",username)
print(username[-5])
print(username[3])
'''
'''
#slicing
data = "Python is a Programming Language."
     start:stop:skip
print(data[1:8:3])
print(data[10:4:-2])
print(data[::3])
print(data[:3])
print(data[-1:-11:-1])
print(data[::-1])
'''

'''
car = "Porsche Panamera"
print(car.upper())
print(car.lower())
print(car.capitalize())
print(car.title())
print(car.startswith("P"))
print(car.endswith("r"))
print(car.replace("Porsche", "GTS"))
#car[3]="a"  /n  print(car)
print(id(car))
uppercase = car.upper()
print(id(uppercase))
'''
'''
#list
user_data = ['Sidharth','Balaramapuram',24,'Glamour X']
print(user_data)
user_data.insert(2,"B.Tech")
print(user_data)
user_data.append("brba")
print(user_data)
user_data.extend("python")
print(user_data)
user_data.append(["mal","eng"])
print(user_data)
user_data.extend(["java","ruby"])
print(user_data)
print(user_data[12])
print(user_data[12][0])
user_data.remove("Sidharth")
print(user_data)
user_data.pop(2)
print(user_data)
user_data.reverse()
print(user_da0a)

#user_data.sort() #Dont mix list , str and numbr
                 #should have same datatype
'''#tuple
'''
tuple1 = (10,20,30,40)
print(tuple1)

nested_tuple=((10,20,30,40,50),21,"sidharth","tvm")
print(nested_tuple)
#try indexing sliccing
#try out immutability

person=("sidharth",24,"tvm")
name,age,place = person
print(name)
print(age)
print(place)

number = (10,20,30,40,50)
A,B,*C = number
print(A)
print(B)
print(C)
D,*E,F = number
print(D)
print(E)
print(F)


value = (2,3,4,5,6,2,6,2,5,6,2,6)
print(len(value))
print(value.count(6))
print(value.index(3))
print(value[3])
'''
'''
userdata = input("Enter a string : ")
count=0
for item in userdata:
   count += 1
print(count)
'''
'''
#print first non repeating character
user_input = input("Enter a string : ")
count=0
for item in user_input:
   if user_input.count(item) == 1:
      print("First Non Repeating character",item)
      break
else:
     print("NO REPEATING CHARACTERS")
'''
'''
#print second non repeating number

student1 = {"Eng","Hin","Mal"}
student2 = {"Eng","Hin","Python"}
student3 = {"Urdu","Python","Hin"}
student1.add("c") #not multiple elements like list
print(student1)
student1.update(["css","java"]) #supports multiple elements
print(student1)

#student1.add(["html","django"])

student1.add("Mal")
print(student1)

student1.remove("Hin")
print(student1)

#student1.remove("Javascript")
#print(student1)

student1.discard("javascript")
print(student1)

student1.pop("javascript")
print(student1)

#union , intersection , difference 
'''
'''
student1 = {"English","Hindi","Malayalam"}
student2 = {"English","Hindi","Python"}
student3 = {"Urdu","Python","Hindi"}

print(student1.union(student2))
print(student1.intersection(student2))
print(student1.difference(student2))

print(student1 | student3)
print(student1 & student3)
print(student1 - student3)

#disjoint sets

set1 = {1,2,3}
set2 = {7,8,9}
set3 = {4,5,6}

print(set1.isdisjoint(set2))
print(set2.isdisjoint(set1))
'''
'''
#frozen set

fs1 = frozenset("sidharth")
fs2 = frozenset([12,23,24])
fs3 = frozenset((11,22,33))

print(fs1)
print(fs2)
print(fs3)
'''
#dictonary

student = {
    "name" : "Sidharth",
    "age" : 24 ,
    "place" : "Balaramapuram"
}

print(student)
print(student["name"])
print(student.get("marks"))
student["marks"] = 55
print(student)
student.pop("age")
print(student)
del student["name"]
print(student)

student.update({"marks":88 ,"nationality":"brazil"})
print(student)

info = dict(city = "Trivandrum", location = "Kerala")
print(info.keys())
print(info.values())
print(info)

#try out update function for multiple insertions

employee = {
    "emp1" : {
        "name" : "Sidharth",
        "age" : 24
    },
    "emp2" : {
        "name": "George",
        "age" : 30
    },
    "emp3" : {
        "name" : "Shah",
        "age" : 27
    },
    "emp4" : {
        "name" : "Jacky",
        "age" : 25  
    }
}

print(employee["emp3"]["age"])