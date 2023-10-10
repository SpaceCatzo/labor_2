groceries = {}

# asking for a data
shops_count = int(input("Enter the number of shops: "))
shops = []

for i in range(shops_count):
    shop = input(f"Enter the name of {i + 1} shop: ")
    shops.append(shop)
    groceries[shop] = {}
    for grocery_item in input(f"Enter the groceries list separated by commas for {shop}: ").split(','):
        price = float(input(f"Enter the price for '{grocery_item}' in {shop}: "))
        groceries[shop][grocery_item] = price

# calculating the ntotal price
purchases_cost = {}

for shop, prices in groceries.items():
    total_cost = sum(prices.values())
    purchases_cost[shop] = total_cost

# find the best shop
saved_money = {}

for shop, price in groceries.items():
    saved_money[shop] = purchases_cost[shop] - min(purchases_cost.values())

best_shop = max(saved_money, key=saved_money.get)

# results
print("\nTotal cost in each shop :")
for shop, cost in purchases_cost.items():
    print(f"{shop}: {cost} €.")

print(f"\nThe most profitable shop: {best_shop}")