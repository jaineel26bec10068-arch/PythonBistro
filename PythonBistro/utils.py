MENU = {
    1: {"name": "Burger", "price": 120},
    2: {"name": "Pizza", "price": 180},
    3: {"name": "Pasta", "price": 150},
    4: {"name": "French Fries", "price": 80},
    5: {"name": "Sandwich", "price": 100},
    6: {"name": "Cold Coffee", "price": 70},
    7: {"name": "Coke", "price": 50},
    8: {"name": "Coffee", "price": 25},
    9: {"name": "Tea", "price": 20},
    10: {"name": "Thali", "price": 180},
}

GST_RATE = 0.05

def calculate_subtotal(order):
    return sum(MENU[item]["price"] * quantity for item, quantity in order.items())

def calculate_gst(subtotal):
    return subtotal * GST_RATE

def calculate_total(subtotal):
    return subtotal + calculate_gst(subtotal)

def print_menu():
    print("\n----------- MENU -----------")
    for number, item in MENU.items():
        print(f"{number}. {item['name']:<13} - INR {item['price']}")
    print("----------------------------")

def print_bill(name, order_type, order, subtotal, gst, total):
    print("\n===================================")
    print("             FINAL BILL")
    print("===================================")
    print("Customer:", name)
    print("Order Type:", order_type)
    print("-----------------------------------")
    for item_number, quantity in order.items():
        item = MENU[item_number]
        print(f"{item['name']:<15} x {quantity:<3} INR {item['price'] * quantity:.2f}")
    print("-----------------------------------")
    print(f"Subtotal:   INR {subtotal:.2f}")
    print(f"GST 5%:     INR {gst:.2f}")
    print(f"Final Bill: INR {total:.2f}")
    print("===================================")
    print("Thank you for visiting Python Bistro!")
    print("===================================")
