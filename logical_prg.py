'''
#Prime number

number = int(input("Enter a number : "))
if number <= 1 :
    print("Not a Prime Number")
else:
    is_prime = True
    for i in range(2,int(number//2)+1):
       if number%i == 0:
          is_prime = False
          break
    if is_prime == True:
       print("It is a prime number")
    else:
       print("Not a prime number")   
'''
'''
#fibonacci series


n = int(input("Enter a number : "))
a = 0
b = 1

for i in range(n):
   print(a,end=",")
   c = a+b
   a = b
   b = c
'''
'''
#palindrome

number = int(input("Enter a number : "))
temp =number
reverse = 0
while number > 0:
   remainder = number%10
   reverse = reverse*10+remainder
   number = number//10

if temp == reverse:
   print("Number is Palindrome")
else:
   print("Not a palindrome")

#Palindrome - String

str = input("Enter a string : ")
rev = ""

for i in str:
   rev = i + rev

if str == rev:
   print(f"{rev} is a Palindrome")
else:
   print("Not a palindrome")

'''
'''
#count the number of digits
number = int(input("Enter a number : "))
count = 0
temp = abs(number)

if temp == 0:
   count = 1
else:
   while temp > 0:
     temp = temp//10
     count+=1

print("Count is :",count)
'''
'''
#Sum of digits
number = int(input("Enter a number : "))
sum_digits = 0
temp = abs(number)

while temp > 0:
   digit = temp%10
   sum_digits += digit
   temp = temp//10

print("Sum of digits : ",sum_digits)
'''
'''
#Product of digits
number = int(input("Enter a number : "))
product_digits = 0
temp = abs(number)

while temp > 0:
   digit = temp%10
   product_digits *= digit
   temp = temp//10

print("Product of digits : ",product_digits)
'''