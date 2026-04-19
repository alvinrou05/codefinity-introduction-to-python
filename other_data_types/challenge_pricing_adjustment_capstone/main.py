grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}
#先把货物分类三项 类别、价格、数量
eggs_category, eggs_price, eggs_stock = grocery_inventory["Eggs"]
#按照不同的类型去执行
if eggs_price > 5: #如果价格大于5就会执行下一步
    print("Eggs are too expensive, reducing the price by $1.") #打印的
    grocery_inventory["Eggs"] = (eggs_category, eggs_price - 1, eggs_stock) #执行优惠扣一块
else: #如果没有大于5就执行这一步
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes":("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes: ", grocery_inventory["Tomatoes"][2])

Milk_category, Milk_price, Milk_stock = grocery_inventory["Milk"]
if Milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (Milk_category, Milk_price, Milk_stock + 20)
else:
    print("Milk has sufficient stock.")
apple_category, apple_price, apple_stock = grocery_inventory["Apples"]
if apple_price > 2:
    grocery_inventory.pop("Apples")
else:
    pass

print("Updated inventory:", grocery_inventory)