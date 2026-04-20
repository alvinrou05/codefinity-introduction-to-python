# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}
for neirong,ziliao in inventory.items():
    kucun = ziliao[0]
    yuanjia = ziliao[1]
    dazejia = ziliao[2]
    if kucun < 30:
        print(f"{neirong} need restocking.")
    elif kucun > 100:
        print(f"{neirong} should be sold at the discounted price of {dazejia}.")
    else:
        print(f"{neirong} should be sold at the regular price of {yuanjia}.")