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

#fibonacci series


n = int(input("Enter a number : "))
a = 0
b = 1

for i in range(n):
   print(a,end=",")
   c = a+b
   a = b
   b = c
