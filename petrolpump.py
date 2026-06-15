user_name=input("Enter the user name : ")
vehicle_no=input("Enter the vehicle number : ")
fuel_type=input("Enter the fuel type : ")
litres_filled=float(input("Enter the litres filled : "))
price_per_litre=int(input("Enter the price per litre : "))
premium_card=bool(input("Is the person haves a premium card (T/F) : "))

total = litres_filled * price_per_litre
gst = total * 5 / 100
final_amount = total + gst

print("-------- PETROL BILL---------")

print("Enter Customer Name : ",user_name)
print("Enter Vehicle Number : ",vehicle_no)
print("Enter Fuel Type : ",fuel_type)

print("Fuel Amount : ",total)
print("GST Amount : ",gst)
print("Final Bill Amount : ",final_amount)

print("Datatype of Litres : ",type(litres_filled))
print("Datatype of premium card : ",type(premium_card))

print("Is litres float? ",isinstance(litres_filled,float))
print("Is premium card boolean? ",isinstance(premium_card,bool))

print("ID of Total Amount",id(final_amount))
print("ID of Final Amount",id(total))



'''
final_amount1=36000
final_amount1 += 5000
print(final_amount1)
final_amount1 -= 3000
print(final_amount1)
final_amount1 *= 100
print(final_amount1)

print("Logical Operators")

premium_card = True
if premium_card and final_amount > 3000:
   discount = 200
   final_amount -= discount
else:
   print("Sorry No Discounts Available : ")


print("Type of user name : ",type(user_name))   
print("Type of vehicle number : ",type(vehicle_no))
print("Type of fuel type : ",type(fuel_type))
print("Type of litres filled : ",type(litres_filled))
print("Type of price per litre : ",type(price_per_litre))
print("Type of premium card : ",type(premium_card))
print("Type of final amount : ",type(final_amount))
print("Type of total : ",type(total))
print("Type of gst : ",type(gst))


print(isinstance(litres_filled,float))
print(isinstance(premium_card,bool))


print(id(final_amount))
print(id(total))
'''




