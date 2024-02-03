# Global dictionary variable to store shopping carts for each customer
shopping_carts = {}

def add_item(customer_id, item, price):
    if customer_id not in shopping_carts:
        shopping_carts[customer_id] = {}

    if item in shopping_carts[customer_id]:
        shopping_carts[customer_id][item] += 1
    else:
        shopping_carts[customer_id][item] = 1

    print(f"{item} added to the cart for customer {customer_id}.")

def remove_item(customer_id, item):
    if customer_id in shopping_carts and item in shopping_carts[customer_id]:
        if shopping_carts[customer_id][item] > 1:
            shopping_carts[customer_id][item] -= 1
        else:
            del shopping_carts[customer_id][item]
        print(f"{item} removed from the cart for customer {customer_id}.")
    else:
        print(f"{item} not found in the cart for customer {customer_id}.")

def calculate_total_price(customer_id):
    if customer_id in shopping_carts:
        total_price = sum(quantity * price for item, quantity, price in shopping_carts[customer_id].items())
        return total_price
    else:
        return 0

def display_cart(customer_id):
    if customer_id in shopping_carts:
        print(f"Shopping Cart for customer {customer_id}:")
        for item, quantity in shopping_carts[customer_id].items():
            print(f"{item}: {quantity}")
        total_price = calculate_total_price(customer_id)
        print(f"Total Price: ${total_price:.2f}")
    else:
        print(f"Shopping Cart not found for customer {customer_id}.")

def main():
    while True:
        print("\nOnline Shopping Cart Simulator")
        print("1. Add Item to Cart")
        print("2. Remove Item from Cart")
        print("3. Display Cart")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            customer_id = input("Enter customer ID: ")
            item = input("Enter item name: ")
            price = float(input("Enter item price: "))
            add_item(customer_id, item, price)

        elif choice == '2':
            customer_id = input("Enter customer ID: ")
            item = input("Enter item name to remove: ")
            remove_item(customer_id, item)

        elif choice == '3':
            customer_id = input("Enter customer ID: ")
            display_cart(customer_id)

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
