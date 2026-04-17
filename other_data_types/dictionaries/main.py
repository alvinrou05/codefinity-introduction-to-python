grocery_inventory = {
    "Mike":(113,"Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}
bread_details = grocery_inventory.get("Bread")
grocery_inventory.update({"Cookies": (143, "Bakery")})
grocery_inventory.pop("Eggs")

print("Details of Bread:",bread_details)
print("Inventory after adding Cookies:",grocery_inventory)
print("Inventory after removing Eggs:",grocery_inventory)