from utils import MENU, calculate_subtotal, calculate_gst, calculate_total, print_menu, print_bill

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid whole number.")

def get_order_type():
    while True:
        print("\nSelect Order Type")
        print("1. Dine-In")
        print("2. Takeaway")
        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                return "Dine-In"
            if choice == 2:
                return "Takeaway"
            print("Please choose 1 or 2.")
        except ValueError:
            print("Please enter 1 or 2.")

def add_items(order):
    while True:
        print_menu()
        print("0. Finish Order")
        try:
            item_number = int(input("\nEnter item number: "))
        except ValueError:
            print("Please enter a valid item number.")
            continue
        if item_number == 0:
            break
        if item_number not in MENU:
            print("Invalid item number!")
            continue
        quantity = get_positive_integer("Quantity: ")
        order[item_number] = order.get(item_number, 0) + quantity
        print(f"{quantity} x {MENU[item_number]['name']} added!")

def show_current_order(order):
    if not order:
        print("\nNo items have been ordered yet.")
        return
    print("\n----------- CURRENT ORDER -----------")
    for item_number, quantity in order.items():
        item = MENU[item_number]
        print(f"{item['name']:<15} x {quantity:<3} INR {item['price'] * quantity:.2f}")
    print("-------------------------------------")
    print(f"Subtotal: INR {calculate_subtotal(order):.2f}")

def generate_bill(name, order_type, order):
    if not order:
        print("\nYour order is empty.")
        return False
    subtotal = calculate_subtotal(order)
    gst = calculate_gst(subtotal)
    total = calculate_total(subtotal)
    print_bill(name, order_type, order, subtotal, gst, total)
    return True

def main():
    print("===================================")
    print("       WELCOME TO PYTHON BISTRO")
    print("===================================")
    name = input("Enter your name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    order_type = get_order_type()
    order = {}

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. View Menu & Place Order")
        print("2. View Current Order")
        print("3. Generate Bill")
        print("4. Exit")
        print("===============================")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid menu choice.")
            continue

        if choice == 1:
            add_items(order)
        elif choice == 2:
            show_current_order(order)
        elif choice == 3:
            if generate_bill(name, order_type, order):
                print("\nOrder completed successfully!")
                break
        elif choice == 4:
            print("\nThank you for visiting Python Bistro!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
