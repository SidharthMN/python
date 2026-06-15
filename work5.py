customer_name = input("Customer Name : ")
mobile_no = int(input("Mobile Number : "))
food_item = input("Food Item Name : ")
quantity = int(input("Quantity : "))
price_per_item = float(input("Price Per Item : "))
delivery_distance = float(input("Delivery Distance (in KM) : "))
premium_status = bool(input("Premium Membership Status (True/False) : "))

def calculate_food_amount(quantity,price_per_item):
    total_amount = quantity*price_per_item
    return total_amount

total_amount =calculate_food_amount(quantity,price_per_item)
print("Total Food Amount : ",total_amount)

def calculate_delivery_charge(delivery_distance): 
    if delivery_distance < 5:
        delivery_charge = "40 Rupees"
    elif delivery_distance >= 5:
        delivery_charge = "80 Rupees"
    else:
        delivery_charge = "0"
    return delivery_charge

delivery_charge = calculate_delivery_charge(delivery_distance)
print("Delivery Charge : ",delivery_charge)

def calculate_discount(total_amount,premium_status):
    if premium_status  and total_amount >1000:
        discount = 150
        bill_amount = total_amount - discount
    else:
        discount = 0
        bill_amount = total_amount

    return bill_amount,discount

quantity_datatype = type(quantity)
price_datatype = type(price_per_item)
premium_status_datatype = type(premium_status)

quantity_int = isinstance(quantity,int)
price_float = isinstance(price_per_item,float)
premium_bool = isinstance(premium_status,bool)

bill_amount , discount = calculate_discount(total_amount,premium_status)
print("Bill Amount : ",bill_amount)
print("Discount : ", discount)

amount_id=id(total_amount)
bill_id=id(bill_amount)
offer="Free Soft Drink on Orders Above 1500"
result=food_item

def generate_bill(**details):
    print("----FOOD ORDER BILL-----")
    for key,value in details.items():
        print(f"{key.replace('_' ,' ')} : {value}")
    return details

generate_bill(
    Customer_Name=customer_name,
    Mobile_No=mobile_no,
    Food_Item=food_item,
    Discount = discount,
    Quantity=quantity,
    Price_Per_Item=price_per_item,
    Total_Amount=total_amount,
    Delivery_Charge=delivery_charge,
    Premium_Status=premium_status,
    Final_Bill_Amount=bill_amount,
    Quantity_Datatype=quantity_datatype,
    Price_Datatype=price_datatype,
    Premium_Status_Datatype=premium_status_datatype,
    Is_Quantity_Integer=quantity_int,
    Is_Price_Float=price_float,
    Is_Premium_Member_Boolean=premium_bool,
    ID_of_Food_Amount=amount_id,
    ID_of_Total_Bill_Amount=bill_id,
    Offer=offer,
    Food_Search_Result=result
)



