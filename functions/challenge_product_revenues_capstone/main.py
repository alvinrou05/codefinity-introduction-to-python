# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenues = []
    
    for price, quantity in zip(prices, quantities_sold):
        revenues.append(price * quantity)
    return revenues

def formatted_output(revenue_per_product):
    sorted_list = sorted(revenue_per_product)
    for product, revenue in sorted_list:
        print(f"{product} has total revenue of ${revenue}")

revenues = calculate_revenue(prices, quantities_sold)

revenue_per_product = list(zip(products, revenues))

formatted_output(revenue_per_product)
#for product, revenue in revenue_per_product:
    #print(f"{product} has total revenue of ${revenue}")

print()
# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")