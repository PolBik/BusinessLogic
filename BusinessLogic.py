# ALL monetary values are in CAD
# Item Catalog
catalogue = ["1", "2","3", "4", "5", "6", "7"]

# Payment Options
payment_options = ["Visa", "Mastercard", "Debit", "PayPal"]



# "Acquisition" Prices from the items

item1_construct_price = 5
item2_construct_price = 10.00
item3_construct_price = 15.00
item4_construct_price = 20.00
item5_construct_price = 25.00
item6_construct_price = 30.00
item7_construct_price = 35.00

# Shipping costs for Canada

item1_shipping_price_CDN = 10.00
item2_shipping_price_CDN = 10.00
item3_shipping_price_CDN = 10.00
item4_shipping_price_CDN = 20.00
item5_shipping_price_CDN = 20.00
item6_shipping_price_CDN = 20.00
item7_shipping_price_CDN = 30.00
# Mark up multiplier (same for all countries)

items_price_multiplier = 1.60

#Available items
item1 = 1
item2 = 2
item3 = 3
item4 = 4
item5 = 5
item6 = 6
item7 = 7

requested_number = input("Enter the item number you want to purchase, please?\n")

 
if requested_number in catalogue:

    print( "You've chosen item " + requested_number)

else:
    print("error 01, try again, this item does not seem to be in sale right now :/")
    exit()

# Math part here
if requested_number =="1":
    price = (item1_construct_price*items_price_multiplier) + item1_shipping_price_CDN
    print(str(price) + " is your price")

elif requested_number =="2":
    price = (item2_construct_price*items_price_multiplier) + item2_shipping_price_CDN
    print(str(price) + " is your price")

elif requested_number =="3":
    price = (item3_construct_price*items_price_multiplier) + item3_shipping_price_CDN
    print(str(price) + " is your price")

elif requested_number =="4":
    price = (item4_construct_price*items_price_multiplier) + item4_shipping_price_CDN
    print(str(price) + " is your price")

elif requested_number =="5":
    price = (item5_construct_price*items_price_multiplier) + item5_shipping_price_CDN
    print(str(price) + " is your price")

elif requested_number =="6":
    price = (item6_construct_price*items_price_multiplier) + item6_shipping_price_CDN
    print(str(price) + " is your price")

elif requested_number =="7":
    price = (item7_construct_price*items_price_multiplier) + item7_shipping_price_CDN
    print(str(price) + " is your price")

else:
    print("error 02, there seems to be an issue with your price")
    exit()

# Payment options Fees, ugh
PayPal = 0.0290 * price
Mastercard = 0.0115 * price + 0.05
Visa = 0.0115 * price + 0.05
Interac = 0.02

pay = input("Debit, Mastercard, Visa or PayPal?\n")

if pay in payment_options:
    print("Good")
else:
    print("error 03, This does not seem to be a supported payment method")
    exit()

#Payment method percentages added

if  pay == "Debit":

    full_price_raw = price + Interac

elif pay == "Mastercard":
    full_price_raw = price + Mastercard

elif pay == "Visa":
    full_price_raw = price + Visa

elif pay == "PayPal":
    full_price_raw = price + PayPal

else:
    print("error 04,the payment method was not found, try again")
    exit()

price_polished = round(full_price_raw, 2)
print("Your Full price was," + str(price_polished) + "CAD" + "\nProcessing payment now." )
 
import pandas as pd

daily_customer_set = { 
     "Items" : ["item "+ requested_number ],
     "Prices": price_polished
}

daily_customer_sheet = pd.DataFrame(daily_customer_set)

print(daily_customer_sheet)
    
