'''
n = 4
for row in range(1,n+1):
    for column in range(1,n+1):
        print("*",end="")
    print()
'''
'''
n = 4 
for row in range(1,n+1):
    for column in range(1,row+1):
        print("*",end="") #use row and column instead of "*"
    print()
'''

'''
*****
****
***
**
*
'''
'''
n = 5
for row in range(n):
    for column in range(1,n-row+1):
        print("*",end="")
    print()
'''

'''
----*
---**
--***
-****
*****


'''
'''
n=4
for row in range(1,n+1):
    for column in range(1,n-row+1):
        print(" ",end="")
    for column in range(1,row+1):
        print("*",end="")
    print()
 '''   

n = 4
for row in range(1,n+1):
    for column in range(1,n+1):
        if column <= n-row:
            print(" ",end="")
        else:
            print("*",end ="")
    print()

'''
1
2 3
4 5 6
7 8 9 10
'''
'''
1 
3 2
4 5 6
10 9 8 7
11 12 13 14 15
'''
'''
'''
number=int(input("Enter Total Rows: "))
i=1
while i<=10:
    for row in range(1,number+1):
        for col in range(1,row+1):
                print(i,end=" ")
                i+=1
        print()