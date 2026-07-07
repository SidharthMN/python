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