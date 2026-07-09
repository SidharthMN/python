'''
s1="Python Lambda Function"
s2 = lambda func:func.upper()
print(s2(s1))

new_list=[1,2,3,4,5,6,7]
squared_list=list(map(lambda x:x*x,new_list))
print(squared_list)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, list2)) 
print(result)

#sorting
list_tuple=[
    ("Gouri",20,"Trivandrum"),
    ("Malavika",22,"Palakkad"),
    ("Aishu",24,"Idukki"),
    ("Janaki",21,"Kozhikode")
]

sorted_list=sorted(list_tuple,key = lambda element:element[1])
print(sorted_list)


new_set = (1,2,6,3,5,8)
multiplied = set(map(lambda item:item*10,new_set))
print(multiplied)

employees={
    "Arian":34,
    "Chandra":41,
    "Elias":25,
    "Franko": 31
}

sorted_dictionary = dict(sorted(employees.items(),key = lambda item:item[0]))
print(sorted_dictionary)
'''
'''
from functools import reduce

item_list = [10,20,30,40,50]
sum_of_elements = reduce(lambda x,y:x+y,item_list)
print(sum_of_elements)

#Create a constructor using lambda having name and marks as the parameters
#with accessing using self.name & self.marks
#Evaluate the student marks whether they pass or fail 
#define lambda in self.status
'''

#comprehension

'''syntax =[expression for item in iterable if condition]
numbers = [1,2,3,4,5,6,7,8,9]
odd_numbers = [item for item in numbers if item%2!=0]
print(odd_numbers)
'''
'''
lambda function (focuses on defining behaviour)
-used to create anonymous function
-performs a single expression and returnss a value
-syntax lambda arguments : expression
-commonly used with map filter and sorte
-returns a function object

comprehension (focuses on generating datas)
-used to create list,set or dictionaries in a concise way
-iterates over an iterable and generates a new collection
-syntax  [expression for item in iterable if condition]
-commonly used for transforming and filtering data.
-returns a list,set or dictionary 

'''
'''
item_list = [1,2,3,4,5,6]
result = tuple(x**2 for x in item_list)
print(result)
'''
'''
cubes = {item:item**3 for item in range(1,11)}
print(cubes)
elements_list = [1,4,2,5,3,6,2,4,1,6]
even_number={item for item in elements_list if item%2==0}
print(even_number)
'''
'''
roll_call = ["Arein","philip","parin","james","Zack","Pinas"]
upper_name = [item.upper() for item in roll_call]
print(upper_name)
check_a = [item for item in roll_call if 'A' in item]
print(check_a)
'''
'''
text = "Luxumberg"
#create a a list of vowels
#set of unique characters
#dictionary containing each characters and its ascii value

vowels=[ch for ch in text if ch in "aeiou"]
print(vowels)
unique_characters = {ch for ch in text}
print(unique_characters)
ascii_numbers = {ch:ord(ch) for ch in text}
print(ascii_numbers)
'''
#ord = char to number
#chr = number to char

'''
#student mark analysis 
mark_list = [70,45,55,65,60,80,90,40]
#list of passed students(marks greater tha or equal to 65)
#set of unique passed amrks
#dictionary containing mark and grade

passed_students = [mark for mark in mark_list if mark > 65]
print(passed_students)

unique_passed_marks = {mark for  mark in mark_list}
print(unique_passed_marks)

student_grade = {mark:("A" if mark >= 90 else "B" if mark >=80 else "C" if mark >= 70 else "D" if mark >= 60 else "E") for mark in mark_list}
print(student_grade)

#list of languages
# alist of word length
#set of first letters
#dictionary with word and length

languages = ["Python","Django","SQL","React"]
length = [len(ch) for ch in languages]
print(length)

first_letter = {ch[0] for ch in languages}
print(first_letter)

word_length = {ch:len(ch) for ch in languages}
print(word_length)
'''
#multiplication table
#list of multiples of 5
#set of multiples of 3
#dictionary presenting multiplication table of 7

number = range(1,11)
multiple_of_5 = [multiple*5 for multiple in number ]
multiple_of_3 = [multiple*3 for multiple in number]

multiple_of_7 = {multiple:multiple*7 for multiple in number}

print(multiple_of_3)
print(multiple_of_5)
print(multiple_of_7)