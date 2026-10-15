# cafe.py

cafe_name = "Python Café"
tax_rate = 0.08

# the menu
menu = {
    "espresso": 3.00,
    "latte": 4.50,
    "cappuccino": 4.25,
    "americano": 5.00,
    "chocolate muffin": 2.50,
    "croissant": 3.25,
}

# the order
order = []

# print a welcome message
def greet(name):
    print(f"Welcome to {cafe_name}, {name}!")

# loop through the menu and print every item with its price.
def show_menu(menu):
    print("--- MENU ---")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

# show everything in the order
def show_order(order, menu):
    if len(order) == 0:
        print("Your order is empty.")
    else:
        print("--- YOUR ORDER ---")
        for item in order:
            print(f"{item}: ${menu[item]:.2f}")
        print(f"Items: {len(order)}")

# add up the price and return the total.
def calculate_subtotal(order, menu):
    total = 0.0
    for item in order:
        total = total + menu[item]
    return total

# discount 
def get_discount(subtotal, is_member):
    if is_member and subtotal >= 20:
        discount = subtotal * 0.15
    elif is_member and subtotal >= 10:
        discount = subtotal * 0.10
    elif not is_member and subtotal >= 25:
        discount = subtotal * 0.05
    else:
        discount = 0.0
    return discount

# full receipt at checkout
def print_receipt(name, order, menu, is_member):
    subtotal = calculate_subtotal(order, menu)
    discount = get_discount(subtotal, is_member)
    # tax is figured after the discount is taken off.
    tax = (subtotal - discount) * tax_rate
    total = (subtotal - discount) + tax

    print(f"===== {cafe_name} RECEIPT =====")
    print(f"Customer: {name}")
    for item in order:
        print(f"{item}: ${menu[item]:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")

    # only non-members see the rewards club message
    if not is_member:
        print("Join our rewards club to save on every order!")

    print(f"Thanks for visiting, {name}!")

# it starts here.
print(f"*** {cafe_name} ***")
name = input("What's your name? ")
greet(name)

# is_member is only true if they type "yes"
answer = input("Are you a rewards member? (yes/no) ")
is_member = answer.lower() == "yes"

# keep showing the list until the customer checks out
while True:
    print()
    print("1. View menu")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. View my order")
    print("5. Checkout")
    choice = input("Choose an option (1-5): ")

    # view the menu
    if choice == "1":
        show_menu(menu)

    # add an item
    elif choice == "2":
        item = input("What would you like? ").lower()
        if item in menu:
            quantity = int(input("How many? "))
            if quantity >= 1:
                for i in range(quantity):
                    order.append(item)
                print(f"Added {quantity} {item} to your order.")
            else:
                print("Error: the quantity must be at least 1.")
        else:
            print(f"Sorry, we don't have {item} on the menu.")

    # remove an item
    elif choice == "3":
        item = input("Which item should I remove? ").lower()
        if item in order:
            order.remove(item)
            print(f"Removed one {item}.")
        else:
            print(f"{item} isn't in your order.")

    # view the order
    elif choice == "4":
        show_order(order, menu)

    # checkout
    elif choice == "5":
        if len(order) == 0:
            print("Your order is empty. Please add something first.")
        else:
            print_receipt(name, order, menu, is_member)
            break

    # anything else
    else:
        print("Please choose a number from 1 to 5.")
