import json

def calculate_total_cost(products):
    total_cost = 0
    for product in products:
        total_cost += product['price']
    return total_cost

def main():
    
    with open("/home/hp/Skillohomework/homework_5/homework9/products.json", "r") as file:
        products = json.load(file)

   
    total_cost = calculate_total_cost(products)

    
    print("Total cost of all products:", total_cost)

if __name__ == "__main__":
    main()
