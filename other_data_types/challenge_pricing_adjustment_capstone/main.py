grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}
#先把货物分类三项 类别、价格、数量
eggs_category, eggs_price, eggs_stock = grocery_inventory["Eggs"]
#按照不同的类型去执行
if eggs_price > 5: #如果鸡蛋价格大于5就会执行下一步
    print("Eggs are too expensive, reducing the price by $1.") #打印会扣一块
    grocery_inventory["Eggs"] = (eggs_category, eggs_price - 1, eggs_stock) #执行优惠扣一块
else: #如果没有大于5就执行这一步
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes":("Produce", 1.20, 30)}) #添加新的物品信息
print("Inventory after adding Tomatoes: ", grocery_inventory["Tomatoes"]) #打印出来

Milk_category, Milk_price, Milk_stock = grocery_inventory["Milk"] #分类牛奶
if Milk_stock < 10: #库存少过10执行这一步
    print("Milk needs to be restocked. Increasing stock by 20 units.") #打印需要补货
    grocery_inventory["Milk"] = (Milk_category, Milk_price, Milk_stock + 20) #执行加20库存
else:
    print("Milk has sufficient stock.") #反之打印这个
apple_category, apple_price, apple_stock = grocery_inventory["Apples"] #把apples也分类出来
if apple_price > 2: #价格大于2执行
    grocery_inventory.pop("Apples") #pop移除字典元组
else:
    pass #结束结果

print("Updated inventory:", grocery_inventory) #打印更新后列表