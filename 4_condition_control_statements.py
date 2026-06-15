#syntax if - else
'''
if condition:
    code to be executed
else :

if - elif -else :
    
if condition : 
    code to be executed
elif condition :
    code to be executed
else :
'''

#To check whether a no is positive or negative
'''
num = int(input("Enter a Number : "))
if num>0:
    print("Positive Number")
else:
    print("Negative Number")
'''
#To check wheteher a no is vowel or constant
'''
vowel_check = input("Enter a character : ")
if vowel_check in 'aeiouAEIOU' :
    print("Vowel")
else : 
    print("Consonant")
'''
'''
odd_even = int(input("Enter a number : "))
if odd_even%2 == 0:
   print("Number is even")
else:
   print("Number is odd")
'''

'''
age = int(input("Enter the age : "))
if age <= 13 :
   print("Child")
elif age <= 18 :
   print("Teenager")
elif age <= 60 :
   print("Adult")
else:
   print("Senior Citizen")
'''

#program to check whether given number is positive and ever or positive and odd number or negative
'''
num = int (input("Enter the number : "))
if num > 0:
    if num % 2 == 0:
        print("Number is positive and even")
    else:
        print("Number is postive and odd")
else:
    print("Number is negative")
'''
#To check whether the number is 3 digit or not
'''
num=int(input("Enter a number : "))
if num > 99 and num < 1000 : #99<num<1000
    print("It's a 3 digit number")
else:
    print("It's not 3 digit number")
'''
#Simple ATM Program

balance_amt = 150000
withdraw_amt = int(input("Enter the withdraw amount : "))
if withdraw_amt <= balance_amt:
    print("Cash Debited")
else:
    print("Insufficient Balance")
