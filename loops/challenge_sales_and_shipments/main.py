# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

for jieguo in range(len(products)):
    products[jieguo][1] -= units_sold[jieguo][1]
for jiejie in range(len(products)):
    products[jiejie][1] += shipment_received[jiejie][1]
print(f"Final stock levels for all products: {products}")