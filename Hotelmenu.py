# Menu of the restaurant

menu = {
    "Coffee": 50,
    "Tea": 35,
    "Sandwich": 40,
    "Veg-puff": 30,
    "pizza": 60
}
# Greet
print("Welcome to Python Restaurant")
print(" Coffee:50 Rs\n Tea:35 Rs\n Sandwich:40 Rs\n Veg-puff:30 Rs\n Pizza:60 Rs")

total_price = 0

item1 = input("Please tell me what you want to order: ")
if item1 in menu:
    total_price += menu[item1]
    print(f"your {item1} is added successfully and your total price is {total_price} ")

else:
    print("This item is not available")

another_order = input("Do you want something else ? (Yes or No)")
if another_order == "Yes":
    item2 = input("enter the name of the item: ")
    if item2 in menu:
        total_price += menu[item2]
        print(f"your {item2} is added successfully and your total price is {total_price} ")
else:
    print("Thankyou for your order,have a nice day")
