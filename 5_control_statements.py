#for loop
'''
for variable in sequence:
    code to be executed
'''

'''
word = input("Enter a word :")


for letter in word:
    print(letter,end=" ")
'''

'''
for element in [1,2,3,4]:
    print(element)
'''
#Using Range Function
'''
for variable in range(start,stop,skip):
    code to be executed
'''

'''
for element in range(11):
    print(element)
'''

'''
for element in range(5,16):
    print(element)
'''

'''
for element in range(10,26,5):
    print(element)
'''

#Doesn't Work
'''
for element in range(1,10,-1):
    print(element)
'''

'''
for element in range(10,0,-1):
    print(element)
'''
'''
for element in range(17,3,-3):
    print(element)
'''
'''
num = int(input("Enter a number : "))
for i in range(1,11):
    print(i,"*",num,"=" ,num*i)
    print(f"{i} * {num} = {num*i}")'''  #printing using formatting string

#while loop
'''
initialisation
while condition:
    code to be executed
    updation
'''

'''
value = 1
while value<=10:
    print(value)
    value+=1
'''
#find sum till iteration
'''
value = 1
sum = 0
iteration = int(input("Enter the number of iterations : ")) 
while value <= iteration:
    sum += value
    value+= 1
print(sum)

'''
#reverse a number
#step 1 : getting the last digit
# 165 % 10 = 5
#step 2 : remove the last digit
#165 / 10 = 16
#step 3 : build reversed number
#reverse = 0
#reverse = reverse*10+digit
#0*10+5
#5*10+6
'''   
number = int(input("Enter the number to get reversed : "))
reverse = 0
while number > 0:
    remainder = number%10
    reverse=reverse*10+remainder
    number//=10
print(reverse)
'''

'''number = 165
   165 > 0 is True
   165%10 is 5
   reverse = 0*10+5=5
   number = 165//10=16
   still 16 > 0

   number =16
   16>0 is true
   remainder = 16%10 is 6
   reverse = 5*10=6
   number = 16//10= 1
   
   number=1
   1>0 is true
   remainder = 1%10 = 1
   reverse = 56*10+1
   number = 1//10 = 0
   exit while
'''
# number of 9's from 1 to 100
count = 0
for num in range(1,101):
    temp = num
    while temp> 0:
        digit =  temp % 10
        if digit ==  9:
            count+=1
        temp//=10
print("Total Number of 9's : ",count)
    
    
     





