'''print("Arithmetic Operators")

price_per_book = 500
quantity = 25
total = price_per_book * quantity
avg = total/quantity
extra_charge = 50
final_price = total + extra_charge
discount = 25
final_price -= discount 
remainder = final_price % quantity
floor_division = final_price // 7
squared_value = price_per_book ** 2

print("Price of one book is : ",price_per_book)
print("Quantity of books are : ",quantity)
print("Total price of books are : ",total)
print("Average amount of books are : ",avg)
print("Extra charge of book is : ",extra_charge)
print("Discount of book is : ",discount)
print("Final price of books are : ",final_price)
print("Remainder is : ",remainder)
print("Floor division is : ",floor_division)
print("Squared value is : ",squared_value)'''

'''print("Assignment Operators")

score = 100
score += 50
print("Score : ",score)
score -= 20
print("Score : ",score)
score *= 2
print("Score : ",score)'''


'''print("Logical Operators")
username = "sid.xoid"
password= "*****"
entered_username = input("Enter the username : ")
entered_password = input("Enter the password : ")
if entered_username == username and entered_password == password:
    print("Login Successfull")
else:
    print("Invalid Login")
'''

'''
current_day= input("Enter a day : ")
if current_day == "Saturday" or current_day == "Sunday":
   print ("It's a holiday")
else :
   print("It's a working day")

'''
#not
'''
logged_in = False
if not logged_in :
    print("Welcome User")
else : 
    print("Please login")
'''

'''
print("Membership Operator")
movies = ["Drishyam","Micheal","Titanic"]
movie = input("Enter the movie name : ")
if movie in movies:
    print("Movie Available")
else:
    print("Movie not available")
'''
'''
employees = ["user1","user2","user3"]
name = input("Enter employee name : ")
if name not in employees :
    print("Access Denied")
else : 
    print("Access Granted")
'''

#Identity Operator
'''
#initialization is different than input
value1 = input("Enter the first value : ")
value2 = input("Enter the second value : ")
print(value1 is value2)
print(value1 == value2)
'''

'''
value1 = 100
value2 = 100
print(value1 is value2)
print(value1 == value2)

'''


'''
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)
print(list1 == list2)
'''

'''
languages = ["Python","Java","C++"]
selected_language = languages[0]
print(selected_language is languages[0])
print(selected_language is "Python")
print(selected_language is "Django")
'''


'''
list1 = [10,20,30]
list2 = [10,20,30]
print(list1 is list2)
print(list1 == list2)
list3 = list1
print(list3 is list1)
print(list3 == list1)
'''

a = 5
b = 3
print(bin(a))
print(bin(b))
print(a & b)
print(bin(a | b))
print(bin(a ^ b))
print(bin(~a))

#left shift (a*2^b)
print(bin(a << 1))
#right shift (a/2^b)
print(bin(a >> 1))

