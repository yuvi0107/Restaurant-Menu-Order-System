#Define the menu of the restaurant
menu = {
    'spicy chicken':150,
    'Cocktails ':195,
    'Burger':60,
    'Fruit Salad':99,
    'Coffee':80,
}

#Greet
print("Welcome to Zisma Restaurant")
print("spicy chicken: RS150\nCocktails: RS195\nBurger: RS60\nFruit Salad: RS99\nCoffee: RS80")

order_total = 0
#150 + 60 = 210

item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1] #0 +60
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of seconnd item = ")
    if item_2 in menu:
        order_total += menu [item_2]
        print(f"Item {item_2}has been added to order")
    else:
        print(f"Ordeed item {item_2}is not available!")
print(f"The total amount of items to pay is  {order_total}") 
