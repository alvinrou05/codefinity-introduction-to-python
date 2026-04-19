# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for 食物 in range(5):
    weekday = weekdays[食物]
    优惠天 = daily_promotions[食物]
    print(f"{weekday}: Promotion on {优惠天}")