class CustomException(Exception):
    pass
def check_number(num):
    if num < 0:
        raise CustomException("Not allowed negative numbers")
    return num
try:
    result = check_number(22)
    print(result)
except CustomException as e:
    print(e)  

name = input("Enter the name : ")
if len(name) < 5:
    raise CustomException("Name too short")

try:
    print(name)
except CustomException as e:
    print(e)

#bubble sort
numbers = [12,24,15,17,16]
def bubblesort (num):
    n=len(num)
    for i in range(n):
        for j in range(i+1,n):
            if num[i]<num[j]:
                num[j],num[i]==num[i],num[j]
    return num

print(bubblesort(numbers))                


           