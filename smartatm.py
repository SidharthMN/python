print("----------- SMART ATM SYSTEM ----------- ")
customer_name = input("Customer Name : ")
card_no = input("Card Number : ")
pin_no = int(input("PIN Number : "))
acc_type = input("Account Type : ")
avail_balance = float(input("Available Balance : "))
withdraw_amt = float(input("Withdraw Amount : "))

if acc_type in ["Savings", "Current"]:
    print("Valid Account Type : True")
else:
    print("Valid Account Type : False")

stored_pin = [1234,2255,3366,4488,5522]
if pin_no in stored_pin :
    print ("PIN Verified : True")
else :
    print("PIN Verified : False")   


if avail_balance > 0 :
    print("Sufficient Balance : True ")
else :
    print("Sufficient Balance : False ")

remaining_balance = avail_balance - withdraw_amt
print("Remaining Balance : ",remaining_balance)

if remaining_balance != avail_balance:
    print("Transaction Status : Successful")
else:
    print("Transaction Status : Unsuccessful")

print("Datatype of Balance : ",type(avail_balance))
print("Datatype of Balance : ",type(withdraw_amt))

print("Is Balance Float : ",isinstance(avail_balance,float))
print("Is Withdraw Float : ",isinstance(withdraw_amt,float))

print("ID of Balance : ",id(avail_balance))
print("ID of Withdraw : ",id(withdraw_amt))
 
account1 = "Savings"
account2 = "Savings"

if account1 is account2 :
    print("Account1 is Account2 : True")
else:
    print("Account1 is  Account2 : False")

if account1 is not account2 :
    print("Account1 is not Account2 : True")
else:
     print("Account1 is not Account2 : False")