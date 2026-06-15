'''student_name=input("Enter the student name : ")
student_id=int(input("Enter the student id : "))
student_mark=input("Enter the student mark : ")
true_false=bool(input("If the student attended the course (T/F) : "))
languages_known=input("Enter the languages known : ").split(",")

print("The name of the student is", student_name)
print("The id of the student is", student_id)
print("The mark of the student is", student_mark)
print("He has attended the course ", true_false)
print("Languages known by the student are ", languages_known)

print(type(student_name))
print(type(student_id))
print(type(student_mark))
print(type(true_false))
print(type(languages_known))'''

num1=10
num2=10

print("ID OF num1 : ",id(num1))
print("ID OF num1 : ",id(num2))

arr1=["a","b","c"]
arr2=["a","b","c"]

print("ID OF arr1 : ",id(arr1))
print("ID OF arr2 : ",id(arr2))

print(isinstance(num1,int))
print(isinstance(arr1,list))
print(isinstance(arr1[0],str))