#define the menu of resturent
menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
    'Noodels':60,
    'Chai':20,
    'Coldrink':40,
    'Kheer':30,
    'Cold Coffee':90,
    
}
#Greet
print("Welcome to PYTHONN Restaurant")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80\nNoodels: Rs60\nChai: Rs20\nColdrink: Rs40\nKheer: Rs30\nCold Coffee: Rs90" )

order_total = 0
#80 + 70 + 150
item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu [item_1] #0 + 50
    print(f"Your item {item_1} hes been added to your order")
else:
    print(f"Ordered item {item_1} is not avaialable yet!")
    another_order = input("Do you want to add another item? (Yes/No)")
    if another_order == "Yes":
       
        item_2 = input("Enter the name of second item  =")
if item_2 in menu:
    order_total += menu [item_2]
    print(f"Item {item_2} has been added to order")
else:
    print(f"Ordered item {item_2} is not avaialable!")
    
    print(f"The total amount of items to pay is {order_total}")