prices = [29.99, 45.50, 12.75, 38.20]
discount_messages = [
    "apply a 10% discount",
    "apply a 20% discount",
    "apply a 15% discount",
    "apply a 5% discount"
]
discount_persen = [
    0.1 , 0.2 , 0.15 , 0.05
]

for jiage in range(len(prices)):
    print(f"{jiage} {discount_messages[jiage]}")
    prices[jiage] -= prices[jiage] * discount_persen[jiage]
    
    print(f"Updated price for item {jiage}: ${prices[jiage]:.2f}")
