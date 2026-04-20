# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started:", inventory)

for item, data in inventory.items():
    print(f"Processing {item}")
    current_stock = data[0]
    min_stock = data[1]
    restock_qty = data[2]
    on_sale = data[3]
    # while 补货
    while current_stock < min_stock:
        current_stock += restock_qty
    # 更新库存
    data[0] = current_stock
    # 折扣判断
    if current_stock > discount_threshold and not on_sale:
        data[3] = True

print("Processing completed")