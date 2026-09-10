# code challenge 

name = input(">> ENTER YOUR NAME <<" )
item = input("What would be the item?")

is_fragile = bool(input("Is the item fragile?")) == "yes"

weight = float(input(">> ENTER THE WIEGHT OF THE ITEM IN Kg <<"))
distance = float(input(">> ENETER THE DISTANCE TAHT YOU WANT TO SHIP THE ITEM IN Km <<")) 

is_express = bool(input("Is the shipping express?")) == "yes"
is_international = bool(input("Is the shipping international?"))  == "yes"

# base cost calculation
base_cost = (weight * 2.50) + (distance * 0.15)

if weight <= 2 and distance <= 100 and  not is_express  and not is_international :
    total = 0.00
    print("The shipping cost is $ 0.00")
    print("THE SHIPPING IS FREE")

elif is_express and is_international :
    total = (base_cost * 1.40) + 50
    print("The shipping cost is $ ", total)
    print("THE SHIPPING IS EXPRESS AND INTERNATIONAL")

elif  is_international and weight > 20:
    total = (base_cost * 1.20) + 25
    print("The shipping cost is $ ", total)
    print("THE SHIPPING IS EXPRESS")

elif weight > 30 or distance > 1000:
    total = base_cost + 30
    print("The shipping cost is $ ", total)
    print("THE ITEM IS OVERSIZED ")

else:
    total = base_cost
    print("The shipping cost is $ ", total)

